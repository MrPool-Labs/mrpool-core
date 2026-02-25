# Mr.Pool Core

Adaptive stochastic control for coordinated adversarial ecosystems.

**Open Core (Apache-2.0)**: research framework, reproducible experiments, paper-ready artifacts.  
**Enterprise**: production ingestion/enforcement/RBAC/observability (see `ENTERPRISE.md`).

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

pytest -q
python experiments/benchmark_ray.py --quick
python experiments/gnn_hjb_control.py --quick
```

## Landing page

Bilingual landing page in `site/index.html`.  
Enable GitHub Pages: Settings → Pages → Deploy from branch → `main` → `/site`.

## Releases

Publishing a GitHub Release triggers `.github/workflows/release-paper.yml`, which compiles `paper/main.tex`
and uploads `paper/_build/main.pdf` as a release asset.

## Enterprise Edition

See [ENTERPRISE.md](ENTERPRISE.md) for the production deployment and 30-day pilot program.

## Sales Ops

- LinkedIn content: `sales/linkedin_posts/`
- Outreach templates: `sales/outreach_templates/`
- 30-day daily plan: `sales/daily_plan_30_days_*`
- Pilot SOW (EN/PT): `sales/pilot_sow/`
- Metrics governance: `sales/metrics_governance/metrics_v1.0.md`

## License

Apache-2.0 (see `LICENSE`).
