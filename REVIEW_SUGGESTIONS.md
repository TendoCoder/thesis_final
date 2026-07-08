# Thesis Review — Suggestions for Clarity, Coherence, and Organization

Scope: everything included from `main.tex` (Introduction, Preliminaries, Ramification After
Blowup Is Tame, Geometric Class Field Theory, Proof of the Reduced Theorem,
`proof_completes/proof_complete.tex`, `a_wrong_path/a_wrong_path.tex`), plus the orphaned and
scratch files in the repo. **No edits were made** — this is a checklist to work through.

Legend: 🔴 = blocking (a reader/referee will stop here), 🟡 = important, 🟢 = polish.

---

## 1. Big-picture structure

### 1.1 🔴 The document's skeleton doesn't match the promised roadmap
`sections/Introduction.tex:110-116` promises three chapters (Preliminaries / Ramification After
Blowup Is Tame / Geometric Class Field Theory). The actual document has **seven** top-level
sections, including "Proof of Theorem 2" (`main.tex:60`), then three raw sections coming from
`proof_completes/proof_complete.tex` ("Setup and notation", "The master diagram",
"Unramifiedness of …"), then "A Wrong Path". Suggested target structure:

1. Introduction
2. Preliminaries
3. Ramification After Blowup Is Tame (with the completed proof — see §2.1 below)
4. Geometric Class Field Theory (absorb the short "Proof of Theorem 2" file as its final
   subsection — it is only 54 lines and is the payoff of the whole thesis; it deserves to sit
   inside the GCFT chapter, not float after it)
5. Appendix A: A Wrong Path (why the naive induction fails)

Update the roadmap paragraph to match, and mention the appendix there ("In Appendix A we
explain why the natural inductive approach fails, which motivated the direct computation of
Chapter 3" — this is genuinely interesting content and selling it in the intro helps the
narrative).

### 1.2 🔴 `proof_complete.tex` and `a_wrong_path.tex` are near-duplicates — keep one
Both files contain the same setup, the same four quotient schemes, the same "master diagram"
(byte-for-byte identical tikz-cd), and the same theorem (H1)–(H3). `a_wrong_path.tex` is the
polished narrative version (with the reduction steps R1/R2, the inertia-injection lemma, and
two fully worked counterexamples); `proof_complete.tex` is the raw working note ("Proof
Attempts / Attempt 1 … Where the argument stalls"). Including both (`main.tex:63-64`):

- duplicates ~100 lines of content and one entire diagram,
- creates a **duplicate label** `sec:master` (`proof_completes/proof_complete.tex:49` and
  `a_wrong_path/a_wrong_path.tex:56`), so `\Cref{sec:master}` resolves arbitrarily,
- puts un-numbered orphan sections in the table of contents.

Suggestion: drop `proof_complete.tex` from `main.tex` entirely and keep `a_wrong_path.tex` as
the appendix. Anything unique in `proof_complete.tex` (the explicit Galois-closure bookkeeping
in "Attempt 1") can be merged into the appendix if you want it.

### 1.3 🔴 The completed proof exists but is not in the thesis
`theorem_49_completion/theorem_49_completion.tex` (953 lines, standalone) contains what its
header describes as a complete, direct, Witt-vector proof of
`theorem:ramification_after_blowup_is_tame_for_p_power` — exactly the theorem whose in-thesis
proof is broken (see §2.1). Its own header says: "Sections 1–2 (Witt vectors, ASW theory) are
background intended for the Preliminaries; Sections 3–4 are the proof itself, intended to
replace the broken inductive proof in RamificationAfterBlowupIsTame.tex (lines 636–673)."
`induction_completion/induction_completion.tex` is an earlier note with the same goal.
**The single highest-value organizational task is doing this integration**: move the Witt/ASW
background into Preliminaries, replace the broken proof in
`sections/RamificationAfterBlowupIsTame.tex:632-677`, and retire the scratch note.

### 1.4 🟡 Orphaned and empty files
- `sections/Preliminaries/KummerTheory.tex` is not `\input` anywhere, yet Kummer ramification
  is central to Chapter 3. Either fold the useful parts into the Preliminaries "Kummer and
  Artin–Schreier Theories" subsection (which already covers most of it) or delete the file.
  It also contains its own red TODOs ("Something about the proof here doesn't work",
  "Check if the lang bib entry is correct (i generated it using ai)") — don't let those
  silently survive a future include.
- `sections/Preliminaries/Gtorsors.tex` is empty — delete.
- `sections/RamificationAfterBlowup.tex` is a superseded draft of the GCFT section (its
  theorem/label collide with `GeometricClassFieldTheory.tex`); it's only referenced from a
  commented-out line (`main.tex:58-59`). Delete or move to scratch.

### 1.5 🟡 Scratch directories mixed with the thesis source
`witt/`, `q_ramification_along_VF/`, `induction_completion/`, `theorem_49_completion/`,
`inertia_symmetry_obstruction/`, `claude_atm_1/`, `claude_atm_2/`, and
`proof_completes/proof_complete copy.tex`, `proof_completes/qwn_atm_1.tex` are working notes
living next to the final document. After integrating §1.3, move them into a single `scratch/`
directory (or a separate git branch) so `main.tex`'s dependency tree is the whole story of the
repo.

---

## 2. Mathematical completeness (these are also coherence problems — the text currently claims results it doesn't prove)

### 2.1 🔴 Proof of the ℤ/pʳ case is unfinished and ends mid-sentence
`sections/RamificationAfterBlowupIsTame.tex:632-673`: the proof of
`theorem:ramification_after_blowup_is_tame_for_p_power` contains
`\textcolor{red}{Not clear how to finish here without analyzing the ramification even further.}`
and literally ends with "decompose $\cP \to U$ as:" followed by `\end{proof}`. Fix via §1.3.

### 2.2 🔴 The general abelian case is a two-line "Idea"
`sections/RamificationAfterBlowupIsTame.tex:675-677`: "Finally, **Proof of Theorem** …: Idea:
decompose G be the structure theorem, and finish by the above." The main theorem of the
chapter (`theorem:torsors_after_blowup_is_tame`) needs an actual proof: write out the
decomposition G ≅ ∏ ℤ/pᵢ^{rᵢ}, apply `prop:quotient_torsors` /
`lemma:bounding_ramification_of_contracted_product`, and check the tame/wild bookkeeping.

### 2.3 🔴 `lemma:ExtensionOfTamelyRamifiedSheaf` has a placeholder proof
`sections/GeometricCFT/ProofOfReducedTheorem.tex:42-53`: the proof body is a red note listing
two candidate routes. This lemma is the bridge from "tamely ramified along H" to "extends to a
locally constant sheaf", i.e., the final step of the whole thesis. It must be proved or
precisely cited (Guignard/Takeuchi both have versions; a precise citation with a short
deduction would be acceptable for a thesis).

### 2.4 🟡 The reduction to C = ℙ¹ is asserted, not proved
`sections/RamificationAfterBlowupIsTame.tex:427-438`: the "Invariance of Local Invariants
under Formal isomorphism" principle is stated in italics, in informal language ("we make our
life simpler"), with no proof, reference, or precise statement. This principle carries the
entire chapter (it justifies computing on 𝔸ⁿ/ℙ¹ only). Promote it to a numbered lemma with an
honest proof sketch: the completed local ring of C at P is k[[x]]; symmetric powers and
blowups commute with the formal/étale localization used; ramification at η is read off the
completed DVR. Same for "We also assume k is algebraically closed. (We can etale base change,
and this doesn't change ramification.)" — point to `lemma:descend_ramification_along_etale`.

### 2.5 🟡 Unproven claim inside the Kummer computation
`sections/RamificationAfterBlowupIsTame.tex:602`: "$Y^n − \prod f_i$ is irreducible degree n
equation for Y" — irreducibility is asserted (in the Artin–Schreier case at line 531 too).
The rank-counting argument that follows actually only needs the invariant subring computation;
if you keep the irreducibility claim, justify it (or rephrase to avoid it — you don't need the
quotient to be a domain, only to identify the invariants).

### 2.6 🟡 Uniqueness in the main theorem is never addressed
`thm:GCFT_reduced` asserts a **unique** 𝒢_d, and `thm:GCFT_torsors`
(`sections/GeometricCFT/ProofOfReducedTheorem.tex:4-7`) repeats it, but the proof only
constructs existence via the π₁ isomorphism. Uniqueness is immediate from
π₁-surjectivity/full-faithfulness of pullback — say it in one sentence.

### 2.7 🟡 Weak justification inside `lemma:takeuchi_lemma`
`sections/GeometricClassFieldTheory.tex:245-247`: "(Because it will be unramified at this
point and thus also at the generic point of V.)" — passing from unramifiedness at one closed
point to the generic point of V uses openness of the étale locus plus the fact that the
closed point specializes appropriately; one sentence with `\stackstag{...}` would fix it.

### 2.8 🟢 Leftover red TODOs
Every remaining `\textcolor{red}{…}` in included files (found at
`sections/Introduction.tex:32`, `sections/Preliminaries/Preliminaries.tex:228, 417, 487, 488,
518, 523`, `sections/GeometricCFT/ProofOfReducedTheorem.tex:47-51`,
`sections/RamificationAfterBlowupIsTame.tex:671`, `a_wrong_path/a_wrong_path.tex:234`) must be
resolved or deleted before submission. The one at `Preliminaries.tex:488` ("claude generated
at the end of the article, add it somewhere") especially should not reach a referee.

---

## 3. Duplication within the included text

- 🔴 **The affine-blowup local-ring computation appears three times, twice verbatim.**
  `sections/RamificationAfterBlowupIsTame.tex:440-460` (in the proof of the main theorem) and
  `:711-732` (in "Extending To Product of Blowups") are word-for-word identical (a third copy
  sits commented out at `:355-377`). Extract it once as a lemma/subsection ("The local ring at
  the generic point of the exceptional divisor", with the valuation-=-order-of-vanishing
  corollary) early in the chapter, and have both proofs cite it.
- 🟡 **The fiber-description of the Abel–Jacobi map appears twice**: as an unnumbered display
  in `sections/Introduction.tex:6-13` and as the theorem at
  `sections/GeometricClassFieldTheory.tex:123-132`. Fine to state twice, but the intro should
  say "see Theorem …" and the two should use the same hypotheses/notation (the theorem's cases
  say "m > 0" — should be $\mdls > 0$).
- 🟡 **Setup restated twice in Chapter 2**: the standing notation ($C$, $\mdls$, $Z_\ndls$,
  $X_\ndls$, $E_\ndls$, $\eta_\ndls$ + diagram) at `RamificationAfterBlowupIsTame.tex:1-16`
  is repeated in a big commented block at `:314-328`. Delete the dead copy.
- 🟡 **Two consecutive paragraphs saying the same thing**:
  `sections/Preliminaries/Preliminaries.tex:638-646` — "Now and for the rest of the section
  assume A is a complete discrete valuation ring …" immediately followed by "For the remainder
  of this section, assume A is a complete discrete valuation ring …" (both state the Cohen
  structure theorem). Keep the second, delete the first.
- 🟡 **Two subsections with the same title**: `sections/GeometricClassFieldTheory.tex:219` and
  `:379` are both called "Proof of Theorem …". Rename the first to "Reduction Lemmas" (it even
  has a `\subsubsection{Reduction Lemmas}` inside it — flatten that).
- 🟢 Dead commented-out blocks make the sources hard to navigate: e.g.
  `RamificationAfterBlowupIsTame.tex:237-423` (~190 lines), `Preliminaries.tex:158-176,
  254-286, 530-555`, `Introduction.tex:86-96, 124-133`, `GeometricClassFieldTheory.tex:167-173,
  360-367`. Once the live text is stable, delete them (git already remembers).

---

## 4. Coherence of the theorem chain (the "spine" of the thesis)

The logical spine is: `thm:GCFT` → `thm:GCFT_reduced` →
`theorem:SymmetricPowerOfSheafIsTamelyRamified` →
`theorem:SymmetricPowerOfSheavesIsTamelyRamifiedReduction` ≡
`theorem:torsors_after_blowup_is_tame`. Problems:

- 🔴 **The sheaf↔torsor switch is silent at the point where it matters.**
  `RamificationAfterBlowupIsTame.tex:18-22` says "Our main goal in this section is to prove
  \Cref{theorem:SymmetricPowerOfSheavesIsTamelyRamifiedReduction}:" and then states a
  *different-looking* theorem (`theorem:torsors_after_blowup_is_tame`) in torsor language,
  with no bridge. Add one sentence: "By \Cref{prop:torsor_module_equivalence}, rank-1 locally
  free Λ-module sheaves with ramification bounded by 𝔪 correspond to Λ^×-torsors with the same
  ramification bound, so the theorem above is equivalent to:". (The equivalence sentence
  currently first appears only in `ProofOfReducedTheorem.tex:3`, one chapter too late.)
- 🟡 **The `restatable` machinery is declared but never used.** All three
  `\begin{restatable}` theorems are never restated with the starred command, so they behave as
  plain theorems while confusingly re-declaring restate macros — and
  `theorem:SymmetricPowerOfSheafIsTamelyRamified` is *re-declared* as a new restatable in
  `GeometricClassFieldTheory.tex:3` (its twin also lives in the dead file
  `RamificationAfterBlowup.tex:3` — duplicate label if that file is ever re-included). Either
  actually use `\SymmetricPowerOfSheavesIsTamelyRamifiedReduction*` to restate the intro
  theorems at the top of their chapters (recommended — readers of chapter 3 shouldn't have to
  flip back), or drop `restatable` for plain `theorem`.
- 🟡 **Two near-identical theorem names.**
  `theorem:SymmetricPowerOfSheafIsTamelyRamified` vs
  `theorem:SymmetricPowerOfSheavesIsTamelyRamifiedReduction` differ by "Sheaf/Sheaves" and a
  trailing "Reduction" — very easy to confuse in `\Cref`s and while reading. Consider
  `thm:sym-power-tame-global` (all of H, large d) vs `thm:sym-power-tame-local` (single-point
  modulus, exceptional divisor of one blowup), or similar names carrying the distinction.
- 🟡 **"Chapter 2 proves X" vs what Chapter 2 proves.** The roadmap says Chapter 2 proves the
  *Reduction* theorem plus corollaries "instrumental in the proof" — but the key corollaries
  (`cor:tame-ramification-symmetric-product`, `lemma:moduli_reduction`) actually live in
  Chapter 3 (`GeometricClassFieldTheory.tex`). Either move `subsection:ram_prod_analysis` +
  those lemmas into one place or update the roadmap.
- 🟢 The chapter-2 strategy paragraph (`RamificationAfterBlowupIsTame.tex:24-29`) promises
  "First … cyclic case G=ℤ/pℤ and groups with gcd(|G|,p)=1" but the first theorem proved
  (`:465`) covers "tamely ramified" + "totally ramified with G=ℤ/pℤ" — align the promise with
  the delivery.

---

## 5. Section-by-section notes

### Abstract (`main.tex:33-39`)
- 🟡 Uses $\cF^{[\deg\mdls]}$, $\mdls$, $E_\mdls$ with no definitions; an abstract should be
  readable standalone. Suggested shape: "Let C be a smooth projective curve over a perfect
  field, 𝔪 an effective divisor (modulus), U = C∖𝔪. For a rank-1 local system ℱ on U with
  ramification bounded by 𝔪, we show by an explicit, elementary computation that the symmetric
  power ℱ^{[deg 𝔪]} is at most tamely ramified at the generic point of the exceptional divisor
  of the blowup of C^{(deg 𝔪)} at 𝔪…".
- 🟢 "local system $\cF$ on a curve $C\setminus\mdls$" — C∖𝔪 is not a curve of the advertised
  type; phrase as "on the complement of 𝔪 in a curve C".

### Introduction (`sections/Introduction.tex`)
- 🟡 The opening (lines 1–2) is abrupt: sentence 1 announces an "elementary proof of a certain
  imporant geometric theorem" before any context; sentence 2 dumps notation. Consider opening
  with 2–3 sentences on what class field theory / GCFT says (you have exactly this at lines
  51-53 — move it up front), then introduce Deligne's approach, then the notation.
- 🟡 Setup is stated twice: lines 2 ("We (usually) work over a perfect field k…") and 51 ("Let
  k be a perfect field, and let C be…"). Keep one, at the point where the formal statements
  begin.
- 🟡 Line 3: "descends via the Abel-Jacobi $\Phi: U \to \PicCm[]$ to $\PicCm[]$" — repetitive;
  and Φ, Pic, "modulus", "ramification bounded by 𝔪" are all used before being defined (they
  get defined at lines 54-57). Fine for an intro, but add "(precise definitions below)" or
  reorder.
- 🟡 Line 32: red TODO "[incorporate \cite{Rabinoff2014Witt} here]".
- 🟡 Line 49 is one long sentence carrying three theorem references; split.
- 🟢 The footnote at 62-65 (multiplicative sheaves) is doing a lot of work for a footnote —
  consider promoting to a remark, since "multiplicative" is the key hypothesis of the main
  theorem.
- 🟢 Line 104: "Let $\ndls = n_i P_i \subset \mdls$ be a sub modulus" — say explicitly
  "supported at a single point $P_i$"; that's the point of the reduction.
- 🟢 Acknowledgements ("Acknowledgemets", line 118) should probably be its own unnumbered
  section/page in a thesis, not a paragraph of the introduction.

### Preliminaries (`sections/Preliminaries/Preliminaries.tex`)
- 🔴 Line 9-11: `\subsection{Scheme Quotients in general}` has placeholder body "basic
  definitions, categorail qoutient, when it exists, etc, properties, universal properties,
  etc... prop 14 beolw". Write it or delete the subsection (the SGA1 material in "Symmetric
  Powers of Schemes and Torsors" already covers what's used).
- 🟡 **Audit which preliminaries are actually used.** The "Quotient of Torsors Towers"
  subsection (lines 451-555, incl. `prop:torsor_tower_diagram`) is used only by the Wrong-Path
  appendix material; if that becomes an appendix, consider moving this subsection to the
  appendix too — it's the heaviest part of the chapter and a reader will expect it to be used
  in the main proofs.
- 🟡 Line 141-145 (`theorem:torsors_are_realized_as_spaces`): missing period after
  "$X_{\text{\'Et}}$", and the second sentence ("Similarly, the morphism sending Y to
  Hom_X(−,Y) to the category of G-torsors on X_ét is an equivalence") is garbled. Also state
  the hypothesis (G affine/finite over X) inside the theorem, not only in the section
  preamble.
- 🟡 Line 147-152 (corollary): last sentence "And every G-torsor, in each of the above sites
  can be realized as a scheme, which is a prinicipal G-bundle" — grammar and it partially
  restates the theorem. Tighten.
- 🟡 Line 288-296: the intro to symmetric powers says "the difference being that we ask Γ to
  act on the left", but every definition/proposition that follows uses **right** actions
  (lines 302, 318, 329, 364). Resolve the left/right story once — this left/right/inverse
  juggling recurs at 411 ("letting the S_d-action be a left action (via the inverse)") and is
  a real comprehension hazard in the Ξ = K_G ⋊ S_d computations later.
- 🟡 Lines 479-488: the four quotient schemes are defined and then the two identifications are
  justified only inside a red note. Turn the red note's content (preimage of K_{G/H} under
  G^d ↠ (G/H)^d equals H^d + K_G) into a displayed lemma with a two-line proof.
- 🟡 Line 411-421: the paragraph deriving Ξ = K_G ⋊ S_d contains a red note "explain why the
  qoutineing by the double qoutient exists" — this existence (admissibility of the Ξ-action)
  is needed for `cor:sym-power-quotient` to make sense; add the one-line argument
  (Ξ acts through finite group on a scheme covered by invariant affines, by the same SGA1
  criteria already quoted).
- 🟡 The section header promise (lines 1-7) says "We focus specifically on the theory of
  G-torsors … Subsequently … ramification theory … Finally … algebraic geometric remarks" —
  matches, good — but "Scheme Quotients in general" (empty) is promised nowhere; see above.
- 🟢 Line 71: "where $\mathcal{G}$ acts on $T$-points by" — $T$ never introduced; say "on
  sections".
- 🟢 Line 107-111: notation drift — `$(\mathcal{G}\mathcal{E})/\cX$`, `$\mathcal{G}(\mathcal{E}/\cX)$`,
  `$\mathbf{Tors}(\cX,\cG)$`, `$\cG \cE_{/\cX}$` in four lines; also switches between $G$ and
  $\cG$. Pick one slice notation.
- 🟢 Line 232: double label `\label{prop:quotient_torsors_finite}\label{prop:quotient_torsors}`
  — keep one, `sed` the references.
- 🟢 Lines 766-780: in the finite-flat-image theorem, "$f(Z) \subset X$ is a prime divisor"
  should be "$\subset Y$".
- 🟢 Lines 789-809: the proof is nested *inside* the theorem environment (also
  `lemma:takeuchi_lemma` in GCFT, lines 242-251). Move `\begin{proof}` after `\end{theorem}`
  so theorem bodies are italicized correctly and the proof-end square sits right.
- 🟢 Line 844: `$\left( k[[t_1,\dots,t_d]]\right)^{S^d}$` — superscript should be $S_d$; line
  845 "elementary symmetric power series" → "elementary symmetric polynomials".
- 🟢 Line 697/703: `\Cite{serreLF}` (capital C) — works only by accident if defined; use
  `\cite`.
- 🟢 Line 733: the ramification-index formula is typeset garbled:
  `$\frac{n}{|gcd(v_K(a)|, n)}$` — should be $n/\gcd(v_K(a), n)$ with `\gcd`.
- 🟢 The Galois base-change lemma (lines 850-887) is filed under "Algebraic Geometry" but is
  pure field theory used only in the appendix — move it next to the ramification material (or
  to the appendix, per the audit above).

### Ramification After Blowup Is Tame (`sections/RamificationAfterBlowupIsTame.tex`)
- 🟡 Line 429-438: rewrite the reduction paragraph formally (see §2.4). Replace "We argue its
  enough", "make our life simpler", "So in what follows" with a numbered reduction lemma and a
  proof.
- 🟡 Line 437: "$\bG_m = U \subset U' = C\setminus\mdls$" — here $U'$ is a *bigger open of the
  curve*, but 100 lines earlier (line 154-176) $U'$ denoted the *total space of the torsor*.
  Rename one of them (e.g. use $V = C\setminus\{0\}$ for the curve open).
- 🟡 Line 440 onwards: the blowup analysis is written for $\mathbb{A}^n$ with variables
  $x_1,\dots,x_n$, then the application uses $d$; and the theorem at line 466 sets
  $\mdls = d\cdot 0$ so $d = \deg\mdls$, while elsewhere in the thesis $d$ is the *large*
  symmetric-power degree and $\deg\mdls$ is separate. Within this chapter, use one letter for
  the blowup dimension (= deg 𝔫) and never reuse $d$ for anything else; reserve $d$ for the
  large degree of Chapter 3.
- 🟡 Line 465-476: the first main computation theorem is **unlabeled** (it's later invoked as
  "the previous theorem", lines 648, 665) — label it, and rephrase the statement: currently
  "the ramification … at $\eta_\mdls$ … is tamely ramified / unramified" (a ramification isn't
  ramified; the torsor is). Also "ramificaiton" typo, and hypothesis 2 should say *wildly*
  or "totally ramified with ramification bounded by $d$" consistently with the corollary at
  line 624.
- 🟡 Line 496 (`eq:complete_field_at_generic_point`):
  `$\hat K = k(\frac{e_1}{e_d},\dots,\frac{e_{d-1}}{u_d})((e_d))$` — the $u_d$ should be
  $e_d$. Same equation appears correctly nowhere else, and it's the equation the two case
  analyses cite. Also line 491: `[[s_d]]` should be `[[e_d]]`.
- 🟡 Line 501: Artin–Schreier written `$X^p + X - f$` here but `$X^p - X$` everywhere else
  (line 508, 513, `theorem:artin_schreier_ramification`) — sign consistency.
- 🟡 Line 574-575: the conclusion of the Artin–Schreier case, "(that $\cP$ is unramified at
  the generic point…)", should be $\cP^{[d]}$; and the sentence "we get by
  \Cref{eq…} and \Cref{theorem:artin_schreier_ramification} the result" hides the actual final
  step — spell out: the datum $\sum f(x_i)$ lies in the residue field
  $k(e_1/e_d,\dots)$ ⊂ ring of integers, valuation ≥ 0, so by the theorem case (1)/(2) the
  extension is unramified. Same at line 619-620 for the Kummer case ($\cP$ → $\cP^{[d]}$, and
  say what $v(\tilde F)$ is and why tameness follows).
- 🟡 Line 654-655: two names for the same object, back to back: "Let $\ndls' = \pi^{-1}(\ndls)$
  … Let $\tilde\ndls$ be the pullback of $\ndls$ to $C'$." Neither is used afterwards. Delete
  both or use one.
- 🟡 Line 680-799 ("Extending To Product of Blowups"): `prop:ramification-external-product` is
  stated, then the proof is delivered as free-flowing subsubsections ("The Affine Case", "The
  Product Case", "Comparison of Blowups", "Extensions of DVRs", "Ramification of G-Torsors")
  ending with the fragment "And we finish by \Cref{lemma:bounding_ramification_of_contracted_product}."
  Wrap the whole thing in `\begin{proof}[Proof of \Cref{prop:ramification-external-product}]`
  … `\end{proof}` (minus the duplicated affine computation, per §3), so the reader knows when
  the proposition is discharged.
- 🟢 Line 26: "$\gcd(|G|, p) = 1$" — at this point $p$ hasn't been introduced in the chapter
  (it's char k); say "p = char k > 0" in the chapter preamble at line 2.
- 🟢 Line 549-553: the inner lemma is stated for "$\alpha \in k(e_1/e_d,\dots,e_{d-1}/e_d)$"
  but the proof shows more precisely that α is a *polynomial* in the $e_k(y) = e_{d-k}(x)/e_d(x)$;
  stating the sharper conclusion makes the "valuation ≥ 0" step in the application transparent.

### Geometric Class Field Theory (`sections/GeometricClassFieldTheory.tex`)
- 🟡 Line 13: subsection titled "Etale Fundamental Groups and Tame Fundamental Groups" — tame
  fundamental groups never appear (the tameness material is commented out). Retitle or add the
  intended remark; note the Proof-of-Reduced-Theorem chapter *does* need a tame-π₁ statement
  for `lemma:ExtensionOfTamelyRamifiedSheaf`, so this may be exactly where that missing
  ingredient should live.
- 🟡 Lines 160 and 381: "$\mdls = \sum_{i=1}^n k_P P$ with $\deg P = d_P$" — the sum index is
  $i$ but the summands are indexed by $P$; earlier chapters write $\mdls = \sum n_i P_i$.
  Unify (and note $n$ is also used for #points here while being a Kummer degree elsewhere).
- 🟡 Line 154: "the fibers of Φ_d are affine spaces (of the same degree)" — dimension, not
  degree; and "This hint that a solution … is to compactify the morphism to yield projective
  fibers" — grammar, and the real motivation (homotopy exact sequence needs properness) is
  worth one explicit sentence, echoing the intro.
- 🟡 Lines 259-273: the paragraph "Following from this, we look at the following diagram,
  coming from the flat base change $C^{(d-\deg\mdls)} \to \Spec(k)$ …" is hard to parse — the
  base change is *along the projection* $C^{(\deg\mdls)} \times C^{(d-\deg\mdls)} \to C^{(\deg\mdls)}$
  (flat since $C^{(d-\deg\mdls)} \to \Spec k$ is flat). Rewrite naming the map. Also
  "Hence it is well defined question … to ask whether" — grammar.
- 🟡 Lines 286-308: this run of prose between the lemmas does the real work of
  `cor:tame-ramification-symmetric-product` but lives outside any proof environment, and the
  corollary's proof then says "follows from the preceding discussion". Restructure: state the
  corollary first, put the discussion inside its proof.
- 🟡 Line 297: `\boxP{...}{...}` (box-product of torsors) is used without ever being defined
  in the text — define it where the external product is first used (or in Preliminaries next
  to `prop:symmetric_powers_on_curves`).
- 🟡 Line 321-357 (proof of `cor:tame-ramification-symmetric-product`): the statement is about
  $\cP$ but the proof of the wrapping theorem (line 380-385) applies it to $\cF$ — with the
  sheaf/torsor bridge made explicit once (see §4), pick one language for the whole chapter;
  currently the chapter statement (`theorem:SymmetricPowerOfSheafIsTamelyRamified`) is about
  $\cF$, all lemmas are about $\cP$, and the final proof silently mixes them.
- 🟢 Line 6: defines $H = \tilde C^{(d)}_\mdls \setminus U^{(d)}$ — $H$ collides with the
  subgroup $H \subseteq G$ used heavily elsewhere. Consider $\partial$ or $B$ (boundary).
- 🟢 Lines 178, 187, 214, 327, 336, 347: the arrow label "c.i" is never explained — say
  "closed immersion" once or drop the label.
- 🟢 Line 151: the purple-arrow convention "(the purple arrow emphasizes that the morphism is
  of sheaves on the étale site)" is nice; move the explanation to the *first* purple diagram
  and reuse silently after.
- 🟢 Lines 363, 372: "tamely tamified" → "tamely ramified".
- 🟢 Line 123: theorem unlabeled and its proof is only a citation — fine, but format as
  `\begin{proof} See \cite{...} Propositions 3.13–3.14. \end{proof}` (currently ends with a
  colon and an empty line).

### Proof of the Reduced Theorem (`sections/GeometricCFT/ProofOfReducedTheorem.tex`)
- 🟡 The `\section` heading lives in `main.tex:60` while every other chapter carries its own
  heading — move it into the file, and (per §1.1) demote to a subsection of the GCFT chapter.
- 🟡 Line 10-21, Case 𝔪 = 0: this case isn't really a case of `thm:GCFT_reduced` as stated
  (the theorem fixes a modulus and bounds ramification by it) — clarify that 𝔪 = 0 means ℱ is
  unramified, i.e., $\cF^{[d]}$ extends to $C^{(d)}$, and note $U^{(d)} = C^{(d)}$ then. Also
  π₁'s need base points (suppressed silently — one remark suffices).
- 🟡 Line 30-38: switches to $\cF$ after setting up the torsor statement `thm:GCFT_torsors`;
  and "by the isomorphism of etale fundamental groups above, corresponds to a unique locally
  constant sheaf" — this is where uniqueness should be stated properly (§2.6).
- 🔴 Lines 42-53: the placeholder proof (§2.3).

### A Wrong Path (`a_wrong_path/a_wrong_path.tex`)
This is the best-written part of the thesis — the R1/R2 reductions, the inertia-injection
lemma, and the two absorption examples are clear and well-motivated. Remaining points:
- 🟡 As organized now it comes *after* the proof of the main theorem, but it explains
  difficulties with a theorem from two chapters earlier. As an appendix (§1.1), open with one
  paragraph placing it: "Chapter 3 proved Theorem X directly. A more natural-looking route is
  induction on r via the torsor tower; here we document precisely why that fails."
- 🟡 Line 105-115: the theorem is unlabeled and (H3) is listed as a hypothesis although it's a
  standing assumption ("G is cyclic of prime power order") — restructure as "Assume G = ℤ/pʳℤ.
  Suppose (H1) and (H2). Then …" so the counterexample's "all of (H1)–(H3) hold" reads
  cleanly.
- 🟡 Line 234: red note "Put in other words: The base change $K_{C'}/F$ is wildly ramified, so
  the inertia comparison is not onto." — that's a good summary sentence; promote it into the
  text (end of the paragraph above it) and remove the red.
- 🟢 Line 13: "ramification strictly bounded by d … (i.e. < d) … (i.e. the higher
  d'th-ramification group … is trivial)" — two parentheticals for one definition; also
  "strictly bounded" isn't defined in `definition:local_ramification_boundness` (which defines
  non-strict bounds). Add the strict variant to the definition and cite it.
- 🟢 The setup (lines 8-54) restates the four quotient schemes and Cartesian square from
  Preliminaries — as an appendix this repetition is defensible, but trim to a reminder +
  `\Cref`.

---

## 6. Notation consistency (cross-cutting)

| Issue | Where |
|---|---|
| $d$ = large degree vs $d$ = deg 𝔫 = blowup dimension vs $n$ = blowup dimension | Ch. 2 uses all three; Ch. 3 uses $d$ = large. Fix per §5 notes |
| $U'$ = torsor total space vs $U'$ = larger curve open | `RamificationAfterBlowupIsTame.tex:154` vs `:437` |
| $H$ = subgroup of $G$ vs $H$ = boundary divisor | `GeometricClassFieldTheory.tex:6` vs everywhere |
| $n$ = Kummer degree, #points in 𝔪, blowup dim | pick distinct letters |
| $\mdls$ vs $m$ in the fibers display | `GeometricClassFieldTheory.tex:127-128`, `Introduction.tex:9-10` |
| $\tilde C^{(d)}_\mdls$ written out vs `\Cmod{d}` macro | intro + ProofOfReducedTheorem write it out; GCFT uses the macro — use the macro everywhere |
| Frac / $\Frac$, max / $\max$, gcd / $\gcd$ as text vs operators | e.g. `RamificationAfterBlowupIsTame.tex:128, 125`, `Preliminaries.tex:733` |
| "étale/Etale/etale/\'etale" and $X_{\text{ét}}$ vs $X_{\text{Ét}}$ vs $U_{et}$ | e.g. `GeometricClassFieldTheory.tex:301` uses $U_{et}$; standardize small/big site notation once in Preliminaries |
| Left vs right group actions (Γ, S_d, inverse-twists) | see Preliminaries note §5 |
| $q$ = quotient map `cor:sym-power-quotient` and $q$ also used for other maps | audit |

---

## 7. Spelling and grammar catalogue (🟢, but there are many — worth one dedicated pass)

Recurring misspellings (grep-able): `qoutient`/`qoutineing` (many), `extesntion`/`exntesion`/
`extesntions`, `invaraint`/`Invaraince`, `equivilant`/`equiviliant`/`equivlantly`/`Equivantly`,
`prinicipal`, `otherhand`, `similiar`/`similiary`, `Conversly`, `cosntant`, `shuffeling`,
`sesction`, `condlude`, `projecive`, `corrsponding`, `deonte`, `seprable`, `ramificaiton`,
`excptional`, `algebraicly`, `continious`, `morphsm`, `orginial`, `defintion`, `opeartor`,
`throughtout`, `imporant`, `occuring`, `Acknowledgemets`, `necessarily material` (→ necessary),
`tamely tamified` (×2), `beolw`, `categorail`, `Guingard` (→ Guignard),
`Incoporating`, `sume auxilary` (→ some auxiliary), `Y^P` (→ $Y^p$,
`RamificationAfterBlowupIsTame.tex:531`), `t_d^{±1}` (→ $x_d$, `:617`), "if X be a connected
scheme" (`Preliminaries.tex:189`), "acts … simply transitively" as adjective
(`Preliminaries.tex:34`), "is trivial torsor"-style missing articles in several proofs.

Also: many sentences begin with "And"/"So,"/"Where"/"Which" as fragments (e.g.
`Preliminaries.tex:90`, `Introduction.tex:13`, `RamificationAfterBlowupIsTame.tex:434, 608-611`);
capitalized mid-sentence words after commas ("Such that", `RamificationAfterBlowupIsTame.tex:124`;
"The point θ defined in the Corollary", `GeometricClassFieldTheory.tex:351`). A grammar pass
with a LaTeX-aware checker (or reading each chapter aloud) is warranted before submission.

---

## 8. LaTeX / build mechanics

- 🟡 `main.tex:21-22`: both `\bibliography{Bib}` and `\addbibresource{Bib.bib}` — with biblatex
  only `\addbibresource` is right; delete line 21.
- 🟡 Duplicate labels to fix: `sec:master` (§1.2), `prop:quotient_torsors_finite`/`prop:quotient_torsors`
  (same object, `Preliminaries.tex:232`), and the latent `theorem:SymmetricPowerOfSheafIsTamelyRamified`
  duplication if `RamificationAfterBlowup.tex` is ever re-included.
- 🟡 `main.tex:8-10`: "%%%% this is incharge of spacing between paragraphs.... fix later" —
  decide the parskip/parindent style (a thesis usually uses parindent with no parskip) and
  remove the note.
- 🟢 `main.tex:24-25`: boolean `ThesisIntro` is set and (apparently) never tested — delete or
  use.
- 🟢 Title page: `\date{\today}` and no institution/advisor/degree frontmatter — check your
  department's thesis template requirements (title page, declaration, Hebrew abstract if HUJI,
  etc.).
- 🟢 Mixed diagram packages: `xymatrix` (`Preliminaries.tex:817`,
  `RamificationAfterBlowupIsTame.tex:37`) alongside `tikz-cd` everywhere else — port the two
  xymatrix squares to tikz-cd.
- 🟢 Some proofs end in displayed equations without `\qedhere`, pushing the QED box to an empty
  line (e.g. `Preliminaries.tex:592`, `a_wrong_path.tex` lemma proof).
- 🟢 Footnote duplication: the "Equivantly, the sum is obtained as the contracted product …
  along the multiplication map" footnote appears twice (`Preliminaries.tex:74-76` and
  `:380-382`) — second occurrence can reference the first.
- 🟢 `sorting=ynt` with `style=alphabetic` is unusual (alphabetic labels but year-name-title
  ordering); consider `sorting=nyt` or the default.

---

## 9. Suggested order of attack

1. Integrate the completed ℤ/pʳ proof (§1.3, §2.1) and write the general-abelian deduction
   (§2.2) — the thesis is unfinished without these.
2. Prove or properly cite `lemma:ExtensionOfTamelyRamifiedSheaf` (§2.3).
3. Restructure per §1.1–1.2 (drop `proof_complete.tex`, make A Wrong Path an appendix, fold
   the reduced-theorem proof into the GCFT chapter, fix the roadmap).
4. De-duplicate (§3) and fix the theorem-chain bridges and names (§4).
5. Formalize the ℙ¹/formal-invariance reduction (§2.4) and the smaller math gaps (§2.5–2.7).
6. Notation pass (§6), then language pass (§7), then build mechanics (§8).
