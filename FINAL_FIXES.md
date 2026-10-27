# Final editor fixes (27 October 2026)

These changes were made after the verification re-review, the targeted proof audit and a final outside-model correctness audit. No further review round followed. Each change is listed with its reason. Version 2.0 of the manuscript was the input.

## Mathematics

1. **Theorem 6.3 (kinetic bound).** The cumulant estimate |C_n| <= n! (g/2)(E_max/ell)^n is now stated on its own. The ratio bounds are conditional: if C_1 > 0 then S >= -(3g/C_1)(E_max/ell)^3, and if C_2 > 0 then K >= -(12g/C_2)(E_max/ell)^4. For any C_1 != 0 the bound |S| <= (3g/|C_1|)(E_max/ell)^3 is given. Reason: the proof divided by C_1 and C_2 without assuming their sign. The final audit gave a trap-family example with reversed temperature ordering in which C_1 < 0 while S tends to minus infinity, so the unconditional statement was false.
2. **Theorem 6.3, other hypotheses.** Irreducibility of L(0), so that 0 is simple, is now assumed explicitly, together with A > 0 and E_max > 0 (otherwise every C_n vanishes).
3. **Theorem 6.3, terminology.** g is now called the *spectral separation* of the zero eigenvalue. The text says it equals the usual spectral gap for reversible chains, and that in general g >= min(-Re lambda) and g need not be the relaxation rate. The "relaxation time of order sqrt(X)" interpretation is restricted to reversible chains with A, C_1 and E_max uniformly controlled. For nonreversible chains it concerns g and also depends on kappa.
4. **Theorem 6.3, novelty.** The proof now says it combines standard Bauer-Fike, Riesz-projection and Cauchy estimates. It also says that analyticity-radius bounds for Markov additive functionals are classical, and that the contribution is only their explicit specialisation to these ratios.
5. **Remark 6.4 (robustness).** It now states that each C_n is continuous (indeed rational) on the open set of irreducible prefactors, that S is continuous where C_1 != 0 and that K is continuous where C_2 != 0. The persistence of a strict S < 0 or K < 0 follows because S < 0 forces C_1 != 0 and K < 0 forces C_2 != 0.
6. **Proposition 6.1.** It now notes that -15/4 is attained in the epsilon -> 0 limit at r = 3/2, for example by (a,b,c,d,alpha,beta,E) = (1,2,1,4,8,9,1).
7. **Proposition 6.2.** A paragraph after the proof now says three things. First, the result is an amplification of Theorem 5.1 by closure under independent products, not a new mechanism. Second, the asymptotics set in late. In exact computation K-hat first becomes negative near epsilon = 1e-2 and S-hat only below about 2e-3, so both ratios are negative only for epsilon of about 1e-3 or less. Third, multiplying the whole product generator by epsilon leaves both ratios unchanged and keeps every rate bounded. The sign-change points were computed with exact rational arithmetic on the 6-state tilted generator, at epsilon = 0.3, 0.1, 0.03, 0.01, 0.003, 0.001 and below. At 3e-3, S-hat = +0.032 and K-hat = -0.37. At 1e-3, S-hat = -0.11 and K-hat = -1.65.
8. **Theorem 4.3, prior art.** The proof now says at the point of use that the limiting quadratic (11) is the standard two-state telegraph cumulant generating function [Jordan-Sukhorukov 2004; Bagrets-Nazarov 2003]. What is specific here is its realisation in the two-bath local-detailed-balance class.

## Wording and statistics (re-review NEW-1 to NEW-7)

9. **Abstract, two states (NEW-3).** The sentence now reads "In the standard state-jump model with one counted bath, two states can never violate either sign." The Section 7 title is now "Two states never suffice in the standard model".
10. **Abstract, rate separation (NEW-4).** "about 10^2 or more" became "of order 10^2 (a disparity above 60 suffices in the simplest example)".
11. **Abstract, kinetic bound.** It now says "for positive mean and variance" and "spectral separation of the stationary eigenvalue", in line with items 1 and 3.
12. **Section 8, hertz switching (NEW-2).** The text now says kilohertz switching (epsilon >= 1e-3) needs records of order 1e6 fast-rate times. Record length grows roughly like 1/epsilon, so hertz switching (epsilon ~ 1e-6) would need about 1e9.
13. **Table 2 caption (NEW-5).** The caption now says that source-scheme fractions use all 1e5 samples as the denominator, including the 34% skipped as ill-conditioned.
14. **Table 1 header and Section 8 (NEW-6).** The header now cites "Sec. III (stated) and III D (setting)". The text no longer says the source sampled "uniformly". It says the source does not name the distribution and that our replication samples uniformly.
15. **code/README.md (NEW-1).** The tested versions now match uv.lock: numpy 2.4.6 (2.5.4 on Python 3.12+), matplotlib 3.11.2 and sympy 1.14.0.
16. **REVISION_RESPONSE.md item 32 (NEW-7).** This is reworded so that it no longer mentions ratings.

## Additions to the package

17. `code/negative_controls.py` adds 11 semantic negative controls. Each corrupts one claim or input in an exact verifier, and the verifier must then fail. The script refuses to run under `python -O`.

## Rebuild and checks

- The PDF was rebuilt with latexmk (pdfTeX). It has 13 pages, no undefined references and no overfull boxes. Every page was rendered and inspected.
- All six scripts were rerun in README order from a clean copy containing only `code/`, `pyproject.toml` and `uv.lock`, wrapped in the shared research queue. The census took about 10 minutes. Outputs were compared byte for byte with the shipped evidence; see REPLAY_RECEIPT.md.
- The negative controls passed: the 4 baselines passed and all 11 corruptions were rejected.

Theorems 4.3 and 5.1, Propositions 6.1, 6.2 and 7.1 and Lemma 4.2 are mathematically unchanged. The changed text is in Theorem 6.3, Remark 6.4, the notes after Propositions 6.1 and 6.2, and the wording items above.
