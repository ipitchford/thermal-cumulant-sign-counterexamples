# Reproducibility supplement

Run every command from the bundle root (the directory holding `pyproject.toml`).
Dependencies are declared in `pyproject.toml`; `uv` installs them on first use.

| Order | Command | Checks | Output |
|---|---|---|---|
| 1 | `uv run python3 -I code/verify_determinant.py` | Characteristic-polynomial series, Secs. 3 and 5 (eps = 1e-3 to 1e-5) | `evidence/determinant_certificate.json` |
| 2 | `uv run python3 -I code/verify_poisson.py` | Rational Poisson recursion, Secs. 3 and 5 (eps = 1e-3 to 1e-6) | `evidence/poisson_certificate.json` |
| 3 | `uv run python3 -I code/verify_scaling.py` | Scaled determinant (Thm 5.1) and two-state inequalities (Prop. 7.1) | `evidence/independent_scaling_certificate.json` |
| 4 | `uv run python3 -I code/verify_extension.py` | Lemma 4.2, Thm 4.3 leading terms, Props 6.1-6.2, Thm 6.3, feasibility table | `evidence/extension_certificate.json` |
| 5 | `uv run python3 -I code/plot_divergence.py` | Figure 2 data | `evidence/divergence.csv`, `figures/thermal_divergence.*` |
| 6 | `uv run python3 -I code/census.py 100000` | Random census, Sec. 8 (numerical evidence only; about 10 minutes) | `evidence/census.json` |

`determinant_series.py` is a library module used by step 1. Scripts 1-3 use only the
Python standard library and exact rational arithmetic. Scripts 1-5 are deterministic;
script 6 uses fixed seeds. Figure files are written without timestamps.
Tested with Python 3.11 and the versions pinned in uv.lock: numpy 2.4.6 (2.5.4 on Python 3.12+), matplotlib 3.11.2, sympy 1.14.0.
