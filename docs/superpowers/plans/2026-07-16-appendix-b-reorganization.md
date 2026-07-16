# Appendix B Reorganization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rename and reorganize Appendix B around the attempted induction from the degree-$p$ Artin--Schreier calculation, show exactly what the two induction inputs contribute in the valuation tower, and end with a local wild-base-change example explaining why the inference does not close.

**Architecture:** Preserve the existing quotient-tower proposition, base-change lemma, field dictionary, valuation diagrams, and inertia lemma, but reorder them into a five-section narrative. Add a forward reference at the transition from Case (2) to Case (3) in Chapter 2, retain the existing Appendix B label as a compatibility alias, and update the already-reorganized Introduction without disturbing the user’s Appendix A edits.

**Tech Stack:** LaTeX (`report`, `tikz-cd`, `cleveref`, `biblatex`), `latexmk`, Poppler (`pdfinfo`, `pdftoppm`).

## Global Constraints

- Use the title `A Failure of an Artin--Schreier Induction Strategy`.
- State that the appendix diagnoses failure of an induction inference, not failure of the theorem proved in Chapter 2.
- Do not claim that the explicit local absorption example is itself realized by a particular symmetric-power comparison map `q`.
- Preserve existing mathematical labels when their content survives, including `prop:torsor_tower_diagram`, `lem:galois-base-change`, `lem:inertia-injection`, `ex:p2-counterexample`, and `ex:absorption-explicit`.
- Preserve the user’s uncommitted Appendix A reorganization in `witt/` and the corresponding Introduction entry.
- Do not modify generated LaTeX files except through the normal compilation command.

---

### Task 1: Rename Appendix B and add reader navigation

**Files:**
- Modify: `main.tex:72`
- Modify: `sections/Introduction.tex:119`
- Modify: `sections/RamificationAfterBlowupPPower.tex:1-7`

**Interfaces:**
- Consumes: Existing compatibility label `section:a_wrong_path`.
- Produces: New semantic label `appendix:artin_schreier_induction_failure` used by Chapter 2 and the Introduction.

- [ ] **Step 1: Rename the chapter while preserving its old label**

Use:

```tex
\chapter{A Failure of an Artin--Schreier Induction Strategy}
\label{appendix:artin_schreier_induction_failure}
\label{section:a_wrong_path}
```

- [ ] **Step 2: Update only the Appendix B entry in the Introduction**

Keep the user’s new Appendix A entry unchanged and replace the Appendix B item with:

```tex
\item[Appendix B] \emph{A Failure of an Artin--Schreier Induction Strategy} examines the tempting attempt to deduce the cyclic $p$-power calculation inductively from the degree-$p$ Artin--Schreier case, and explains how wild base change obstructs that argument.
```

- [ ] **Step 3: Add the forward reference at the start of Case (3)**

Immediately after the `Case (3): Artin--Schreier--Witt` heading, insert:

```tex
A natural alternative to the direct calculation below would be to filter a
cyclic $p$-power torsor by its degree-$p$ layers and try to apply the
Artin--Schreier calculation inductively. In
\Cref{appendix:artin_schreier_induction_failure} we examine this approach and
explain why the two expected induction inputs do not by themselves control
ramification before the intervening wild base change.
```

- [ ] **Step 4: Verify navigation text mechanically**

Run:

```bash
rg -n 'A Failure of an Artin|appendix:artin_schreier_induction_failure|Appendix B' main.tex sections/Introduction.tex sections/RamificationAfterBlowupPPower.tex
```

Expected: the title appears in `main.tex` and the Introduction, and the new label appears once at its definition and once in the Chapter 2 reference.

---

### Task 2: Reorganize Appendix B into the approved five-section narrative

**Files:**
- Modify: `a_wrong_path/a_wrong_path.tex:1-550`

**Interfaces:**
- Consumes: Chapter 2 cases `theorem:cyclic_cases_after_blowup(2)` and `(3)`, plus the existing symmetric-power and quotient-torsor results.
- Produces: Five top-level sections in the order motivation, preliminaries, valuation-tower attempt, wild-base-change failure, and precise takeaway.

- [ ] **Step 1: Replace the three-line opening with the motivation section**

Use the heading:

```tex
\section{Motivation: can the Artin--Schreier calculation be iterated?}
\label{sec:as_induction_motivation}
```

The opening must explicitly set

```tex
G=\Z/p^r\Z,\qquad
H=p^{r-1}G\cong\Z/p\Z,\qquad
G/H\cong\Z/p^{r-1}\Z,
```

factor `\cP\to\cP/H\to U`, and present the three intended moves: induction on the quotient, the degree-$p$ calculation on the top layer after passage to `C'`, and recombination. End by previewing that the second conclusion is measured only after a potentially wild base change.

- [ ] **Step 2: Consolidate all definitions into one preliminaries section**

Use:

```tex
\section{Preliminaries for the attempted induction}
\label{sec:as_induction_preliminaries}
```

Within it, use the following subsections in this order:

```tex
\subsection{The symmetric quotient tower}
\subsection{The geometric boundary and its valuations}
\subsection{The master diagram}
\subsection{The proposed induction step}
\subsection{A base-change lemma}
```

Move the existing summation-kernel definitions, four quotient schemes, `prop:torsor_tower_diagram`, and its proof into the first subsection. Keep the non-normality remark but shorten its final takeaway to: the comparison map `q` is not one of the constant-group torsors to which the induction hypotheses apply.

Move the current setup, compactification, blowup, and DVR definitions into the second subsection. Display the master diagram only in the third subsection; delete the repeated smaller copy from the old setup block.

- [ ] **Step 3: Restate the false target as a proposed implication, not a theorem**

Use a displayed `description` or `enumerate` block headed `Proposed induction step`, with:

```tex
\item[\textnormal{(IH$_{r-1}$)}]
$(\cP/H)^{[d]}\to U^{(d)}$ is unramified at $\eta_C$;
\item[\textnormal{(AS)}]
$\cP^{[d]_H}\to(\cP/H)^{(d)}$ is unramified at $\eta_{C'}$.
```

Ask whether these statements imply that `\cP^{[d]_G}\to U^{(d)}` is unramified at `\eta_C`. Do not use a theorem environment. Retain the base-change lemma and proof immediately afterward because it is the algebraic tool used in the next section.

- [ ] **Step 4: Build the valuation-tower section around the contributions of the hypotheses**

Use:

```tex
\section{Following the hypotheses through the valuation tower}
\label{sec:as_induction_valuation_tower}
```

Move the connectedness and `H\ne0` reductions here. Then retain the existing field dictionary

```tex
K_C,\qquad F,\qquad E,\qquad K_{C'},\qquad E\cdot K_{C'}
```

and both tower diagrams. Immediately after them add a four-row display or description explaining:

```tex
\text{(IH$_{r-1}$)}\Rightarrow F/K_C\text{ unramified at }V_C,
```

```tex
\text{(AS)}\Rightarrow E\cdot K_{C'}/K_{C'}
\text{ unramified at }V_{C'},
```

```tex
\text{missing step: }E/F\text{ unramified at }V_F,
```

```tex
\text{goal: }E/K_C\text{ unramified at }V_C.
```

Retain `lem:inertia-injection` and its proof, but introduce it at the precise point where the comparison

```tex
I(v_\star\mid V_{C'})\hookrightarrow I(v_E\mid V_F)
```

is needed. Conclude the section by saying that (AS) kills only the source and that surjectivity is the missing assertion.

- [ ] **Step 5: Replace the two examples with one explicit wild-absorption example**

Use:

```tex
\section{Failure under wild base change}
\label{sec:as_induction_wild_base_change}
```

Create one example carrying both compatibility labels:

```tex
\begin{example}[Absorption of an Artin--Schreier layer]
\label{ex:p2-counterexample}
\label{ex:absorption-explicit}
```

Retain the explicit fields

```tex
k=\bar{\F}_p,\qquad F=k((t)),\qquad K=k((\pi)),
\qquad t=\frac{\pi^p}{1-\pi^{p-1}},
```

and

```tex
E=F(y),\qquad y^p-y=t^{-1}.
```

Show that `E/F` has break one, whereas

```tex
t^{-1}=\pi^{-p}-\pi^{-1}=\wp(\pi^{-1})
```

makes `E\cdot K/K` trivial. Translate this as

```tex
1=I(EK/K)\hookrightarrow I(E/F)=\Z/p\Z.
```

State explicitly that the example disproves the general local inference used by the proposed induction step; it does not assert that this `K/F` is produced by `q` for a particular global torsor.

- [ ] **Step 6: End with a scope-controlled conclusion**

Use:

```tex
\section{What the example proves}
\label{sec:as_induction_takeaway}
```

The conclusion must say:

1. Chapter 2’s Artin--Schreier--Witt theorem remains true;
2. the quotient induction hypothesis controls the lower field extension;
3. the degree-$p$ calculation controls the top layer only after base change;
4. wild base change may absorb the original ramification;
5. additional geometric control of `K_{C'}/F` would be needed to repair the induction;
6. the direct Witt-vector calculation avoids this missing descent step.

- [ ] **Step 7: Verify the source hierarchy and labels**

Run:

```bash
rg -n '^\\(section|subsection)\{|prop:torsor_tower_diagram|lem:galois-base-change|lem:inertia-injection|ex:p2-counterexample|ex:absorption-explicit' a_wrong_path/a_wrong_path.tex
```

Expected: exactly five top-level sections in the approved order; each preserved label appears exactly once.

---

### Task 3: Compile and verify the reorganized appendix

**Files:**
- Verify: `main.pdf`
- Verify: `main.toc`
- Create temporarily: `tmp/pdfs/appendix_b_review/*.png`

**Interfaces:**
- Consumes: The reorganized LaTeX sources from Tasks 1–2.
- Produces: A compiling thesis with a visually verified Appendix B and accurate navigation.

- [ ] **Step 1: Run static checks before compilation**

Run:

```bash
git diff --check
rg -n 'A Wrong Path|Difficulties in Proving the Theorem|Unramifiedness of .*eta_C' main.tex sections/Introduction.tex a_wrong_path/a_wrong_path.tex
```

Expected: no whitespace errors and no stale reader-facing Appendix B title or old section headings.

- [ ] **Step 2: Compile the complete thesis**

Run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Expected: exit status 0.

- [ ] **Step 3: Check references and the table of contents**

Run:

```bash
rg -n 'undefined references|multiply defined|LaTeX Warning: Reference' main.log
rg -n 'appendix.B|section.B\.' main.toc
```

Expected: no undefined or multiply defined references; Appendix B has the new title and exactly five sections in the approved order.

- [ ] **Step 4: Render all Appendix B pages**

Use Poppler to determine the document length, locate the first physical page containing the new Appendix B title, and render through the end of the thesis:

```bash
pages=$(pdfinfo main.pdf | awk '/^Pages:/ {print $2}')
first=$(for n in $(seq 1 "$pages"); do pdftotext -f "$n" -l "$n" main.pdf - 2>/dev/null | rg -q 'A Failure of an Artin' && { echo "$n"; break; }; done)
mkdir -p tmp/pdfs/appendix_b_review
pdftoppm -f "$first" -l "$pages" -png -r 144 main.pdf tmp/pdfs/appendix_b_review/page
```

Expected: one PNG per Appendix B page.

- [ ] **Step 5: Inspect every rendered page**

Check all PNGs for clipped or overflowing diagrams, broken headings, isolated section titles, malformed cross-references, unreadable table content, and inconsistent spacing. If any defect is found, correct the source, recompile, and re-render the affected pages.

- [ ] **Step 6: Review the final scoped diff**

Run:

```bash
git diff --check
git diff -- main.tex sections/Introduction.tex sections/RamificationAfterBlowupPPower.tex a_wrong_path/a_wrong_path.tex
```

Expected: only the approved title, navigation, structural, and explanatory changes; the user’s Appendix A edits remain intact.
