import numpy as np
from mrpool.stats.bootstrap import bootstrap_ci, bootstrap_uplift_ci

def test_bootstrap_ci_mean():
    rng = np.random.default_rng(0)
    x = rng.normal(size=200)
    stat, lo, hi = bootstrap_ci(np.mean, x, n_boot=300)
    assert lo <= stat <= hi

def test_uplift_ci():
    stat, lo, hi = bootstrap_uplift_ci(30, 1000, 20, 1000, n_boot=300)
    assert lo <= stat <= hi
