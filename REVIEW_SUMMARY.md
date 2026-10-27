# Review summary (rating-free public record)

All review was internal and AI-assisted. The original reports are kept privately. This summary keeps the substance of the objections and how each was resolved, without scores or ratings.

## Round 1

An editor, four reviewer roles (methodology, domain, perspective, devil's advocate) and an outside-model correctness audit raised these points, among others:
- the significance and purpose of a sign bound;
- thin literature;
- why random search missed the violations;
- context for non-specialists;
- physical accessibility;
- the point that unboundedness is variance growth;
- overreach in "necessary" and "phase diagram";
- a hypothesis-by-hypothesis match with the source;
- the breadth of the "thermodynamic-only" claim;
- the minimality class;
- gaps in proof display;
- code hygiene.

Each item and its disposition is in [REVISION_RESPONSE.md](REVISION_RESPONSE.md).

## Verification of the revision

- **Re-review.** The re-review found every major item addressed. It replayed the census, the certificates and the figures byte-identically from a fresh copy, matched all 16 references on Crossref and inspected every PDF page. It asked for seven copy-level fixes: the README package versions, the hertz-switching record length, qualifying the two-state claim by model class, "of order 10^2", the census denominator, the source's sampling wording, and the wording of one response item.
- **Proof audit.** The audit used its own exact full-counting-statistics code and found Lemma 4.2, Theorem 4.3, Corollary 4.4, Theorem 5.1, Propositions 6.1, 6.2 and 7.1 correct. It found minor gaps in Theorem 6.3 (C1 > 0 and C2 > 0 were used but not assumed) and Remark 6.4 (continuity of S and K where C1 or C2 vanish). It noted that the six-state asymptotics set in late.
- **Final outside-model audit.** The audit agreed that the counterexamples are correct. It showed that Theorem 6.3 is false as stated: a trap family with reversed temperature ordering has C1 < 0 while S tends to minus infinity. It asked for "spectral separation" in place of "spectral gap" outside the reversible case, for the continuity claim of Remark 6.4 to be restricted, and for narrower novelty framing: the telegraph formulas are standard, Proposition 6.2 is an amplification, and the Theorem 6.3 machinery is standard.

All of these were fixed in [FINAL_FIXES.md](FINAL_FIXES.md). No further review round followed.

## Open after review

The kinetic constants are loose. There is no explicit disparity threshold. Whether K-hat >= -15/4 holds for three states is open. The source's other inequalities were not tested. The search for related work was bounded.
