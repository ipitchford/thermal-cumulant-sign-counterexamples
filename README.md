# Thermal heat-current cumulant ratios can be arbitrarily negative: three-state counterexamples to two sign conjectures

**Unrefereed research candidate**, version 1.0.0-candidate (27 October 2026). DOI [10.5281/zenodo.23689958](https://doi.org/10.5281/zenodo.23689958); concept DOI 10.5281/zenodo.23689957. Release page: https://evidencepress.org/releases/thermal-cumulant-sign-counterexamples/

Creator: Anonymous. Text and data CC0-1.0; code MIT ([LICENSES.md](LICENSES.md)).

## In one paragraph

Ptaszyński (Phys. Rev. E 106, 024119, 2022) conjectured, from random-network calculations, that the long-time heat-current cumulant ratios C3/C1 and C4/C2 are never negative in classical Markov systems driven only by temperature differences (his equations (19)-(20)). A negative ratio would then have certified non-thermal or quantum driving. This package gives exact three-state, two-bath counterexamples that obey local detailed balance. In a fully connected family the energies, temperatures, stationary law, mean heat current and entropy production are held fixed while both ratios tend to minus infinity like eps^-2. The mechanism is classical slow switching (telegraph statistics). The divergence tracks the variance. The variance-normalised ratios stay finite in the trap family (limits -9/4 and -3/4), and **variance-based bounds such as the thermodynamic uncertainty relation are untouched**. With six states, even the normalised ratios are unbounded below. A kinetic bound, stated for C1 > 0 and C2 > 0 in terms of the spectral separation of the stationary eigenvalue, captures the eps^-2 rate. In the standard state-jump model with one counted bath, two states never violate either sign.

## Where to start

- Manuscript: [thermal_cumulants.pdf](thermal_cumulants.pdf) (13 pages) and its [LaTeX source](thermal_cumulants.tex).
- Claims: [CLAIMS.json](CLAIMS.json). Status: [STATUS.md](STATUS.md). Assurance limits: [ASSURANCE.md](ASSURANCE.md). Agent guide: [AI_INDEX.md](AI_INDEX.md).
- Review record without scores: [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md), [REVISION_RESPONSE.md](REVISION_RESPONSE.md), [FINAL_FIXES.md](FINAL_FIXES.md).
- Code and replay: [code/README.md](code/README.md), [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md), [ENVIRONMENT.txt](ENVIRONMENT.txt).

## Replay

From the package root, with [uv](https://docs.astral.sh/uv/) installed:

```sh
uv run --frozen python3 -I code/verify_determinant.py
uv run --frozen python3 -I code/verify_poisson.py
uv run --frozen python3 -I code/verify_scaling.py
uv run --frozen python3 -I code/verify_extension.py
uv run --frozen python3 -I code/plot_divergence.py
uv run --frozen python3 -I code/census.py 100000      # about 10 minutes
uv run --frozen python3 -B -I code/negative_controls.py
sha256sum -c SHA256SUMS
```

The scripts rewrite `evidence/` and `figures/` in place, so run them in a copy and compare the outputs with the shipped files. Do not use `python -O`: the exact checks are `assert` statements.

## Cite

Anonymous (2026). *Thermal heat-current cumulant ratios can be arbitrarily negative: three-state counterexamples to two sign conjectures*. Evidence Press research candidate, version 1.0.0-candidate. https://doi.org/10.5281/zenodo.23689958
