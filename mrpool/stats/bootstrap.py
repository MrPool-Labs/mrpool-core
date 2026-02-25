from __future__ import annotations
import numpy as np
from typing import Callable, Tuple

def bootstrap_ci(stat_fn: Callable[[np.ndarray], float],
                 data: np.ndarray,
                 n_boot: int = 2000,
                 alpha: float = 0.05,
                 rng: np.random.Generator | None = None) -> Tuple[float,float,float]:
    """Percentile bootstrap CI for a statistic."""
    rng = rng or np.random.default_rng(0)
    data = np.asarray(data)
    n = data.shape[0]
    boots = np.empty(n_boot, dtype=float)
    for i in range(n_boot):
        idx = rng.integers(0, n, size=n)
        boots[i] = stat_fn(data[idx])
    stat = float(stat_fn(data))
    lo, hi = np.quantile(boots, [alpha/2, 1-alpha/2])
    return stat, float(lo), float(hi)

def bootstrap_uplift_ci(e_b: int, n_b: int, e_p: int, n_p: int,
                        n_boot: int = 5000, alpha: float = 0.05,
                        rng: np.random.Generator | None = None):
    """Bootstrap CI for uplift Delta=(pB-pP)/pB using Bernoulli resampling."""
    rng = rng or np.random.default_rng(0)
    pB = e_b / n_b
    pP = e_p / n_p
    base = rng.binomial(1, pB, size=(n_boot, n_b))
    pil  = rng.binomial(1, pP, size=(n_boot, n_p))
    pB_b = base.mean(axis=1)
    pP_b = pil.mean(axis=1)
    delta = (pB_b - pP_b) / np.clip(pB_b, 1e-12, None)
    stat = (pB - pP) / max(pB, 1e-12)
    lo, hi = np.quantile(delta, [alpha/2, 1-alpha/2])
    return float(stat), float(lo), float(hi)
