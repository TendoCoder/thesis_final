# Gap closure for `induction_completion.tex`

`gap_closure.tex` (compiled: `gap_closure.pdf`) closes the two critical gaps identified in
`../induction_completion_review/REPORT.md`, yielding an **unconditional** proof of
Theorem 52 (`theorem:ramification_after_blowup_is_tame_for_p_power`): for
$G = \mathbb{Z}/p^r\mathbb{Z}$, the symmetric power $\mathcal{P}^{[\deg\mathfrak{n}]}$ is
unramified at $\eta_\mathfrak{n}$.

## How each report item is resolved

**Critical gap 1 (the "principal part" step — unjustified, and false as stated).**
Replaced by a genuine $W_r$-realization lemma (Lemma 9 in the note), proved via the
repair strategy sketched in the report:

- Lemma 6: $\wp$ is surjective on $W_r(k[[x]])$ (induction on $r$ through the exact
  sequence $0 \to W_1 \xrightarrow{V^{r-1}} W_r \to W_{r-1} \to 0$, base case = the
  thesis's $r=1$ computation).
- Proposition 7: every class in $W_r(k((x)))/\wp$ has a **reduced polynomial
  representative** (all components in $x^{-1}k[x^{-1}]$, pole orders zero or prime to
  $p$). Key point: adjustments at the top level use $V^{r-1}$-moves, which are
  **carry-free** (Lemma 2(iii), proved by ghost components), so they never disturb the
  already-fixed lower components; the induction on $r$ through the truncation
  $W_r \twoheadrightarrow W_{r-1}$ handles all lower levels. No componentwise
  "principal part" of a Witt vector is ever taken.
- Proposition 8 (Schmid–Witt break formula): stated with "reduced" defined
  ($m_j := \max(0, -v_x(f_j))$, zero or prime to $p$), only the direction actually used
  (evaluating on one reduced representative computes the largest upper break), with a
  remark explaining why reducedness makes the formula exact (no ties possible).
  Citations: Kanesaka–Sekiguchi 1979, Thomas 2005, Elder–Keating arXiv:2503.16830.
- The realization lemma also proves the degree-$p^r$ class forces $f_0 \neq 0$
  (via $p^{r-1}V = V^r F^{r-1} = 0$), extends the torsor over
  $\mathbb{P}^1\setminus\{0\}$, and derives `eq:polebound`
  ($p^{r-1-j} m_j < d$) from ramification bounded by $d$.

**Critical gap 2 (identification of the cover at $\eta_C$ — asserted, not proved).**
Proposition 12: the honest Witt-coordinate invariant computation generalizing thesis
lines 726–765. The Witt sum $\vec Y = \bigoplus_i \vec X_i$ is invariant under the
twisted $G^{d-1}$-action (telescoping) and under $S_d$, satisfies
$\wp\vec Y = \bigoplus_i \vec f(x_i)$ by additivity of $\wp$, and the induced map of
$G$-torsors is an isomorphism because **any equivariant morphism of torsors is one**
(Lemma 4) — replacing the rank count, which alone would not show generation. The
$S_d$-symmetry of the components $\alpha_n$ (hence
$\alpha_n \in k[e_1,\dots,e_d,e_d^{-1}]$) is stated and proved explicitly, and a remark
records why a pure $H^1$-restriction argument would not descend to the symmetric base.

**Degree count (§4).** The review-verified Lemmas (symmetric regularity, isobaricity)
and the estimate $\sum_j E_j m_j < d\,p^{\,n-(r-1)} \le d$ are reproduced verbatim-in-
substance, now fed with legitimate inputs (polynomial components, identified cover).

**Minor issues from the report also addressed:**
- "reduced representative" is defined; $m_j := \max(0, -v_x(f_j))$;
- only the existence direction of the break formula is used;
- sanity-check remark: $p^{r-1-j} \ge d$ forces $f_j = 0$;
- framed as a **direct proof for all $r$** (not an induction); the final remark notes
  that on merge, the thesis proof body from "We proceed by induction on $r$" onward
  (including the unjustified upper/lower-numbering step at line ~891) must be replaced,
  while the preceding reduction paragraph (lines 863–872) is kept;
- ASW étale/torsor facts isolated in one lemma (Lang isogeny), used both over
  $k[x,x^{-1}]$ and over $\widehat{\mathcal{O}}_\eta = \kappa(\eta)[[e_d]]$;
- no hard-coded proposition numbers: thesis results are referenced by label name
  (`cor:reduction_to_P1`, `eq:complete_field_at_generic_point`, ...); on merge, replace
  with `\Cref`. `KanesakaSekiguchi1979` and `ElderKeating2025` are not yet in `Bib.bib`.

## Not done here (follow-ups)

1. Merge §§2–5 into `sections/RamificationAfterBlowupIsTame.tex`, replacing the current
   proof body of Theorem 52 from line 874 on (keep lines 863–872).
2. §§2–3 of the original `induction_completion.tex` (the (H1)/(H2) heuristics) contain
   the upper/lower-numbering error flagged in the report; they are not used here and
   should be demoted or dropped on merge.
3. Add the two missing bibliography entries to `Bib.bib`.

Build: `pdflatex gap_closure.tex` (×2).
