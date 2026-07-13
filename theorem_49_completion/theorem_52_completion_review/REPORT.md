# Review of `theorem_49_completion.tex` against Theorem 52

**Date:** 2026-07-09
**File reviewed:** `theorem_49_completion/theorem_49_completion.tex`
**Target:** Theorem 52 of the thesis (label `theorem:ramification_after_blowup_is_tame_for_p_power`,
`sections/RamificationAfterBlowupIsTame.tex:859`; formerly numbered 49 — `main.aux` confirms the
label currently resolves to **52**).

---

## Verdict

**Yes — the document proves the intended theorem.** The theorem it targets is identified by
*label*, not by number, and the label matches the current Theorem 52 exactly. The stated goal
("For $G=\mathbb{Z}/p^r\mathbb{Z}$, $\mathcal{P}^{[\deg\mathfrak{n}]}$ is unramified at
$\eta_\mathfrak{n}$") is the same statement, under the same standing hypotheses (ramification of
$\mathcal{P}$ bounded by the modulus). I checked the proof step by step, and every convention it
imports from the thesis against the thesis's actual definitions; the architecture is sound and
the two new key lemmas are correct. The proof is **conditional on exactly one external input**
(the Schmid–Witt break formula, `thm:schmid-witt`), whose citation is the most significant issue
found — see Problem 1.

No fatal error was found. The problems listed below are: one citation gap on the single imported
result, several small justification gaps, one mischaracterized cross-reference, and integration
housekeeping.

---

## 1. Does it prove the *same* statement? (convention audit)

Every interface between the standalone document and the thesis was checked against the thesis
source:

| Interface | Completion document | Thesis | Match? |
|---|---|---|---|
| Theorem statement | "$\mathcal{P}^{[d]}$ unramified at $\eta_\mathfrak{n}$", $d=\deg\mathfrak{n}=n$ | Thm 52: "$\mathcal{P}^{[\deg\mathfrak{n}]}$ is unramified at $\eta_\mathfrak{n}$" | ✔ |
| "Ramification bounded by $d$" | $\mu(\underline{f})\le d-1$ via `thm:schmid-witt` | `definition:local_ramification_boundness` (RamificationAfterBlowupIsTame.tex:73): $H^{d}=1$ in upper numbering. With break at $m$ meaning $G^{(m)}\ne 1$, $G^{(m+1)}=1$ (`theorem:artin_schreier_ramification`, Preliminaries.tex:741), $H^d=1 \iff \mu\le d-1$. Also consistent with `lemma:realization_over_Gm`(2): "bounded by $d$ iff $m<d$". | ✔ |
| $r=1$ specialization of `thm:schmid-witt` | $\mu=m_0$, break at $m_0$ | `theorem:artin_schreier_ramification`(3): $G^{(m)}=G$, $G^{(m+1)}=1$ | ✔ |
| Definition of $\mathcal{P}^{[d]}$ | $\mathcal{P}^{\times d}/\Xi$, $\Xi=K_G\rtimes S_d$, $K_G=\ker(G^d\to G)$; quotient = Spec of invariants | `cor:sym-power-quotient` + `prop:symmetric_power_torsor` (Preliminaries.tex:392–434) | ✔ |
| "Unramified" for a DVR | $e_i=1$, separable residue extensions, per field factor | `definition:tamely_ramified_dvrs` (Preliminaries.tex:626), `definition:tamely_ramified_in_codim_1` | ✔ (but see Problem 5) |
| Local model at $\eta_\mathfrak{n}$ | $v_\eta(e_j)=1$, $\kappa(\eta)=k(e_1/e_d,\dots,e_{d-1}/e_d)$, $\widehat{R}=\kappa(\eta)[[e_d]]$ | `lemma:formal_local_invariance`(2) (RamificationAfterBlowupIsTame.tex:485–487) | ✔ |
| Reduction to $\mathbb{P}^1$ | invariance principle | `lemma:formal_local_invariance` + `cor:reduction_to_P1`; the corollary needs only $\mathcal{Q}_x\cong\mathcal{P}_x$ over $k((x))$, which holds since both have class $[\underline{f}]$ | ✔ |

Note the completion works over $U=\mathbb{P}^1\setminus\{0\}$ (modulus $d\cdot 0$) rather than the
thesis's $\mathbb{G}_m$ (modulus $d\cdot 0+\infty$); this is fine because `cor:reduction_to_P1`
allows different curves/moduli on the two sides, and $\mathcal{P}_{\underline{f}}$ is étale over
all of $\operatorname{Spec} k[y]$.

Also verified: all thesis labels the document `\Cref`s exist in the compiled thesis
(`theorem:ramification_after_blowup_is_tame_for_p_power`, `theorem:artin_schreier_ramification`,
`theorem:kummer_ramification`, `definition:tamely_ramified_dvrs`,
`definition:local_ramification_boundness`, `definition:tamely_ramified_in_codim_1`,
`cor:sym-power-quotient`, `prop:quotient_torsors`,
`lemma:bounding_ramification_of_contracted_product`, `prop:ramification-external-product`,
`theorem:torsors_after_blowup_is_tame`, `ex:p2-counterexample` — the last is Example 70, defined
in `a_wrong_path/a_wrong_path.tex`, which *is* `\input` into `main.tex`). The referenced scripts
`witt_general.py`, `witt_r3.py` and `a_wrong_path.tex` exist.

## 2. Steps verified in detail (no errors found)

* **`lem:isobaric` / `lem:triangular`** (isobaricity and triangularity of Witt addition
  polynomials): the ghost-recursion induction is correct; dividing by $p^n$ over $\mathbb{Q}$
  doesn't change monomial supports.
* **`prop:etale`**: the triangular tower of Artin–Schreier equations, the lower-triangular
  Jacobian with diagonal $-1$, and the simply-transitive fiber action via
  `lem:kernel` are all correct.
* **`cor:integral-unramified`**: correct, and lands exactly in the thesis's
  `definition:tamely_ramified_dvrs`(1).
* **`prop:classification`**: the ASW exact sequence, vanishing of
  $H^1(U_{\text{ét}}, W_r(\mathcal{O}_U))$ by induction along
  $0\to\mathbb{G}_a\to W_r\to W_{r-1}\to 0$, and the boundary-map description are correct; the
  use of `lem:triangular`(2) is legitimate *here* (both vectors vanish below level $r-1$).
* **`thm:datum`** (the heart of the paper): I re-derived the triangular unipotent change of
  variables $X_{1,l}\mapsto Y_l$, the two-sided ideal identity
  $(\wp\underline{X}_i-\underline{f}(y_i))_i=(\wp\underline{Y}-\underline{F},\ \wp\underline{X}_j-\underline{f}(y_j))_{j\ge2}$
  via $P(u)-P(v)\in(u-v)$ plus additivity of $\wp$, the $K_G$-invariants via
  `lem:torsor-invariants` (with flatness of $B$), and the $S_d$-invariants via the free monomial
  basis. All correct. The residual $G$-action matches.
* **`lem:isobaric-bound`**: the estimate
  $\sum n_{i,l} m_l \le p^j\max_l(m_l/p^l)=p^{j-r+1}\mu\le\mu$ is correct (checked including the
  degenerate cases $f_l=0$).
* **`lem:integrality`**: the lex-leading-term algorithm argument that a symmetric polynomial of
  degree $D<d$ uses only $\varepsilon_1,\dots,\varepsilon_D$ is correct (a monomial of degree
  $\le D$ has at most $D$ parts, and the subtracted product
  $\varepsilon_1^{\lambda_1-\lambda_2}\cdots\varepsilon_s^{\lambda_s}$ has degree
  $\sum\lambda_i\le D$); $\varepsilon_j=e_{d-j}/e_d\in\kappa(\eta)$ for $j\le d-1$ is verified
  against the blowup chart.
* **Final assembly**: $\mu\le d-1<d$ ⇒ each $F_j\in\kappa(\eta)\subset\widehat{R}$ ⇒
  $\underline{F}'\in W_r(\widehat{R})$ ⇒ unramified. Correct.
* $r=1$ sanity check: the whole argument literally specializes to the thesis's existing inline
  lemma (RamificationAfterBlowupIsTame.tex:767–790). ✔

## 3. Problems found

### Problem 1 (most significant): the one external input is cited beyond its stated scope
`thm:schmid-witt` is attributed to `\cite{Thomas2005}`. Lara Thomas's paper works over local
fields **with finite residue field** ($\mathbb{F}_q((T))$). Here the theorem is applied over
$K=k((x))$ with $k$ **algebraically closed**. The break formula
$\mu=\max_l p^{r-1-l}m_l$ for reduced Witt vectors is classical and does hold for perfect residue
fields (it goes back to Schmid 1936/37; modern treatments valid in this generality include
Garuti, Obus–Pries, and Kato's conductor theory), but the citation as given does not literally
cover the use. Since this is the *only* non-elementary imported result, and the whole proof
hinges on the direction "ramification bounded by $d$ ⟹ $\mu\le d-1$" (the sharpness statement in
part (2)), the citation should be made airtight — either add a reference stated for perfect
residue fields, or include a proof/proof sketch in the Preliminaries. (Caveat: the thesis already
has this same imprecision in `theorem:artin_schreier_ramification`, which cites Thomas2005 while
being stated for perfect residue fields — so this is an inherited, thesis-wide issue, not a new
one.)

### Problem 2: wrong lemma cited inside the proof of `lem:reduction`
The "key point" — that subtracting $\wp(V^n(h))$ changes the level-$n$ component by exactly
$-\wp(h)$ and no lower component — is justified by `\Cref{lem:triangular}(2)`. But
triangularity (2) requires **both** vectors to vanish below level $n$, and here $\underline{a}$
is arbitrary. The fact is true, but the correct argument is: by triangularity (1), level-$l$
components of $\underline{u}-_W\underline{v}$ depend only on levels $\le l$; and
$E_l(X_{<l};0)=0$ identically (from the group identity $\underline{u}-_W\underline{0}=\underline{u}$
and uniqueness of the subtraction polynomials), so with $v_{<n}=0$ the levels $<n$ are unchanged
and level $n$ changes by exactly $-\,(h^p-h)$. Easy fix; should be repaired before integration,
since as cited the step doesn't follow.

### Problem 3: the concluding "sharpness" remark mischaracterizes `ex:p2-counterexample`
The remark claims: "for $p=2$, $r=2$, $m_0=1$ (so $\mu=2$) the symmetric square ($d=2$) is
ramified at $\eta_\mathfrak{n}$ (\Cref{ex:p2-counterexample})". The actual Example 70
(`a_wrong_path/a_wrong_path.tex:276`) is a different statement: it is the *absorption*
counterexample to the inductive proof strategy — it exhibits, for arbitrary $p$, a
$\mathbb{Z}/p^2$-tower where hypotheses (H1)–(H3) hold yet $E/K_C$ is ramified. It never computes
that a symmetric square is ramified at the generic point of an exceptional divisor, and it is not
specific to $p=2$, $\mu=2$. Either the description must be rewritten to match Example 70, or the
reference should point to (a yet-to-be-written) example that actually verifies the boundary case
$\mu\ge d$. Additionally, the sharpness claim itself ($\deg F_{r-1}=\mu$ exactly; the extremal
monomial survives mod $p$ with no top-degree cancellation) is asserted without proof — acceptable
in a remark, but nothing should be made to depend on it.

### Problem 4: the non-surjective-$\rho$ case of `thm:schmid-witt` rests on an unproved remark
The remark following `thm:schmid-witt` handles characters of order $p^{r'}<p^r$ by asserting that
$\mu$ is invariant under the Verschiebung identification. This is true — a reduced vector with
$f_l=0$ for $l<v$ is exactly $V^v$ of a reduced length-$(r-v)$ vector, and the weights
$p^{r-1-l}$ restrict correctly — but two facts are used silently: (i) for reduced
$\underline{f}$, the character has order exactly $p^{\,r-v}$ with $v=\min\{l: f_l\ne0\}$ (this
needs: a nonzero reduced component is not in $\wp(K)$); (ii) $V$ intertwines $\wp$ and induces
multiplication by $p^{\,r-r'}$ on $W(\mathbb{F}_p)$, matching the subgroup inclusion
$\mathbb{Z}/p^{r'}\hookrightarrow\mathbb{Z}/p^{r}$. Worth two or three explicit lines, since the
theorem *is* applied to possibly non-surjective local characters (nothing in the standing
hypotheses forces $\mathcal{P}$ to be connected or totally ramified at $P$).

### Problem 5: completed vs. uncompleted local ring in the last step
The final proof establishes unramifiedness of
$\mathcal{P}^{[d]}|_{\operatorname{Spec}\widehat{K}_\eta}$ with respect to
$\widehat{R}=\kappa(\eta)[[e_d]]$, then closes with "ramification at $\eta_\mathfrak{n}$ is
computed exactly on this restriction (\Cref{definition:tamely_ramified_in_codim_1}...)". But that
definition uses the **uncompleted** $K_\eta=\operatorname{Frac}(\mathcal{O}_{X_\mathfrak{n},\eta})$.
The equivalence (ramification indices, residue degrees and separability are preserved under
$-\otimes_{K_\eta}\widehat{K}_\eta$) is standard, but it is stated nowhere — the thesis's
`lemma:formal_local_invariance` makes the same silent jump ("is by definition read off from" the
completed restriction). One preliminary lemma would close this gap for both documents at once.

### Problem 6: perfectness of $k$ is silently assumed
`subsec:reductions` opens with "étale base change to $k^{sep}=\bar{k}$", which presupposes $k$
perfect ($\bar{k}\ne k^{sep}$ otherwise, and $\bar{k}/k$ is not separable). The thesis's own
reduction remark (RamificationAfterBlowupIsTame.tex:442) says explicitly "Assume $k$ is perfect";
neither Theorem 52's statement nor the completion's Goal records this hypothesis. Since the
downstream application (`theorem:SymmetricPowerOfSheafIsTamelyRamified`) invokes the theorem with
$k$ algebraically closed anyway, the honest fix is to state the perfectness (or algebraic
closedness) assumption in the theorem or in the section preamble.

### Problem 7 (housekeeping): stale numbering, broken standalone build, unresolved refs
* The title and header comments hardcode "Theorem 49" (`\texorpdfstring{...}{Theorem 49}`,
  the top comment block, and the phrase "open point (1) of .../general_witt_proof.tex"). After
  integration the `\Cref` will print 52 automatically, but the hardcoded "49"s and the folder
  name will confuse readers. Recommend renaming or at least a comment noting 49 → 52.
* The standalone document has no `\externaldocument` (xr): all `\Cref`s to thesis labels render
  as "??" in the standalone PDF. Fine after integration, but worth knowing when reading the PDF.
* The most recent build in the folder **failed** (`theorem_49_completion.log` ends in an
  emergency stop: `\input{includes}` not found). It must be compiled with
  `TEXINPUTS=../..:` as the header says; the shipped PDF is from an earlier successful run.

### Problem 8 (integration): duplication with the Preliminaries
Sections 1–2 (Witt vectors, ASW theory) partially duplicate and partially generalize existing
Preliminaries material (`theorem:artin_schreier_ramification`, the torsor/character
correspondence `cor:abelian_equivilance_fundamental_torsors`, Kummer/AS theory). The document's
own integration notes acknowledge this. Two concrete watch-items when merging:
* If `thm:schmid-witt` *replaces* `theorem:artin_schreier_ramification` as proposed, check that
  `lemma:realization_over_Gm`(2) and `ex:p2-counterexample`/`ex:absorption-explicit` (which cite
  the $r=1$ theorem by its parts (1)–(3)) still have the statements they need.
* `prop:classification` overlaps with the character description already used at
  RamificationAfterBlowupIsTame.tex:103–117; the two should be reconciled, not duplicated.

## 4. Minor observations (no action strictly required)

* `lem:additivity` is proved but never used by the main line — `thm:datum` re-runs the same
  argument $d$-fold. Could be dropped or `thm:datum` could invoke it by induction.
* In `thm:datum` Step 1, $T^{K_G}=B\otimes_{A^{\otimes d}}(T')^{G^{d-1}}$ silently uses that
  taking finite-group invariants commutes with the flat base change $-\otimes B$ ($B$ free); one
  clause would make it explicit.
* The $d=1$ edge case works degenerately ($\mu\le 0$ forces the trivial class), consistent with
  the thesis conventions.
* The document is noticeably more careful than the surrounding thesis section (e.g. it fixes
  nothing-up-my-sleeve issues like connectedness of $\mathcal{P}$ that the old broken proof
  glossed over, and does not need the totally-ramified reduction at all).

## 5. Bottom line and recommended actions, in order

1. Fix the `lem:reduction` justification (Problem 2) — small but a genuine logical gap as written.
2. Solidify the Schmid–Witt citation for perfect/algebraically closed residue fields (Problem 1),
   and expand the Verschiebung remark (Problem 4).
3. Correct the description of `ex:p2-counterexample` in the concluding remark (Problem 3).
4. Add the perfectness hypothesis and the completed-vs-uncompleted lemma (Problems 5–6) — these
   also repair pre-existing thesis-side gaps.
5. Do the renumbering/renaming housekeeping and the integration per the document's own notes
   (Problems 7–8).

With items 1–3 done, the document is, in my assessment, a correct and complete replacement for
the broken inductive proof of Theorem 52.
