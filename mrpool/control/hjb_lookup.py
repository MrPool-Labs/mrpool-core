from __future__ import annotations
import numpy as np
from dataclasses import dataclass

@dataclass(frozen=True)
class HJBLookup:
    """Parametric lookup table for optimal control u*(x)."""
    grid_x: np.ndarray
    grid_u: np.ndarray

    def evaluate(self, x: float) -> float:
        return float(np.interp(x, self.grid_x, self.grid_u))
