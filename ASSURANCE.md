# Assurance boundary

## What was done

1. **Written proofs** in [thermal_cumulants.tex](thermal_cumulants.tex). The load-bearing identities are certified by three separately written exact verifiers: [verify_determinant.py](code/verify_determinant.py), [verify_poisson.py](code/verify_poisson.py) and [verify_scaling.py](code/verify_scaling.py). These use only the standard library and rational arithmetic. A fourth verifier, [verify_extension.py](code/verify_extension.py), uses SymPy and NumPy for the Section 6 results and the feasibility table.
2. **Internal AI-assisted review.** The first round had an editor and methodology, domain, perspective and devil's-advocate reviewers, plus an outside-model correctness audit. Each finding has a disposition in [REVISION_RESPONSE.md](REVISION_RESPONSE.md). The revision then had a verification re-review, a targeted proof audit (exact checks with its own full-counting-statistics code) and a final outside-model correctness audit. The final audit found that Theorem 6.3 was false as stated without C1 > 0. That, and the other repairable gaps it and the proof audit found, were fixed in [FINAL_FIXES.md](FINAL_FIXES.md), without a further review round. [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md) is a rating-free summary.
3. **Replay.** All six scripts were rerun from a clean copy (27 October 2026), and every output was byte-identical to the shipped files, including the 10^5-sample census ([REPLAY_RECEIPT.md](REPLAY_RECEIPT.md)). CI replays the exact checks on Linux. [negative_controls.py](code/negative_controls.py) runs 11 semantic controls, and each corrupted claim or input must be rejected.
4. **Citations.** All 16 DOIs resolve at doi.org, and each matches its Crossref record by title, first author and year ([CITATION_AUDIT.md](CITATION_AUDIT.md)). The hypotheses of the conjectures were compared with the source text (Table 1 of the paper).

## What was not done

- There was no human specialist review or journal peer review, no independent reproduction by an unaffiliated party, and no proof-assistant formalisation.
- **Priority is bounded.** The search was dated 20 October 2026 ([evidence/literature_audit.md](evidence/literature_audit.md), [evidence/novelty_report.md](evidence/novelty_report.md)), with no exhaustive citation-index search and no author enquiry. The slow-switching mechanism and the telegraph cumulant formulas are prior art (Jordan-Sukhorukov 2004; Bagrets-Nazarov 2003). The contribution is their exact realisation inside the conjectured class, the fixed-thermodynamic-data strengthening, and the account of what can still be bounded.
- The development records under `evidence/` predate the final review. Where they say "independent", they mean a separate internal AI-assisted check, not external review. They also refer to some development files that are not shipped.
- The kinetic bound's constants are loose (about 10^4 in the full family).

Agreement between AI reviewers is not independent evidence.
