# Agent navigation

## Identity

- Release slug: `thermal-cumulant-sign-counterexamples`. Version `1.0.0-candidate`, tag `v1.0.0-candidate`. DOI 10.5281/zenodo.23689958; concept DOI 10.5281/zenodo.23689957.
- Repository: https://github.com/ipitchford/thermal-cumulant-sign-counterexamples. Release page: https://evidencepress.org/releases/thermal-cumulant-sign-counterexamples/
- Scholarly creator: Anonymous. Status: unrefereed candidate ([STATUS.md](STATUS.md)).
- Manuscript: [PDF](thermal_cumulants.pdf) (13 pages) and its self-contained [LaTeX source](thermal_cumulants.tex).
- Machine-readable claims: [CLAIMS.json](CLAIMS.json). Human overview: [README.md](README.md).
- Assurance limits: [ASSURANCE.md](ASSURANCE.md). Review record: [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md), [REVISION_RESPONSE.md](REVISION_RESPONSE.md), [FINAL_FIXES.md](FINAL_FIXES.md).
- Prior art and sources: [evidence/literature_audit.md](evidence/literature_audit.md), [evidence/novelty_report.md](evidence/novelty_report.md), [evidence/target.yaml](evidence/target.yaml), [RESEARCH_GATES.json](RESEARCH_GATES.json), [SOURCES.md](SOURCES.md), [CITATION_AUDIT.md](CITATION_AUDIT.md). Provenance: [PROVENANCE.md](PROVENANCE.md).
- Citation: [CITATION.cff](CITATION.cff), [.zenodo.json](.zenodo.json). Licences: [LICENSES.md](LICENSES.md).

## Scientific map

The object is a finite continuous-time Markov jump process with state energies and two heat baths, with local detailed balance in each bath. The counted quantity is the heat delivered to the cold bath. C_n is the nth long-time cumulant rate: the nth derivative at zero of the tilted generator's dominant eigenvalue. The ratios are S = C3/C1 and K = C4/C2. The target is Ptaszyński 2022 (Phys. Rev. E 106, 024119), equations (19)-(20). It conjectured K >= 0, and S >= 0 for one temperature difference.

- Section 3 gives an exact three-state certificate: S < 0 for eps < 6.91e-3, and K < 0 for eps < 6.67e-2.
- Section 4 is the weak-trap mechanism. Lemma 4.2 gives the pole order. Theorem 4.3 shows both ratios tend to minus infinity like eps^-2 exactly when (3-sqrt5)/2 < U/V < 1. The limiting quadratic is the standard telegraph cumulant generating function. In Corollary 4.4, every conductor with a degenerate trap qualifies.
- Theorem 5.1 is the full-support family at fixed thermodynamic data. Its leading coefficients are -16/21609 and -16/64827.
- Section 6 says what can still be bounded. In Proposition 6.1 the normalised limits are -9/4 and -3/4, and the minimum -15/4 is attained. Proposition 6.2 makes even the normalised ratios unbounded with six states. Theorem 6.3 is a kinetic bound in terms of the spectral separation g; its ratio bounds need C1 > 0 and C2 > 0. Remark 6.4 shows that strict negativity is robust.
- Proposition 7.1: with two states there are no violations, in the standard model.
- Section 8 covers the census, why random sampling missed the violations, and the feasibility estimates.

## Evidence and replay

- Exact standard-library verifiers (they use `assert`, so do not use -O): [code/verify_determinant.py](code/verify_determinant.py), with its library [code/determinant_series.py](code/determinant_series.py), produces [evidence/determinant_certificate.json](evidence/determinant_certificate.json). [code/verify_poisson.py](code/verify_poisson.py) produces [evidence/poisson_certificate.json](evidence/poisson_certificate.json). [code/verify_scaling.py](code/verify_scaling.py) produces [evidence/independent_scaling_certificate.json](evidence/independent_scaling_certificate.json).
- SymPy and NumPy: [code/verify_extension.py](code/verify_extension.py) produces [evidence/extension_certificate.json](evidence/extension_certificate.json). [code/plot_divergence.py](code/plot_divergence.py) produces [evidence/divergence.csv](evidence/divergence.csv) and the figures. [code/census.py](code/census.py) is seeded and produces [evidence/census.json](evidence/census.json); it is numerical evidence only.
- [code/negative_controls.py](code/negative_controls.py) has 11 semantic controls. Run order: [code/README.md](code/README.md). Environment: [pyproject.toml](pyproject.toml), [uv.lock](uv.lock), [ENVIRONMENT.txt](ENVIRONMENT.txt). CI: [.github/workflows/replay.yml](.github/workflows/replay.yml). Records: [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md). Integrity: [SHA256SUMS](SHA256SUMS).

## Trust boundary

All review was internal and AI-assisted. There was no peer review, no independent reproduction and no formal verification. Priority holds only within a bounded search, and the slow-switching mechanism is prior art. Variance-based bounds such as the thermodynamic uncertainty relation are not contradicted. The census and feasibility numbers are numerical evidence only.
