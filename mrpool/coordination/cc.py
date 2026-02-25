from __future__ import annotations
import numpy as np

def coordination_coefficient(x: np.ndarray, y: np.ndarray) -> float:
    """Minimal CC: Pearson correlation on aligned series."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.size != y.size:
        raise ValueError("x and y must have same length")
    x = x - x.mean()
    y = y - y.mean()
    denom = (np.sqrt((x*x).sum()) * np.sqrt((y*y).sum()))
    if denom == 0:
        return 0.0
    return float((x*y).sum() / denom)
