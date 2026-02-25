from __future__ import annotations
import argparse
import numpy as np
import ray

@ray.remote
def simulate(seed: int, n: int):
    rng = np.random.default_rng(seed)
    x = rng.standard_normal(n).cumsum()
    hit = float((x > 10).any())
    return hit

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()

    ray.init(ignore_reinit_error=True, include_dashboard=False)
    N = 200 if args.quick else 20000
    n = 500 if args.quick else 5000
    tasks = [simulate.remote(i, n) for i in range(N)]
    hits = ray.get(tasks)
    print({"N": N, "hit_rate": float(np.mean(hits))})

if __name__ == "__main__":
    main()
