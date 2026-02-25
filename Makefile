.PHONY: install test smoke
install:
	python -m pip install -r requirements.txt
test:
	pytest -q
smoke:
	python experiments/benchmark_ray.py --quick
	python experiments/gnn_hjb_control.py --quick
