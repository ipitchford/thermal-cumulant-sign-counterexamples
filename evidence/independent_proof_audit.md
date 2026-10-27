# Independent adversarial audit of the thermal-current results

**Reviewer:** control_scout, independently of the deriving agent.  
**Date:** 20 October 2026.  
**Verdict:** the mathematical claims inspected below pass. I found no fatal error or missing hypothesis that invalidates the counterexamples, three-state minimality, or full-support divergent family. Publication language still needs the qualifications listed in Section 6. Novelty and historical priority are outside this algebraic verdict.

## 1. Materials and source fidelity

I inspected `stochastic_scout_notes/theorems_and_proofs.md`, `thermal_counterexample.md`, `check_general_thermal.py`, and `fixed_stationary_full_support.json`. I also independently opened Ptaszynski's primary paper, *Bounds on skewness and kurtosis of steady state currents*, arXiv:2204.08421v4, PDF dated 21 July 2022, https://arxiv.org/pdf/2204.08421. The source's Section II, equations (8)–(14), defines the same long-time scaled cumulants used in the candidate. Equations (3) and (4) define the ratios C3/C1 and C4/C2. Equations (19) and (20) conjecture their nonnegativity for the stated thermal classes. Section III D, equations (63)–(70), allows finite classical Markov models with bath-resolved local detailed balance and the same tilted-generator convention used by the candidate.

In particular, the observed heat increment for a jump j to i induced by the cold bath is E_j-E_i. The candidate multiplies that off-diagonal channel rate by exp[z(E_j-E_i)] and leaves escape-rate diagonals untilted. Its orientation is correct. Reversing the current would also leave both proposed ratios unchanged, because the numerator and denominator of C3/C1 are both odd cumulants.

The source's random-test choice of rates in [0,1] is a sampling procedure, not an assumption restricting the conjecture. In any event a common reduction of all rates places any bounded example in that interval without changing either ratio.

## 2. Independent computational checks

I wrote `control_scout/audit_thermal_scaling.py` from scratch using standard-library rational arithmetic and a sparse multivariate-polynomial implementation. It imports none of the deriving agent's code. Its checks are algebraic identities, not floating-point comparisons:

1. It rebuilds the general active-pair-plus-trap determinant with t=exp(Ez) treated as a Laurent indeterminate. The claimed cubic characteristic polynomial agrees coefficient by coefficient.
2. It verifies the two-state lower-bound endpoint N(f,f/2-1/16)=1/32 and the strictly positive Bernstein-type decomposition of H(t). It also verifies the upper-endpoint substitution N(f,f^2)=f H(4f).
3. It constructs the full-support three-state tilted generator directly from the twelve channel rates. It substitutes x=epsilon*y and z=epsilon*k before expanding each matrix entry through epsilon^2. The determinant has zero coefficients at epsilon^0 and epsilon^1, and its epsilon^2 coefficient is exactly
   \[
   \frac{27}{2}\left[y^2+\left(28-\frac89k\right)y-\frac{160}{9}k\right].
   \]
4. It derives the first four derivatives of the limiting root by a separate quadratic power-series recurrence. They are exactly
   \[
   \frac{40}{63},\quad \frac{320}{27783},\quad
   -\frac{640}{1361367},\quad-\frac{5120}{1801088541}.
   \]
   The resulting ratio coefficients are exactly -16/21609 and -16/64827.
5. It checks the fixed stationary distribution and cold mean-current formula as polynomial identities in epsilon.

All assertions pass. The machine-readable result is `control_scout/thermal_independent_scaling_certificate.json`. The parent has also independently checked the finite cumulants with an eigenvector/Poisson-equation method, which does not reuse the determinant recurrence; that complements the present symbolic audit.

## 3. Two-state minimality: analytic audit

Let a,b denote upward/downward rates through every unobserved bath aggregated together, and c,d those through the observed bath. Every observed jump transfers the same magnitude E. The characteristic equation is
\[
 \chi^2+s\chi-p(e^{Ez}-1)-q(e^{-Ez}-1)=0,
 \quad s=a+b+c+d,\quad p=ad,\quad q=bc.
\]
This follows immediately by expanding the 2-by-2 tilted determinant; I checked the signs. Aggregating unobserved baths does not change the observable, so the result covers any finite number of thermal baths.

The inequality s>=2(sqrt p+sqrt q) is valid because a+d>=2sqrt(ad) and b+c>=2sqrt(bc). With f=(p+q)/s^2 and y=(p-q)^2/s^4, it yields
\[
 0\leq f\leq\tfrac14,\qquad
 \max(0,f/2-1/16)\leq y\leq f^2.
\]
No squaring with a negative side occurs: f<=1/4 ensures the right side of sqrt(f^2-y)<=1/4-f is nonnegative.

The C3/C1 expression, whenever C1 is nonzero, is E^2(1-6f+12y). For f<=1/8 it is at least E^2/4 by dropping y. For f>=1/8 the lower bound on y again gives E^2/4. Thus the third/first ratio cannot be negative.

The C4 numerator N(f,y) is concave in y because its y^2 coefficient is -120. A concave function on an interval is at least the minimum of its two endpoint values, so checking endpoints is sufficient. Both lower-endpoint pieces are positive for f>0. At the upper endpoint, H(4f)>0 for 0<=4f<=1 follows from the displayed nonnegative-term decomposition, which is positive even at both endpoints. Therefore C4>0. Also
\[
 C_2/(E^2s)=f-2y\geq f-2f^2\geq f/2>0
\]
when f>0. Consequently C4/C2>0 for every two-state model with a nontrivial extensive observed current.

This is stronger than required because local detailed balance was not used. One-state systems have no nontrivial heat-transfer current. Two states with equal energies likewise have zero heat increments. The three-state construction therefore is minimal for either negative ratio and for their simultaneous negativity. Boundary cases where all extensive cumulants vanish must be described as undefined ratios, rather than assigned zero or declared positive.

## 4. Singular scaling: analytic audit

For the general active conductor plus weak trap I checked the determinant by hand and by the independent Laurent-polynomial code. With u=a+c, v=b+d and w=u+v, the tilted off-diagonal product is uv+d(z). Expanding the determinant gives
\[
 x^3+[w+\epsilon(\alpha+\beta)]x^2
 +\epsilon(\beta w+\alpha v)x-(x+\epsilon\beta)d(z),
\]
exactly as claimed. Differentiating chi^3 gives 6C1^3 at order three and 36C1^2 C2 at order four. Differentiating T chi^2 gives 6T C1 C2 at order three and T(8C1 C3+6C2^2) at order four. These are the correct factorial conventions; there is no missing factorial in the recurrence.

The leading coefficient of C2 is positive. Dividing C3 by C1 cancels the sign of the driven current and leaves a sign determined by U-V. The leading coefficient of C4/C2 has sign U^2-3UV+V^2. Hence the simultaneous-negative interval
\[
 (3-\sqrt5)/2<U/V<1
\]
is correct. Its active-occupancy version 1/2<P<(5+sqrt5)/10 is algebraically equivalent. In the degenerate thermal-trap case alpha=beta and positive finite temperatures, u<v, so U/V=v/(u+v) lies in (1/2,1) and therefore within that interval.

For the full-support family, the quotient of the rescaled determinant by epsilon^2 is analytic near (epsilon,y,k)=(0,0,0): the first two epsilon coefficients vanish identically, as independently checked. Its derivative with respect to y at the origin is (27/2)*28=378, which is nonzero. The analytic implicit-function theorem therefore supplies a joint analytic branch y(epsilon,k). Conservation gives y(epsilon,0)=0. For positive epsilon the zero eigenvalue is simple, so this branch agrees locally with the scaled cumulant-generating eigenvalue. Analyticity permits differentiating the O(epsilon) expansion in k and proves
\[
 C_n(\epsilon)=\epsilon^{1-n}\{y_0^{(n)}(0)+O(\epsilon)\}
\]
for each fixed n. This closes the potential gap of inferring derivative convergence from mere pointwise eigenvalue convergence.

Because y0'(0) and y0''(0) are strictly positive, dividing the third and fourth asymptotic formulas gives the stated ratio expansions with O(epsilon^-1) remainders. The common rate rescaling multiplies every cumulant by the same positive factor, so neither ratio changes.

## 5. Fixed thermodynamics and full support

The energies (0,2,1) are distinct. For energy gap 2, the hot and cold rate ratios are 1/4 and 1/16; for gap 1 they are 1/2 and 1/4. These exactly match inverse temperatures log 2 and log 4 in the chosen energy units. All twelve rates are strictly positive for every epsilon>0, so each bath's transition graph is complete and the full process is irreducible.

The total upward/downward ratios 1/8, 9/20 and 5/18 agree with the respective stationary-probability ratios for pi=(40,5,18)/63. Thus pi is exactly stationary for every epsilon, without an asymptotic approximation.

The cold mean current is correctly
\[
 J_\epsilon=(40+32\epsilon+8\epsilon^2)/63.
\]
The global factor lambda_epsilon=40/(40+32epsilon+8epsilon^2) sets its value to 40/63, preserves pi and detailed balance, and preserves all cumulant ratios. At stationarity energy conservation gives J_hot=-J_cold, so the entropy-production rate is (beta_c-beta_h)J_cold=(40/63)log2 in units k_B=1. This is strictly positive and fixed.

The aggregate state generator is reversible with respect to pi. This does **not** imply thermodynamic equilibrium, because different baths induce parallel transitions with opposite bath-resolved fluxes. Their heat currents and entropy production remain nonzero. This distinction should be explained explicitly to prevent a misleading apparent contradiction.

The divergent family holds fixed the state count, distinct energy levels, bath temperatures, stationary law, positive heat current and positive entropy-production rate. Therefore no lower-bound function that is finite at this fixed tuple and depends only on those quantities can bound both ratios over the stated class. The result does not exclude bounds involving a positive lower rate bound, spectral gap, mixing time, or other kinetic information. Full support means each rate is positive; it does not mean a uniform positive lower bound as epsilon tends to zero.

## 6. Required qualifications and presentation fixes

1. **Undefined ratios.** State C3/C1 only when C1!=0 and C4/C2 only when C2>0. Discuss the continuous extension at equilibrium separately. For the exhibited family both denominators are strictly positive.
2. **Order of limits.** Define the cumulants by taking long observation time first for each fixed epsilon>0, then let epsilon tend to zero. The observation time needed to sample the slow mode grows as epsilon^-1. Nothing here asserts the same asymptotics if time is held fixed while epsilon vanishes.
3. **Units.** Set k_B=1 and specify a fixed energy and time unit, or write E=(0,2E_*,E_*), beta_h=log2/E_* and beta_c=log4/E_*. Each ratio then carries units E_*^2. State rates have units of inverse time. Do not present these ratios as conventional dimensionless standardised skewness or kurtosis.
4. **Fourth cumulant.** Explain that negative C4 is compatible with a positive fourth central moment; C4 subtracts three times the variance squared before taking the scaled long-time limit.
5. **Proof scope.** State the three-state minimality for the finite-state jump-process heat current in the source, with no self-transitions that carry independent energy quanta. The source's model has precisely this scope.
6. **Novelty.** Do not claim that slow switching, telegraph fluctuations or negative higher cumulants themselves are new. The proposed contribution is the resolution of the explicit thermal conjectures and the strengthened fixed-thermodynamics/minimality statements, subject to a bounded prior-art check.

No substantial mathematical revision is required by this audit. The strongest claims survive the independent reconstruction.
