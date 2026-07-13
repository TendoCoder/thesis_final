# Review of `induction_completion.tex` — does it prove Theorem 52?

**Target statement (Theorem 52, `theorem:ramification_after_blowup_is_tame_for_p_power`,
`sections/RamificationAfterBlowupIsTame.tex:859`):**
for $G=\mathbb{Z}/p^r\mathbb{Z}$ and $\mathcal{P}\to U=C\setminus\mathfrak{m}$ a $G$-torsor with
ramification bounded by $\mathfrak{n}=nP$, the symmetric power $\mathcal{P}^{[\deg\mathfrak{n}]}$
is unramified at $\eta_\mathfrak{n}$. The thesis's current proof stops at a red-flagged gap
(line 897).

## Verdict

**The core mechanism of §4 is correct, and it is (in my assessment) the right proof of
Theorem 52 — but the note as written does not yet prove it.** Two load-bearing steps are
asserted without proof, and one of them ("take the principal part of the Witt datum") is
actually *false* under its most natural reading. In addition, the motivational sections §§2–3
contain a genuine error (an upper/lower-numbering confusion in the justification of (H2)),
which is the *same* error that sits in the thesis's current partial proof of Theorem 52.

What is fully correct and verified line by line:

* **Lemma 2 (symmetric regularity)** — correct. A symmetric polynomial in
  $y_i=1/x_i$ with all monomials of total degree $<d$ expands in
  $e_1(y),\dots,e_{d-1}(y)$ only (isobaric expansion of $m_\lambda$, $|\lambda|<d$), and
  $e_k(y)=e_{d-k}(x)/e_d(x)$ lies *exactly* in
  $\kappa(\eta)=k(e_1/e_d,\dots,e_{d-1}/e_d)$. The strict bound $<d$ is precisely what
  excludes $e_d(y)=1/e_d(x)$, the only source of a pole. ✓
* **Lemma 3 (isobaricity of Witt addition)** — correct. The ghost-component induction
  ($p^nS_n=\sum_j p^j(a_j^{p^{n-j}}+b_j^{p^{n-j}})-\sum_{j<n}p^jS_j^{p^{n-j}}$) shows each
  universal addition polynomial is isobaric of weight exactly $p^n$ over $\mathbb{Z}$, hence
  over $\mathbb{F}_p$, and this persists under $d$-fold iteration. ✓
* **Theorem 5's degree count** — airtight *given its inputs*. For a monomial with exponents
  $E_j$, $\sum_j E_jp^j=p^n$ gives total $y$-degree
  $\sum_j E_jm_j<d\,p^{-(r-1)}\sum_jE_jp^j=d\,p^{n-(r-1)}\le d$, strictly (some $E_j>0$,
  and $m_j<dp^{j-(r-1)}$ is strict even when $m_j=0$). Regular Witt class over the DVR
  $\Rightarrow$ étale cover $\Rightarrow$ unramified: standard, and the derivative-of-$\wp$
  remark suffices. ✓
* **Convention bookkeeping** — the thesis defines "ramification bounded by $d$" as
  $H^d=1$ in upper numbering (`RamificationAfterBlowupIsTame.tex:73-77`), i.e. largest
  break $u<d$ strictly; this matches both the note's hypothesis and the $r=1$ usage
  ($m<d$, line 645 of the thesis file). ✓
* The local field description $\widehat K_{\eta}= \kappa(\eta)((e_d))$ matches
  `eq:complete_field_at_generic_point` (the note even silently fixes the thesis typo
  $e_{d-1}/u_d$). ✓

The problems are in how the argument is *fed*: which Witt datum $\vec f$ one is allowed to
use, and why the symmetric-power cover at $\eta_C$ is the Artin–Schreier–Witt cover of the
Witt sum $\bigoplus_i \vec f(x_i)$ at all. These are Gaps 1 and 2 below.

---

## Critical gap 1: the "principal part" step is unjustified — and naively false

§4 opens (lines 210–214): *"We take $\vec f=(f_0,\dots,f_{r-1})$ to be the principal part at
$p_\infty$."* Two distinct problems:

**(a) There is no $W_r$ realization lemma in the thesis.** The reduction chain that makes
$\vec f$ a vector of Laurent *polynomials* is `cor:reduction_to_P1` +
`lemma:realization_over_Gm` — and the realization lemma
(`RamificationAfterBlowupIsTame.tex:592`) covers only the tame case and $G=\mathbb{Z}/p\mathbb{Z}$.
Nothing in the thesis or the note produces, for a $\mathbb{Z}/p^r\mathbb{Z}$-torsor on the
punctured disc with break $<d$, a torsor over $\mathbb{G}_m$ whose Witt datum has components in
$x^{-1}k[x^{-1}]$ with $p^{r-1-j}m_j<d$. Without this, "$f_j(x_i)$ is a polynomial in $y_i$ of
degree $m_j$" — the hypothesis of the entire degree count — is not available: a general
representative is a Laurent *series*, and substituting $x\mapsto x_i$ and Witt-summing a series
is not even defined algebraically in $\widehat K_\eta$ without a separate convergence argument.

**(b) "Principal part" of a Witt vector is not a legitimate operation.** Witt addition is not
componentwise, so componentwise truncation to polar parts changes the ASW class
uncontrollably. Concretely for $r=2$: writing $f_0=f_0^-+f_0^+$, the Witt sum
$(f_0^-,\,\cdot\,)\oplus(f_0^+,\,\cdot\,)$ produces the carry
$-\sum_{0<i<p}\tfrac1p\binom{p}{i}(f_0^-)^i(f_0^+)^{p-i}$ in the second component, and these
mixed products $(\text{polar})^i(\text{regular})^{p-i}$ generally still have poles. So the
componentwise principal part $\vec f^-$ does **not** differ from $\vec f$ by a Witt vector
that is regular at $p_\infty$, and the note's replacement argument (lines 238–240, which
correctly handles $\wp$-equivalence but only that) does not cover this step.

**How to fix.** Prove the $W_r$-analogue of `lemma:realization_over_Gm`(2); the ingredients
are all standard and half of them are already in the thesis's $r=1$ proof:

1. $\wp$ is surjective on $W_r(k[[x]])$ for $k$ algebraically closed (levelwise, via the
   surjectivity of $\wp$ on $k[[x]]$ already proved at line 636, plus the exact sequences
   $0\to W_1\xrightarrow{V^{r-1}}W_r\to W_{r-1}\to 0$; equivalently
   $H^1_{\text{ét}}(\operatorname{Spec}k[[x]],\mathbb{Z}/p^r)=0$).
2. Adding $V^{r-1}(h)$ to a Witt vector changes *only* the last component, by $+h$, with no
   carries. So by induction on $r$ through the truncation $W_r\twoheadrightarrow W_{r-1}$,
   every class in $W_r(k((x)))/\wp$ has a representative with all components in
   $x^{-1}k[x^{-1}]$: fix the first $r-1$ components by induction, then clean the regular
   tail of the last component using $\wp V^{r-1}=V^{r-1}\wp$ and step 1.
3. Reduce pole orders to be prime to $p$ exactly as in the existing lemma (line 640),
   applied level by level (again adjustments propagate only upward through components and
   can be re-cleaned by step 2).
4. Only then invoke the break formula to conclude the reduced representative satisfies
   $\max_j p^{r-1-j}m_j = u < d$, which is `eq:polebound`.

Note the order matters: the representative must be made *rational (polynomial)* before any
symmetrization, so that all subsequent $\wp$-adjustments live in
$W_r(k(e_1,\dots,e_d))\subset W_r(\widehat K_\eta)$ and the note's lines 238–240 apply
verbatim.

## Critical gap 2: the identification of the cover at $\eta_C$ is asserted, not proved

Lines 199–204 claim the cover $\mathcal{P}^{[d]_G}$ over $\widehat K_{\eta_C}$ "is the
Artin–Schreier–Witt extension $\wp(\vec Z)=\vec\alpha$" with
$\vec\alpha=\bigoplus_{i=1}^d\vec f(x_i)$, citing "the $r=1$ proof". But the $r=1$ proof
established this by an explicit invariant-ring computation
(`RamificationAfterBlowupIsTame.tex:726-765`: the invariant $Y=\sum_iX_i$ satisfies
$Y^p-Y=\sum_if(x_i)$, plus a rank count over $G^{d-1}$) — done *only* for $r=1$. For general
$r$ this needs its own proposition. Two viable routes:

* **Invariant computation with Witt coordinates** (the honest analogue): the Witt sum
  $\vec Y=\bigoplus_i\vec X_i$ is $G^{d-1}$-invariant (the twisted action shifts the
  $\vec X_i$ by Witt constants that telescope) and $S_d$-invariant, satisfies
  $\wp\vec Y=\bigoplus_i\vec f(x_i)$ by additivity of $\wp$, and generates by the same rank
  count $p^{rd}/p^{r(d-1)}=p^r$.
* **Character additivity**: the machinery is already in the thesis
  (`lemma:bounding_ramification_of_contracted_product`, whose proof observes that the class
  of a product torsor is the sum of characters). Caution: a pure
  $H^1(k(e))\to H^1(k(x_1,\dots,x_d))$ restriction argument is *not* automatic — restriction
  along a non-trivial extension has kernel — so the descent to the symmetric base still needs
  the invariant-theoretic or torsor-theoretic input; don't shortcut this.

Also worth one sentence in either route: the components of $\bigoplus_i\vec f(x_i)$ lie a
priori in $k(x_1,\dots,x_d)$; commutativity/associativity of Witt addition makes them
$S_d$-symmetric, hence in $k(e_1,\dots,e_d)\subset\widehat K_\eta$. The note uses this
implicitly.

## Error in §§2–3: (H2) is unjustified (upper vs. lower numbering)

Line 128–130 justifies (H2) — "its break at the point over $p_\infty$ is still $<d$" — by
*"lower numbering restricts to subgroups: $H_i=G_i\cap H$, and $G_d=1$."* The hypothesis of
Theorem 52 is $G^{(d)}=1$ in **upper** numbering (thesis Definition at
`RamificationAfterBlowupIsTame.tex:73-77`); $G_d=1$ in **lower** numbering does not follow.
For a totally ramified $\mathbb{Z}/p^r$-extension with upper breaks
$u_1\le\dots\le u_r<d$, the break of the top degree-$p$ layer $\mathcal{P}\to\mathcal{P}'$
(where upper $=$ lower, since the layer has degree $p$) is the largest **lower** break
$\ell_r=\psi(u_r)$, which can be of size $\approx p^{r-1}d$ — far above $d$. So the $r=1$
theorem over $C'$ with the degree-$d$ divisor cannot be applied, and **(H2) as stated is
unproven** (and there is no reason to believe it in general). The natural bound one *does*
get is against the pulled-back divisor $\pi^*\mathfrak{n}$ of degree $p^{r-1}d$ — which
mismatches the symmetric-power degree $d$; that mismatch, not merely the inertia-surjectivity
failure of §3, is why this route dies.

Two consequences:

1. The note presents (H1)+(H2) as *true but insufficient* (§3, "Conclusion"). In fact (H2)
   is not established at all. §3's Lemma 4 obstruction analysis is then a diagnosis of a
   hypothesis nobody has. Since §4 never uses §§2–3, the fix is to demote them explicitly to
   heuristics and correct the (H2) paragraph — or delete §§2–3 when merging.
2. **The same error is in the thesis itself**: the current partial proof of Theorem 52 says
   (`RamificationAfterBlowupIsTame.tex:891`) "since $\cP\to\cP'$ is a $\Z/p\Z$-torsor, we can
   apply the previous theorem" — the previous theorem requires ramification bounded by $d$,
   which is exactly the unverified $\ell_r<d$. The red flag at line 897 is thus even more
   warranted than stated: step (891) itself is unjustified. When §4's argument is merged,
   this whole passage should be replaced, not just its ending.

## Minor issues

* **Prop. 3 (Schmid–Witt break formula).** The citations are genuine — I verified
  Elder–Keating, *Artin–Schreier–Witt extensions and ramification breaks*, arXiv:2503.16830
  (2025) exists and proves exactly the perfect-residue-field break formulas
  (extending Kanesaka–Sekiguchi and Thomas); Thomas 2005 is already cited in the thesis.
  But: (i) "reduced representative" is never defined — state the condition (each $f_j$
  regular or with pole order prime to $p$, plus the tie-breaking conditions from the cited
  sources) or quote the sources' exact statement; (ii) isolate the one direction actually
  used: *existence* of a representative with $\max_jp^{r-1-j}m_j=u$; (iii) the definition
  $m_j:=-v_x(f_j)\ge0$ is wrong for $f_j$ with strictly positive valuation — it should be
  $m_j:=\max(0,-v_x(f_j))$.
* **Lemma 4 (wild base change).** The valuation argument is loose: the units
  $u(w_i)$ in $s_i=u(w_i)w_i^{p^{r-1}}$ are dropped after the first line, and "distinct
  monomials have distinct leading terms" needs the actual no-cancellation argument (the
  minimal-degree homogeneous part is a nonzero polynomial in $\tau$ because the residues
  $\tau_j/\tau_d$ are algebraically independent). Tolerable for a motivational lemma;
  tighten or flag as sketch.
* **"Completing the induction" is a misnomer.** §4 is not an induction: it proves all $r$
  directly (the abstract's "the base case $r=1$ is exactly the already-proven lemma" is
  inaccurate framing — §4 *reproves* $r=1$ as a special case and never invokes it). This is
  a feature, not a bug — say so; the Remark after Theorem 5 already half-says it (it
  subsumes (H1)).
* **`eq:polebound` side remark worth adding:** for $j$ with $p^{r-1-j}\ge d$ the bound
  forces $m_j=0$, i.e. all low Witt components must be entirely regular. This is a good
  sanity check and makes the strength of the hypothesis visible.
* **Integration hazards:** hard-coded "Proposition 23" happens to match
  `prop:torsor_tower_diagram` (currently numbered 23 in `main.aux`) but will rot — use
  `\Cref` on merge. `ElderKeating2025` is not in `Bib.bib` yet. Duplicate `\AS` definition
  (`\newcommand` line 22, `\providecommand` line 33) — harmless, delete one. The note's
  standing assumptions ("after the standard reductions… totally ramified, inertia all of
  $G$") correctly mirror the thesis's reduction (lines 863–872), which *is* valid for all
  $r$ — keep that part of the existing proof.

## Bottom line

Theorem 52 is, I believe, true, and §4's pole-bound + isobaricity + symmetric-degree-count
argument is a correct and elegant mechanism for it — the estimate
$\sum_jE_jm_j<dp^{n-(r-1)}\le d$ genuinely uses the hypothesis at every Witt level at once,
which is exactly what the (H1)/(H2) route cannot do. But the note currently proves:
*"**if** the Witt datum can be taken to be a reduced vector of polynomials in $x^{-1}$
satisfying `eq:polebound`, **and if** the symmetric-power cover at $\eta_C$ is the ASW cover
of the Witt sum, **then** Theorem 52 holds."* Both if's are missing lemmas (Gaps 1 and 2),
the first of which is stated in a form ("principal part") that is false as written though
repairable by the $V$-filtration argument sketched above. Until those two lemmas are written
out, Theorem 52 is not yet proved.

Suggested order of work: (1) $W_r$-realization lemma (Gap 1, subsumes the representative
choice); (2) Witt-coordinate invariant computation (Gap 2, generalizing thesis lines
726–765); (3) merge §4 + the two lemmas into `RamificationAfterBlowupIsTame.tex`, replacing
the current proof body from line 874 on; (4) rewrite or drop §§2–3 and fix the (H2)
justification if kept.
