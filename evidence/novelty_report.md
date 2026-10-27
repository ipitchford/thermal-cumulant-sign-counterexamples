# Novelty-gate report: thermal heat-current cumulant counterexamples

**Search date:** 20 October 2026.  
**Researcher/agent:** Research team; final consolidation and formula mapping by `control_scout`.  
**Corpus boundary:** The bounded live-search corpus recorded in `literature_audit.md`, the inspected primary papers identified below, and the exact project certificates. Both available web search engines were used during scouting. This final consolidation reopened selected papers already in that corpus; it issued no new search queries. No exhaustive citation-index search or author enquiry was performed.  
**Intended contribution unit:** An exact counterexample to two specified thermal sign conjectures, strengthened to simultaneous unbounded negative ratios at fixed thermodynamic data; an auxiliary minimum-state-count proof; and reproducible exact verification. Historical priority is a separate question.  
**Inputs:** `target.yaml`, `literature_audit.md`, `independent_proof_audit.md`, `poisson_certificate.json`, the final `thermal_cumulants.tex`, and the determinant/scaling verification code.

## 1. Frozen claim

### Exact statement

There is a one-parameter family, indexed by every sufficiently small positive \(\varepsilon\), of finite, irreducible, autonomous classical continuous-time Markov jump processes with three states, two positive-temperature baths, and bathwise local detailed balance, such that:

- the energies are the fixed distinct values \((0,2,1)\);
- the inverse bath temperatures are \(\beta_h=\log2\), \(\beta_c=\log4\);
- every directed transition between distinct states has a strictly positive rate through each bath;
- the stationary distribution is \((40,5,18)/63\);
- the mean heat current delivered to the cold bath is \(C_1=40/63\), and the entropy-production rate is \(40\log2/63\);
- the long-time cumulant ratios satisfy

\[
\frac{C_3}{C_1}=-\frac{16}{21609\varepsilon^2}+O(\varepsilon^{-1}),
\qquad
\frac{C_4}{C_2}=-\frac{16}{64827\varepsilon^2}+O(\varepsilon^{-1}).
\]

Thus both ratios have infimum minus infinity even with all the listed thermodynamic quantities fixed. Two-state heat-jump models cannot have either negative ratio where it is defined. Three states are therefore minimal in this model class.

The direct target is Ptaszyński (2022), equations (19) and (20), under the definitions and thermal assumptions in Section III D. The finite rational certificate already refutes those inequalities; the fixed-invariant family is a stronger result.

### Exclusions

The claim does not concern finite-time standardised skewness, the fourth central moment, first-passage-time cumulants, time-dependent engines, chemical or voltage driving, or a quantum coherent component. The limit is \(t\to\infty\) first, at each fixed \(\varepsilon>0\), followed by \(\varepsilon\downarrow0\). The reducible chain at \(\varepsilon=0\) is not itself a counterexample.

No novelty is claimed for telegraph switching, negative higher cumulants in general, tilted-generator differentiation, or elementary two-state current formulas. No conclusion excludes lower bounds that additionally control a mixing rate, spectral gap or minimum transition rate. State-count minimality excludes heat-carrying self-transitions and effective states with an independent ongoing current reward.

### Permitted claim language before the gate

“The displayed rates and exact cumulants give a counterexample to the stated inequalities.” This is a verifiable mathematical statement. “No equivalent thermal resolution was found in the bounded search recorded here” is the permitted historical statement. Neither sentence asserts that this is the first counterexample ever known or that the entire literature has been exhausted.

## 2. Normalisation and translation table

| Original notation or object | Canonical notation used here | Transformation checked |
|---|---|---|
| Source rate \(k_{ij}^{\alpha}\), transition from \(j\) to \(i\) | Column generator \(L\) | No transpose is needed; columns of \(L(0)\) sum to zero. |
| Source scaled current cumulants \(\langle\!\langle j^n\rangle\!\rangle\) | \(C_n=\chi^{(n)}(0)\) | Both use the long-time cumulant per unit time, not a finite-time standardised statistic. |
| Source thermal ratios \(S^h,K^h\) | \(S=C_3/C_1\), \(K=C_4/C_2\) | Same denominators and cumulant order; both have units of energy squared. |
| Bathwise detailed balance | \(k_{ij}^{\alpha}/k_{ji}^{\alpha}=e^{-\beta_\alpha(E_i-E_j)}\) | Checked on every bath-labelled edge of both explicit families. |
| Heat delivered to the cold bath | Jump increment \(E_j-E_i\) | Off-diagonal cold rates receive \(e^{z(E_j-E_i)}\); escape rates remain untilted. |
| Current reversal | \(C_n\mapsto(-1)^n C_n\) | Both ratios are unchanged, so a sign convention cannot remove the violations. |
| Common positive rate scaling | \(L\mapsto\lambda L\), \(C_n\mapsto\lambda C_n\) | Both ratios and the stationary distribution are unchanged. This fixes the mean current in the full family. |
| Reversibility of the summed generator | Pairwise balance for \(\sum_\alpha k_{ij}^{\alpha}\) | Does not cancel opposed bath-labelled heat currents; entropy production remains positive. |
| Fourier counting field used in some transport papers | Real moment field \(z\) | Set the Fourier variable times \(i\) equal to \(z\); differentiate with respect to the corresponding real moment variable. |
| Effective conducting/inactive states | Two-state occupation-time reward process | This is a coarse-grained description of a three-state thermal chain, not a literal two-energy-state heat-jump counterexample. |

The assumption-by-assumption match to the source is recorded in Section 6.1. The simple family uses state order \((0,1,2)\) with energies \((0,1,0)\); the stronger family keeps that state order but has energies \((0,2,1)\). “Up” in its rate table means increasing energy, not increasing state label.

## 3. Fingerprints

### Sequences

For the sparse exact family, the four cumulants are

\[
C_1=\frac17,\quad
C_2=\frac{6+145\varepsilon}{343\varepsilon},\quad
C_3=\frac{1531\varepsilon^2+2595\varepsilon-18}{16807\varepsilon^2},
\]

\[
C_4=\frac{214549\varepsilon^3+402264\varepsilon^2-15924\varepsilon-792}
{823543\varepsilon^3}.
\]

The natural denominator powers are \(7,7^3,7^5,7^7\). The numerator coefficient vectors, in increasing powers of \(\varepsilon\), are \((6,145)\), \((-18,2595,1531)\), and \((-792,-15924,402264,214549)\). Three exact finite instances are:

| \(\varepsilon\) | \(C_1\) | \(C_2\) | \(C_3\) | \(C_4\) |
|---|---:|---:|---:|---:|
| \(1/100\) | \(1/7\) | \(745/343\) | \(81031/16807\) | \(-910799051/823543\) |
| \(1/1000\) | \(1/7\) | \(6145/343\) | \(-15403469/16807\) | \(-807521521451/823543\) |
| \(1/10000\) | \(1/7\) | \(60145/343\) | \(-1774048469/16807\) | \(-793588377145451/823543\) |

For the stronger family's limiting analytic root \(y(k)=\sum_{n\ge1}a_nk^n\), the first ten ordinary Taylor coefficients, generated from the exact recurrence below, are:

| \(n\) | \(a_n\) |
|---:|---:|
| 1 | \(40/63\) |
| 2 | \(160/27783\) |
| 3 | \(-320/4084101\) |
| 4 | \(-640/5403265623\) |
| 5 | \(1280/37822859361\) |
| 6 | \(-94720/150118928803809\) |
| 7 | \(-926720/154472377739119461\) |
| 8 | \(108328960/204366955748855046903\) |
| 9 | \(-240005120/30041942495081691894741\) |
| 10 | \(-7518576640/39745489920993078376742343\) |

The cumulant derivatives are \(n!a_n\), not \(a_n\). The first four derivatives are \(40/63,320/27783,-640/1361367,-5120/1801088541\). The transformed ratio fingerprints are \(\varepsilon^2S\to-16/21609\) and \(\varepsilon^2K\to-16/64827\).

**Search status:** These are recorded reproducible fingerprints. The search ledger does not establish that the ten-term rational sequence, its integer transforms or its reciprocals were submitted to OEIS or a literal full-text engine. They must not be presented as negative sequence-search evidence.

### Generating functions

The sparse-family scaled cumulant generating function is the analytic root through \(x=z=0\) of

\[
F(x,z)=x^3+(8+2\varepsilon)x^2+14\varepsilon x
-[4(e^z-1)+2(e^{-z}-1)](x+\varepsilon)=0.
\]

With \(t=e^z\), an equivalent primitive polynomial near \(t=1\) is

\[
t x^3+(8+2\varepsilon)t x^2+14\varepsilon t x
-2(2t-1)(t-1)(x+\varepsilon)=0.
\]

The general trap polynomial is

\[
x^3+[w+\varepsilon(\alpha+\beta)]x^2
+\varepsilon(\beta w+\alpha v)x
-(x+\varepsilon\beta)[p(e^{Ez}-1)+q(e^{-Ez}-1)].
\]

Here \(u=a+c\), \(v=b+d\), \(w=u+v\), \(p=ad\), \(q=bc\). The leading singular-limit fingerprint of the full-support family is the primitive quadratic

\[
9y^2+(252-8k)y-160k=0,\qquad y(0)=0.
\]

Its explicit square-root solution is

\[
y(k)=\frac{(8/9)k-28+\sqrt{((8/9)k+12)^2+640}}2.
\]

This normal form has a verified collision with the classical telegraph generator, not merely a similar title; see Section 6.2.

### Small matrices/kernels

At \(\varepsilon=1/q\), the untilted sparse generator has the integer-scaled form

\[
qL(0)=
\begin{pmatrix}
-2q-1&6q&1\\
2q&-6q&0\\
1&0&-1
\end{pmatrix},\qquad q=100,1000,10000.
\]

Each is a three-by-three rank-two Metzler generator with determinant zero, trace \(-8-2/q\) before scaling, stationary vector \((3,1,3)/7\), column sums zero and a missing \(1\leftrightarrow2\) edge. Its characteristic polynomial is

\[
x[x^2+(8+2/q)x+14/q],
\]

with eigenvalues \(0\) and \(-4-1/q\pm\sqrt{16-6/q+1/q^2}\). The stronger family's explicit three-by-three tilted matrix and all twelve positive bath-labelled rates are in the manuscript; the certificates verify its stationary distribution and cumulants at four exact couplings.

The finite matrices were checked algebraically. No graph-isomorphism database search or permutation/transpose hash search is recorded, and none is implied.

### Invariants and recurrences

The general leading sign factors are \(U-V\) and \(U^2-3UV+V^2\), where \(U=\alpha v\), \(V=\beta w\). With active occupancy \(P=V/(U+V)\), they become the familiar switching factors \(1-2P\) and \(1-5P+5P^2\), up to positive powers of \(U+V\).

The limiting-root recurrence is

\[
a_1=40/63,\qquad
a_n=\frac{(8/9)a_{n-1}-\sum_{j=1}^{n-1}a_ja_{n-j}}{28}\quad(n\ge2).
\]

Other checked invariants are local detailed balance, current-reversal invariance of both ratios, invariance under common rate scaling, the fixed stationary law, positive fixed entropy production, and the simple family's fluctuation symmetry under \(z\mapsto-\log2-z\). Exact determinant and independent Poisson recursions agree. The algebra is evidence for correctness, not for historical priority.

## 4. Alias map

| Analysis | Probability | Combinatorics | Mathematical physics | Other |
|---|---|---|---|---|
| Singular perturbation of a tilted eigenvalue | Markov additive process; Markov-modulated current | Cycle-cover expansion of a determinant | Full counting statistics; tilted master operator | Heat-current cumulant ratios |
| Two-scale elimination; effective two-dimensional generator | Telegraph process; conducting/inactive switching | Excursion and alternating-renewal descriptions | Bistable transport; dynamical channel blockade; dark-state transport | Gated conductor |
| Algebraic square-root generating function | Integrated occupation time; Markov reward process | Coefficient recurrence with quadratic convolution | Feynman–Kac operator; non-Hermitian transfer matrix | Cumulant-based statistical diagnostics |
| Spectral derivatives; analytic implicit function theorem | Stationary additive-functional cumulants | Closed-walk and cycle-current counts | Thermal detailed balance; fluctuation symmetry | Kinetic restrictions versus thermodynamic invariants |

The probability and transport aliases were actually searched through the queries below. The combinatorial, special-function and representation-theoretic descriptions are **candidate aliases**, not evidence of searches in those literatures. No named orthogonal-polynomial family, group representation or association scheme was identified. The elementary square-root normal form led to a concrete telegraph collision, making a claim of a new general generating function untenable.

## 5. Search log

All rows below are dated **20 October 2026**. Exact query strings are preserved from the existing team ledger. That ledger records use of both search engines but does not preserve which engine returned each individual hit. Results were screened and the primary texts listed in Section 6 were inspected; the table does not assert that every query produced a distinct source.

| Date | Corpus/database | Exact query or query family actually recorded | Results inspected | Consequence |
|---|---|---|---|---|
| 2026-10-20 | Both available web engines; arXiv/publisher full texts | `"Ptaszynski" "heat" "kurtosis" counterexample`; `"2204.08421" counterexample`; `"Bounds on skewness and kurtosis of steady-state currents" correction` | Ptaszyński 2022 and nearby primary literature | Located the exact target; no correction or equivalent resolution was identified in this bounded corpus. |
| 2026-10-20 | Same | `"thermally driven" "negative" "skewness" Markov`; `"negative skewness" "heat current" classical`; `"negative kurtosis" "heat" Markov` | Thermal higher-cumulant and fluctuation-relation papers | Separated long-time classical currents from finite-time and quantum objects. |
| 2026-10-20 | Same | `"heat" "third cumulant" "negative" "Markov"`; `"heat" "fourth cumulant" "negative" classical`; `"heat current" "negative skewness"`; `"heat current" "negative kurtosis"` | Ptaszyński 2022; Salazar 2022 and related screened results | Broad negative-cumulant novelty was rejected. |
| 2026-10-20 | Same | `"kurtosis" "thermal" "dynamical channel blockade"`; `"thermal" "kurtosis" "blockade" -site:researchgate.net`; `thermal transport dark state third fourth cumulant negative` | Classical/quantum transport papers and the source's blockade discussion | Identified the risk of formulas hidden under transport terminology; no equivalent fixed-invariant thermal construction was located. |
| 2026-10-20 | Same | `"heat current" "telegraph" cumulants`; `"heat" "cumulants" "telegraph noise"`; `"telegraph" "fourth cumulant" "negative"`; `"telegraph" "fourth cumulant"` | Jordan–Sukhorukov 2004 | Verified a direct normal-form and mechanism collision. |
| 2026-10-20 | Same | `Sukhorukov Jordan stochastic switching full counting statistics third cumulant bistable systems`; `heat current fluctuations intermittent thermal transport three level system cumulants` | Jordan–Sukhorukov and thermal-switching literature | Cross-disciplinary comparison was performed beyond the source's direct citation neighbourhood. |
| 2026-10-20 | Same | `"Critical heat current fluctuations in Curie-Weiss model"`; `"heat current" "cumulants" "negative" "Ptaszynski"`; `"heat current" "skewness" "kurtosis" "trap"` | Ptaszyński–Esposito 2025 | Thermal switching is prior art; the particular fixed-three-state negative-ratio theorem was not found in the inspected text. |
| 2026-10-20 | Direct inspection of existing corpus, no new search | Saryal et al. 2019, Section II; source references; selected full-text passages | Affinity expansion and thermodynamic uncertainty relation | The equilibrium expansion is a different limiting statement. |
| 2026-10-20 | Direct reinspection during consolidation | Known URLs for Ptaszyński 2022, Jordan–Sukhorukov 2004, Ptaszyński–Esposito 2025 and Saryal et al. 2019 | Equations and sections identified below | Confirmed exact formula mappings and source scope; no additional search coverage claimed. |

**Not recorded as executed:** literal searches for the full cubic coefficient vector, the ten-term rational Taylor sequence, all variable permutations of the primitive quadratic, OEIS queries, systematic graph-database queries, exhaustive citing-paper retrieval, or author correspondence. Formula-level comparison was performed against the primary papers found through the recorded searches; it was not an exhaustive formula-index search.

## 6. Verified collisions or bridges

### 6.1 Exact target: Ptaszyński 2022

Primary source: [*Bounds on skewness and kurtosis of steady-state currents*](https://arxiv.org/pdf/2204.08421), [Physical Review E 106, 024119](https://doi.org/10.1103/PhysRevE.106.024119). Inspected locations: definitions (3)–(4), (8)–(10); thermal model (63)–(70); conjectures (19)–(20); two-state specialisation of (76).

| Source condition | Verified realisation |
|---|---|
| Finite classical Markov dynamics, (63)–(65) | Three-state irreducible column generator for every positive coupling. |
| Bath-resolved detailed balance, (66) | Each bath's up/down rate ratio is the required Boltzmann factor. |
| Heat-to-bath tilt, (67) | The same off-diagonal heat increments and unchanged escape rates. |
| Long-time scaled cumulants, (8)–(10), (68)–(70) | Derivatives of the simple eigenvalue through zero. |
| Thermal driving only, (19) | Fixed energies and two temperatures; no other drive. |
| One temperature difference, (20) | Exactly two baths. |

**Assessment:** The constructed model is inside the conjectured class. Its negative ratios refute the specified statements independently of any priority judgement. Random-sampling ranges reported in the source are not additional hypotheses of the conjectures.

### 6.2 COLLISION: Jordan–Sukhorukov telegraph normal form

Primary source: [*Transport statistics of bistable systems*](https://arxiv.org/pdf/cond-mat/0406261), [Physical Review Letters 93, 260604](https://doi.org/10.1103/PhysRevLett.93.260604). Equations (11)–(12) give a two-state tilted matrix and its dominant eigenvalue; the subsequent discussion gives switching contributions to higher cumulants.

Our explicit translation is

\[
H_1(k)=\frac89k,\quad H_2(k)=0,\quad\Gamma_1=8,\quad\Gamma_2=20.
\]

Their matrix becomes

\[
\begin{pmatrix}(8/9)k-8&20\\8&-20\end{pmatrix}.
\]

Directly taking its determinant gives

\[
y^2+(28-(8/9)k)y-(160/9)k,
\]

exactly our limiting polynomial. Therefore the leading effective generating function and its switching cumulants are known objects. An analytic derivation of those coefficients cannot support a novelty claim by itself.

The unverified priority question concerns the microscopic thermal realisation with all invariants fixed. The inspected paper does not provide that specific rate family. Its effective states also carry a continuous current reward, so its two-state description does not contradict our minimum count of microscopic heat-jump states.

### 6.3 Close thermal antecedent: Ptaszyński–Esposito 2025

Primary source: [*Critical heat current fluctuations in Curie-Weiss model in and out of equilibrium*](https://arxiv.org/html/2411.19643v3), [Physical Review E 111, 034125](https://doi.org/10.1103/PhysRevE.111.034125). Section III.5, equations (46)–(48), uses switching between thermal-current values. Its noise formula has the same telegraph structure \(2(\Delta j)^2p_+p_-/(r_++r_-)\). The results also discuss an equilibrium fourth cumulant.

**Assessment:** Thermal switching and fluctuation divergence are established antecedents. The inspected comparison concerns large-system phase-transition scaling. No statement equivalent to simultaneous negative \(C_3/C_1,C_4/C_2\) divergence in a fixed three-state, fixed-law, fixed-current family was located in that text. This is bounded negative evidence, not proof of absence from every implication of that model.

### 6.4 Different expansion: Saryal et al. 2019

Primary source: [*Thermodynamic uncertainty relation in thermal transport*](https://arxiv.org/pdf/1907.10767), [Physical Review E 100, 042101](https://doi.org/10.1103/PhysRevE.100.042101). Section II, equations (3), (5) and (6), expands current cumulants and the uncertainty ratio in the thermal affinity \(A=\Delta\beta\). In that notation,

\[
C_3=R_1 A+O(A^2),\qquad
A\,C_2/C_1=2+\frac{R_1}{6G_1}A^2+O(A^3).
\]

Our family instead fixes \(A=\log2\) and sends a kinetic coupling to zero. A finite-affinity negative third cumulant is not a negative equilibrium response coefficient \(R_1\). The result does not contradict the variance-based uncertainty relation or this affinity expansion. No equivalent fixed-invariant counterexample was found in the inspected passage.

### 6.5 COLLISION / inherited auxiliary fact: two-state bound

The source's equation (76), specialised to \(N=2\), gives \(1/4\) for the minimum winding-current skewness ratio. A two-energy-state bath current counts a cycle up to a bounded state term; restoring the heat quantum gives \(E^2/4\). The manuscript's direct four-rate proof is an auxiliary self-contained minimality argument, not a claim to have discovered this inequality. No independent priority claim is made for its two-state fourth-cumulant calculation either.

### 6.6 Other inspected distinctions

- [Salazar, *Thermodynamic skewness relation from detailed fluctuation theorem*](https://arxiv.org/pdf/2208.11206), [PRE 106, L042101](https://doi.org/10.1103/PhysRevE.106.L042101): the existing audit inspected the full paper and its example. Negative skewness under fluctuation symmetry is not new; its finite-time entropy-production normalisation and engine setting differ from the frozen claim.
- [Gerry–Segal, *Full counting statistics and coherences: fluctuation symmetry in heat transport with the Unified quantum master equation*](https://arxiv.org/pdf/2212.11307): the existing audit inspected its thermal structure and higher-cumulant discussion. Quantum coherent dynamics are a different class; no equivalent classical three-state construction was located there.
- [Wampler–Barato, *Skewness and kurtosis in stochastic thermodynamics*](https://arxiv.org/pdf/2110.14540), [J. Phys. A 55, 014002](https://doi.org/10.1088/1751-8121/ac3b0c): inspected definitions concern first-passage-time cumulants, a different observable from fixed-time accumulated heat.

These are team inspection records preserved from `literature_audit.md`; this consolidation does not claim a new independent full reading of all three papers.

## 7. Negative evidence and missingness audit

No equivalent resolution of the exact thermal conjectures or the fixed-invariant three-state family was found in the recorded corpus. This supports a bounded contribution claim only. The most material remaining risk is an earlier gated-conductor or blockade model whose printed formulas already imply the same thermal violations but whose title and abstract do not use the target keywords.

The following work was **not** completed or is not evidenced by the ledger:

- exhaustive Web of Science, Scopus, MathSciNet, zbMATH or Google Scholar citation retrieval;
- an exhaustive search of all references and all descendants of the 2022, 2004 and 2025 papers;
- systematic non-English literature searches, theses, conference proceedings and unindexed manuscripts;
- OEIS, long exact-coefficient searches, canonical matrix-hash searches or graph-database searches;
- a systematic survey of every thermal gate, dark-state or dynamical-blockade model;
- author enquiry about prior examples, corrections, unpublished results or intended hidden restrictions.

The listed primary texts were accessible. Accessibility of unqueried subscription databases is unknown, rather than established to be impossible. Some quoted web queries returned generic expansions or irrelevant results; that is weak evidence and is not treated as a proof of absence. Search-engine coverage and indexing dates can lag publication.

The source's conjecture label alone is not evidence that the problem remained open on the search date. The report distinguishes: (i) the verified inconsistency between the source's inequalities and our exact admissible model; (ii) whether someone else already noticed that inconsistency; and (iii) whether the strengthened fixed-invariant theorem has an earlier equivalent. Only (i) is established without a historical qualification.

## 8. Outcome by contribution unit

| Unit | Outcome | Confidence | Allowed wording | Forbidden wording |
|---|---|---|---|---|
| Exact refutation of source equations (19)–(20) | **BOUNDED UNCERTAINTY** about priority; mathematical refutation verified | High on the assumption match and algebra; bounded on history | “These rates provide an exact counterexample to the stated conjectures.” | “This was certainly an unresolved problem until today.” |
| Stronger fixed-invariant negative divergence statement | **BOUNDED UNCERTAINTY** | High on proof; moderate on absence of an earlier equivalent | “No equivalent fixed-invariant construction was found in this bounded search.” | “The first such thermal theorem in the literature.” |
| Complete proof of the thermal embedding and divergence | **BOUNDED UNCERTAINTY** about proof priority | High on internal independent checks | “A complete proof and exact certificates are supplied.” | “The first proof,” without additional historical evidence. |
| Cross-identification with the telegraph generating function | **COLLISION** | High; exact two-by-two substitution checked | “The effective generator is the established telegraph generator.” | “A new switching mechanism” or “a new universal cumulant formula.” |
| Thermal switching as a physical explanation | **COLLISION** at the mechanism level | High from inspected 2025 thermal antecedent | “An explicit finite thermal realisation of known switching behaviour.” | “The discovery that thermal switching can amplify fluctuations.” |
| Two-state sharp skewness bound | **COLLISION / inherited result** | High for the source's two-state specialisation | “A self-contained auxiliary bound establishes the minimum state count.” | “A new two-state skewness inequality.” |
| Specific bridge to a full-support fixed-law thermal family | **BOUNDED UNCERTAINTY**; candidate bridge | Moderate historical confidence | “The construction connects the known normal form to the stated constrained thermal class.” | “A new identification across all literatures.” |
| Verification artefact | Project-specific implementation; **COLLISION** for the general methods | High on reproducibility | “Independent exact determinant and Poisson calculations reproduce the certificates.” | “A new cumulant algorithm” or “numerical agreement proves novelty.” |

## 9. Decision

**BOUNDED UNCERTAINTY**, with explicit **COLLISION** markers for the telegraph normal form, generic switching cumulants, thermal switching mechanism and inherited two-state bound.

Proceed with the narrow manuscript claim: an exact thermal counterexample and a stronger fixed-invariant divergence theorem, accompanied by a self-contained minimality argument. Retain the prominent primary-source comparisons and the bounded search statement. Do not promote the mechanism or the historical priority to a stronger claim.

The report is complete as a record of the performed gate, including its missingness. It is not a certificate that the literature is exhausted. The mathematical counterexample remains valid even if an earlier equivalent is later located; such a finding would change the contribution classification, citations and presentation, not the verified sign calculation.

Before any claim of first discovery, the most valuable next step is a targeted enquiry to the source author and a systematic citation/alias search of thermal gated-conductor models. No enquiry was sent during this task.

## 10. Rerun triggers

Rerun the gate if any of the following occurs:

1. An earlier thermal rate model is found that reduces to the same cubic or limiting two-state generator after relabelling, a current-boundary correction, or common time scaling.
2. A closed-form family, renewal representation or cumulant recurrence identifies a named gated-transport model not covered by the current corpus.
3. A correction, revised source version, author response or citing paper addresses equations (19)–(20).
4. The contribution is extended to a general thermal embedding theorem, a different minimum state count, all higher cumulants or a bound involving kinetic information.
5. The frozen invariant list changes. Holding temperatures alone fixed is a different statement from fixing energies, the complete stationary law, mean current and entropy production simultaneously.
6. A publication or public announcement is prepared: check work appearing or indexed after 20 October 2026 and update the historical wording.

The simplification to the telegraph quadratic already triggered the present collision check. The full-support fixed-stationary family triggered the explicit constrained-embedding comparison. Neither rerun established absolute historical priority.
