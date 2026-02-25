# Metrics Governance (metrics_v1.0)

Freeze definitions for pilot success metrics to avoid baseline bias and moving goalposts.

## Primary Metrics
- X: coordinated escape rate reduction (uplift)
- Y: coordinated cluster growth suppression (slope-based)
- Z: P95 latency impact (ms)

## Statistical Method
- Bootstrap percentile CI for uplift and quantiles.
- Pass/fail: require empirical probability ≥ 0.95 (bootstrap) to satisfy thresholds.

## Change Control
- Any definition changes must be versioned (metrics_v1.1) and may reset baseline periods.
