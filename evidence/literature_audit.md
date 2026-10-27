# Thermal cumulant conjectures: bounded formula-level novelty audit

Date: 20 October 2026. This is an audit record, not a proof of priority. The mathematical verification is in `theorems_and_proofs.md`, `verify_full_family.py` and `full_family_verification.json`.

## Target and current decision

Proceed with the precise contribution: a complete three-state, two-bath, local-detailed-balance family refuting the nonnegativity conjectures for long-time heat-current ratios C3/C1 and C4/C2, with both ratios tending to minus infinity while the energies, bath temperatures, stationary law, positive mean heat current and positive entropy-production rate are fixed. A self-contained two-state calculation establishes minimality. The slow-switching mechanism and its cumulant formulas are established prior art and must be acknowledged.

No prior resolution of the exact thermal conjectures was found in the bounded searches below. This does not establish that the conjectures remained unresolved in all unpublished, non-indexed or newly published work as of the audit date. No author enquiry or exhaustive citation-index search was performed.

## Object identity and fingerprints

The object is a finite irreducible continuous-time Markov chain, bath-labelled transitions, fixed state energies, positive bath temperatures, and local detailed balance separately in each bath. The counted current is heat delivered to one bath. Cn is the nth derivative at zero of the dominant tilted-generator eigenvalue, so C4 is a cumulant and is not an ordinary fourth central moment. Taking the long-time limit first is essential; each epsilon>0 model is irreducible.

The first exact cubic fingerprint is

x^3+(8+2 epsilon)x^2+14 epsilon x-[4(exp(z)-1)+2(exp(-z)-1)](x+epsilon).

The general trap fingerprint is

x^3+[w+epsilon(alpha+beta)]x^2+epsilon(beta w+alpha v)x-(x+epsilon beta)[p(exp(Ez)-1)+q(exp(-Ez)-1)].

The slow-switching sign fingerprints are (U-V) for C3 and U^2-3UV+V^2 for C4, with U=alpha v and V=beta w. In active-occupancy coordinates P=V/(U+V), the latter has the known telegraph factor 1-5P+5P^2. These are structural matches to bistable-current counting statistics, not new probability identities.

The full-support family has limiting characteristic equation y^2+(28-8k/9)y-160k/9=0. Its asymptotic ratio coefficients are -16/21609 and -16/64827. All bath graphs are complete and all levels distinct; the fixed stationary law is (40,5,18)/63 and the common rate normalization fixes C1=40/63.

## Primary-paper comparison ledger

| Primary source, inspected portion | Exact overlap or distinction | Effect on novelty assessment |
|---|---|---|
| K. Ptaszynski, *Bounds on skewness and kurtosis of steady-state currents*, PRE 106, 024119 (2022), DOI 10.1103/PhysRevE.106.024119; https://arxiv.org/pdf/2204.08421, v4. Definitions, Section III D, Section III E and appendix inspected. | Equations (19) and (20) are precisely the thermal targets. Section III D uses bath-wise detailed balance and reports broad random-network checks. Section III E Eq. (76) gives the winding-current skewness lower bound whose N=2 value is 1/4. | Exact target match. The two-state 1/4 skewness inequality is not advertised as new; the proof is auxiliary to minimality. The new claim is the fixed-thermodynamics counterexample/divergence construction, not a general invention of negative current cumulants. |
| A. N. Jordan and E. V. Sukhorukov, *Transport Statistics of Bistable Systems*, PRL 93, 260604 (2004), DOI 10.1103/PhysRevLett.93.260604; https://arxiv.org/pdf/cond-mat/0406261. Full four-page paper inspected, especially Eqs. (12)–(15). | General telegraph-process counting statistics; switching between two current levels produces large higher cumulants, and the third-cumulant sign depends on switching asymmetry. The effective quadratic eigenvalue equation is the same structure as the limiting equation here. | Direct mechanism collision. Cite prominently. It does not supply the present explicit thermal-detailed-balance family or settle the later thermal conjectures in the inspected text. |
| D. S. P. Salazar, *Thermodynamic Skewness Relation From Detailed Fluctuation Theorem*, PRE 106, L042101 (2022), DOI 10.1103/PhysRevE.106.L042101; https://arxiv.org/pdf/2208.11206. Full paper and worked example inspected. | Negative skewness is permitted under a strong detailed fluctuation theorem, with a finite-time heat-exchange example using a qubit swap engine. It treats standardized skewness of an entropy-production distribution. | Reject any broad 'negative thermal skewness is new/impossible before this' assertion. Different observable normalization and finite-time/engine setting; not the same autonomous classical long-time conjecture. |
| K. Ptaszynski and M. Esposito, *Critical heat current fluctuations in Curie-Weiss model in and out of equilibrium*, PRE 111, 034125 (2025), DOI 10.1103/PhysRevE.111.034125; https://arxiv.org/pdf/2411.19643, v3. Full manuscript inspected and cumulant/switching passages searched. | A two-bath thermal model with intermittent switching, divergent noise, an effective two-state description, and equilibrium fourth-cumulant analysis. This is particularly close physical prior art and cites the 2022 paper. | The thermal switching mechanism itself is already recognized. No resolution of the negative-skewness/kurtosis conjectures was found in the inspected text. The present theorem's fixed three-state, fixed-law, fixed-current negative divergence remains distinct on this audit. |
| M. Gerry and D. Segal, *Full counting statistics and coherences: fluctuation symmetry in heat transport with the Unified quantum master equation* (2023), https://arxiv.org/pdf/2212.11307. Full manuscript searched for higher cumulants and thermal-state structure. | Quantum coherent V-system and thermal fluctuation symmetry. | No direct classical Markov counterexample found. Its existence is a reminder to separate coherent thermal models from the source conjecture's classical class. |
| M. Wampler and A. C. Barato, *Skewness and Kurtosis in Stochastic Thermodynamics*, J. Phys. A 55, 014002 (2022), DOI 10.1088/1751-8121/ac3b0c; https://arxiv.org/pdf/2110.14540. Definitions, bounds and limiting examples inspected. | First-passage-time cumulants, rather than fixed-time current cumulants. | Same keywords, different mathematical object; no direct theorem collision. |

## Search ledger

Both available web search engines were used. Queries were issued in multiple batches, with primary PDFs opened after relevant hits. Some heavily quoted searches produced no relevant exact result or only generic keyword expansion; these absences are weak evidence.

- `"Ptaszynski" "heat" "kurtosis" counterexample`
- `"thermally driven" "negative" "skewness" Markov`
- `"2204.08421" counterexample`
- `"kurtosis" "thermal" "dynamical channel blockade"`
- `"negative skewness" "heat current" classical`
- `"negative kurtosis" "heat" Markov`
- `"heat current" "telegraph" cumulants`
- `"Bounds on skewness and kurtosis of steady-state currents" correction`
- `"thermal" "kurtosis" "blockade" -site:researchgate.net`
- `"heat" "third cumulant" "negative" "Markov"`
- `"heat" "fourth cumulant" "negative" classical`
- `"Critical heat current fluctuations in Curie-Weiss model"`
- `Sukhorukov Jordan stochastic switching full counting statistics third cumulant bistable systems`
- `heat current fluctuations intermittent thermal transport three level system cumulants`
- `thermal transport dark state third fourth cumulant negative`
- `"heat" "cumulants" "telegraph noise"`
- `"heat current" "cumulants" "negative" "Ptaszynski"`
- `"heat current" "skewness" "kurtosis" "trap"`
- `"telegraph" "fourth cumulant" "negative"`
- `"heat current" "negative skewness"`
- `"heat current" "negative kurtosis"`
- `"telegraph" "fourth cumulant"`

## Claims to exclude or qualify

1. Do not claim discovery of negative higher cumulants, telegraph-current full counting statistics, or the general slow-switching divergence mechanism.
2. Do not claim the two-state skewness inequality as an independent new result. Its role is to make the minimum state count explicit and self-contained. The kurtosis calculation likewise should be presented as auxiliary, not as a literature-priority claim.
3. Do not say there can be no lower bound at all. The theorem excludes finite lower bounds determined only by the listed quantities held fixed. A mixing-time, spectral-gap or minimal kinetic-rate condition can exclude the construction.
4. Do not confuse aggregate detailed balance with equilibrium of the bath-resolved thermodynamic process. The aggregate generator is reversible, but opposed bath currents produce strictly positive entropy.
5. Distinguish an exact analytic refutation of the stated inequalities from a novelty claim about all literature. The former is proved and independently reproduced; the latter remains bounded-search evidence.

## Remaining uncertainty

The strongest unresolved risk is an earlier or recent thermal gated-conductor example in which negative C3/C1 or C4/C2 is implicit in printed formulas but not described by searchable keywords. The explicit published 2022 conjectures and the lack of a located correction make a targeted contribution plausible, but do not eliminate this risk. The manuscript should acknowledge the close telegraph/Curie–Weiss antecedents and frame the core novelty as the exact fixed-thermodynamics resolution.
