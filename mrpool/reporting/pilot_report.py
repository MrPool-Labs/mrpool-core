from __future__ import annotations
import json
from dataclasses import dataclass, asdict
from mrpool.stats.bootstrap import bootstrap_uplift_ci

@dataclass
class PilotMetrics:
    escape_uplift: float
    escape_ci_lo: float
    escape_ci_hi: float

def compute_escape_uplift(e_b:int,n_b:int,e_p:int,n_p:int):
    return bootstrap_uplift_ci(e_b,n_b,e_p,n_p)

def export_json(path: str, metrics: PilotMetrics):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(asdict(metrics), f, ensure_ascii=False, indent=2)
