import numpy as np
from collections import deque
from dataclasses import dataclass
import config


@dataclass
class AnomalyResult:
    step: int
    similarity: float
    is_anomaly: bool
    reason: str


class AnomalyDetector:

    def __init__(self, engine):
        self.engine = engine
        self.step = 0
        self.history = deque(maxlen=50)   # rolling window

    def process(self, vector):

        self.step += 1

        similarity = self.engine.search(vector)

        # ======================
        # WARMUP
        # ======================
        if self.step <= config.WARMUP_STEPS:
            self.engine.store(vector)
            self.history.append(similarity)

            return AnomalyResult(self.step, similarity, False, "WARMUP")

        # ======================
        # DYNAMIC BASELINE
        # ======================
        if len(self.history) < 10:
            self.history.append(similarity)
            return AnomalyResult(self.step, similarity, False, "COLLECTING")

        arr = np.array(self.history)

        mean = arr.mean()
        std = arr.std()

        # Avoid division issue
        if std < 1e-6:
            std = 1e-6

        # ======================
        # Z-SCORE DETECTION
        # ======================
        z_score = (similarity - mean) / std

        is_anomaly = z_score < -2.0   # adaptive threshold

        # ======================
        # LEARNING LOGIC
        # ======================
        if not is_anomaly:
            self.engine.store(vector)

        self.history.append(similarity)

        reason = f"Z={z_score:.2f}"

        return AnomalyResult(
            self.step,
            similarity,
            is_anomaly,
            reason
        )