# Replay receipt

**Date:** 27 October 2026. **Input:** the final package code (`code/`, `pyproject.toml`, `uv.lock`), copied into an empty directory. **Runner:** the shared local research queue (1 CPU, 2 GB), macOS arm64, CPython 3.11 via uv.

| Order | Script | Exit | Output compared with shipped file |
|---|---|---|---|
| 1 | code/verify_determinant.py | 0 | evidence/determinant_certificate.json: byte-identical |
| 2 | code/verify_poisson.py | 0 | evidence/poisson_certificate.json: byte-identical |
| 3 | code/verify_scaling.py | 0 | evidence/independent_scaling_certificate.json: byte-identical |
| 4 | code/verify_extension.py | 0 | evidence/extension_certificate.json: byte-identical |
| 5 | code/plot_divergence.py | 0 | evidence/divergence.csv, figures/thermal_divergence.pdf and .png: byte-identical |
| 6 | code/census.py 100000 | 0 | evidence/census.json: byte-identical (about 10 minutes) |
| - | code/negative_controls.py | 0 | 4 baselines pass; all 11 corruptions rejected |

The publication gate repeats this replay from a fresh extraction of the frozen archive. Its log is retained privately with the publication receipts.
