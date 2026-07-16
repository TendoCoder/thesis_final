# Appendix A Torsor and Schmid--Witt Placement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align the concrete étale-torsor statements for Kummer, Artin--Schreier, and Artin--Schreier--Witt theory while moving the Schmid--Witt reference discussion to its theorem in Chapter 2.

**Architecture:** Preserve the abstract common construction in Appendix A.1, verify the two classical coordinate equations together after they have been introduced in A.2, and retain the technically dependent ASW coordinate lemma in A.4.2 after Witt-vector algebra. Move explanatory material, rather than duplicating it, from Appendix A to the Chapter 2 theorem and realization lemma that supply its context.

**Tech Stack:** LaTeX (`report`, `cleveref`, `biblatex`), `latexmk`, Poppler PDF inspection tools.

## Global Constraints

- Preserve all existing thesis-source changes already present in the working tree.
- Keep `lemma:asw_etale_torsor` because compiled Chapter 2 arguments cite its finite-free basis and étaleness conclusions.
- Remove `appendix:schmid_witt_reference` only after confirming that no compiled source still cites it.
- Do not introduce Witt-vector coordinate notation before Appendix A.3.
- Do not commit thesis-source edits unless the user explicitly requests a commit.

---

### Task 1: Add the classical torsor lemma and connect it to the ASW analogue

**Files:**
- Modify: `witt/WittVectorAlgebraAppendix.tex`, after the proof of `theorem:artin_schreier_ramification`
- Modify: `witt/WittVectorPrerequisites.tex`, immediately before `lemma:asw_etale_torsor`

**Interfaces:**
- Consumes: the abstract pullback construction in Appendix A.1 and the Kummer and Artin--Schreier equations introduced in A.2.
- Produces: `lemma:classical_cyclic_equations_etale_torsors`, a comparison target for `lemma:asw_etale_torsor`.

- [ ] **Step 1: Confirm that the new label does not exist**

Run:

```bash
rg -n "lemma:classical_cyclic_equations_etale_torsors" --glob '*.tex'
```

Expected: no matches.

- [ ] **Step 2: Add the two-part classical torsor lemma**

Insert the following after the Artin--Schreier ramification proof and before `\section{Witt-vector algebra}`:

```tex
\begin{lemma}[Classical cyclic equations are \'etale torsors]
\label{lemma:classical_cyclic_equations_etale_torsors}
Let $A$ be a ring.
\begin{enumerate}[label=(\roman*)]
    \item If $n$ is invertible in $A$ and $a\in A^\times$, then
    \[
    A[T]/(T^n-a)
    \]
    is finite free over $A$, with basis $1,T,\dots,T^{n-1}$, and is
    \'etale over $A$. Multiplication of $T$ makes its spectrum a
    $\mu_n$-torsor over $\Spec A$.
    \item If $A$ is an $\F_p$-algebra and $a\in A$, then
    \[
    A[X]/(X^p-X-a)
    \]
    is finite free over $A$, with basis $1,X,\dots,X^{p-1}$, and is
    \'etale over $A$. Translation of $X$ makes its spectrum a
    $\Z/p\Z$-torsor over $\Spec A$.
\end{enumerate}
\end{lemma}

\begin{proof}
Both defining polynomials are monic, giving the stated bases and finite
freeness. In the Kummer algebra, $T$ is a unit because $T^n=a\in A^\times$;
therefore the derivative $nT^{n-1}$ is a unit. The derivative of
$X^p-X-a$ is $-1$. Thus both algebras are \'etale over $A$. They are the
pullbacks from Appendix~A.1 of $(-)^n:\bG_m\to\bG_m$ and
$\wp:\bG_a\to\bG_a$, respectively, so translation by the corresponding
kernels $\mu_n$ and $\F_p\cong\Z/p\Z$ gives the asserted torsor structures.
\end{proof}
```

- [ ] **Step 3: Add the ASW transition**

Immediately before `lemma:asw_etale_torsor`, insert:

```tex
The following is the Witt-vector analogue of
\Cref{lemma:classical_cyclic_equations_etale_torsors}. Its coordinate proof
requires the triangular form of Witt addition because, unlike the two
classical equations, Witt subtraction is not componentwise.
```

- [ ] **Step 4: Check the label and transition**

Run:

```bash
rg -n "classical_cyclic_equations_etale_torsors|Witt-vector analogue" witt/WittVectorAlgebraAppendix.tex witt/WittVectorPrerequisites.tex
```

Expected: one label definition, one reference, and one transition sentence.

---

### Task 2: Move Schmid--Witt scope and the pole-bound remark into Chapter 2

**Files:**
- Modify: `sections/Preliminaries/CyclicRamificationTheories.tex`, after `theorem:schmid_witt_break_formula` and after `lemma:realization_over_Gm`
- Modify: `witt/WittVectorPrerequisites.tex`, remove the former reference-and-scope subsection and moved remark

**Interfaces:**
- Consumes: `theorem:schmid_witt_break_formula`, the definition of reduced Witt vectors, and `eq:parallel_witt_pole_bound`.
- Produces: locally contextualized attribution/scope paragraphs and the preserved `rem:realization_Wr_sanity` remark in Chapter 2.

- [ ] **Step 1: Replace the appendix cross-reference after the theorem**

Replace the current two-sentence paragraph after `theorem:schmid_witt_break_formula` with:

```tex
The Schmid--Witt formula is an external ramification theorem: we use it as
stated and do not reproduce its proof. For finite residue fields, the formula
is due to Kanesaka--Sekiguchi \cite{KanesakaSekiguchi1979} and Thomas
\cite{Thomas2005}, building on Schmid \cite{Schmid1937} for $r=1$; for
arbitrary perfect residue fields, it is due to Elder--Keating
\cite{ElderKeating2025}. We use it in one direction only: evaluating the
formula on one reduced representative computes the largest upper break, so
no minimization over representatives is needed.

Reducedness prevents cancellation between Witt levels. Indeed, if two
nonzero pole orders $m_j$ and $m_{j'}$, with $j<j'$, contributed the same
weighted value, then
$m_{j'}=p^{j'-j}m_j$ would be divisible by $p$, contradicting reducedness.
For $r=1$, the formula is exactly the Artin--Schreier break computation.
```

- [ ] **Step 2: Move and contextualize the pole-bound remark**

After the proof of `lemma:realization_over_Gm`, insert:

```tex
\begin{rem*}\label{rem:realization_Wr_sanity}
In part~(3), the weighted pole bound forces $f_j=0$ whenever
$p^{r-1-j}\geq d$: if $f_j\neq0$, then $m_j$ is a positive integer and
$p^{r-1-j}m_j\geq d$, contradicting
\Cref{eq:parallel_witt_pole_bound}. Thus a break smaller than $d$ imposes a
visible restriction on every Witt component, not only on the last one.
\end{rem*}
```

- [ ] **Step 3: Remove the former Appendix A subsection**

Delete from `witt/WittVectorPrerequisites.tex`:

- `\subsubsection{The Schmid--Witt formula: reference and scope}`;
- `\label{appendix:schmid_witt_reference}`;
- the two explanatory paragraphs now located after the Chapter 2 theorem; and
- the old copy of `rem:realization_Wr_sanity`.

- [ ] **Step 4: Verify the move and label uniqueness**

Run:

```bash
rg -n "appendix:schmid_witt_reference|rem:realization_Wr_sanity|Kanesaka--Sekiguchi|no minimization" --glob '*.tex' --glob '!chapter2_reorg/**' --glob '!chapter2_reorganized/**' --glob '!theorem_49_completion/**'
```

Expected: no `appendix:schmid_witt_reference`; one compiled definition of
`rem:realization_Wr_sanity`; the attribution and scope text only in
`sections/Preliminaries/CyclicRamificationTheories.tex` among compiled files.

---

### Task 3: Retitle the remaining Appendix subsection and update its roadmap

**Files:**
- Modify: `witt/WittVectorAlgebraAppendix.tex`, opening roadmap
- Modify: `witt/WittVectorPrerequisites.tex`, A.4.3 heading hierarchy

**Interfaces:**
- Consumes: the removal of the Schmid--Witt reference subsection in Task 2.
- Produces: an Appendix A table of contents that accurately describes its remaining proved material.

- [ ] **Step 1: Update the Appendix roadmap**

Replace the final roadmap sentence with:

```tex
The final section isolates the weighted-homogeneity property used in the
cyclic symmetric-power calculation. The Schmid--Witt ramification-break
formula is stated, referenced, and applied in Chapter~2; we do not reproduce
its proof.
```

- [ ] **Step 2: Collapse the A.4.3 heading**

Replace:

```tex
\subsection{Reduced representatives and ramification}

\subsubsection{Reduced polynomial representatives}
```

with:

```tex
\subsection{Reduced polynomial representatives}
```

- [ ] **Step 3: Check the resulting source structure**

Run:

```bash
rg -n "^\\\\(sub)*section\{" witt/WittVectorAlgebraAppendix.tex witt/WittVectorPrerequisites.tex
```

Expected: A.4.3 is “Reduced polynomial representatives”; no Schmid--Witt
subsubsection remains in Appendix A.

---

### Task 4: Compile and inspect the thesis

**Files:**
- Verify: `main.tex`
- Verify: `main.log`
- Verify: `main.pdf`

**Interfaces:**
- Consumes: all source changes from Tasks 1--3.
- Produces: a fully resolved 73-page-or-similar thesis PDF with visually clean affected pages.

- [ ] **Step 1: Check source whitespace and labels**

Run:

```bash
git diff --check -- sections/Preliminaries/CyclicRamificationTheories.tex witt/WittVectorAlgebraAppendix.tex witt/WittVectorPrerequisites.tex
```

Expected: exit status 0 and no output.

Run:

```bash
rg -n "appendix:schmid_witt_reference" main.tex sections witt
```

Expected: no matches.

- [ ] **Step 2: Compile the complete thesis**

Run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Expected: exit status 0 and `main.pdf` regenerated.

- [ ] **Step 3: Check the build log**

Run:

```bash
rg -n "undefined references|Citation.*undefined|multiply defined|Runaway argument|Fatal error" main.log
```

Expected: no matches.

- [ ] **Step 4: Verify the compiled headings and moved prose**

Run:

```bash
pdftotext -layout main.pdf /private/tmp/appendix-a-torsor-placement.txt
rg -n "Classical cyclic equations|Witt-vector analogue|Reduced polynomial representatives|Kanesaka|visible restriction on every Witt component" /private/tmp/appendix-a-torsor-placement.txt
```

Expected: each new or moved passage appears once in the extracted compiled text.

- [ ] **Step 5: Render and visually inspect affected pages**

Locate the Chapter 2 Schmid--Witt theorem and Appendix A.2--A.4 pages from
the extracted text/page breaks, render those PDF pages to PNG with Poppler,
and inspect them for heading or theorem separation, overfull lines, clipping,
and awkward page breaks.

Expected: no new visual defects in the affected Chapter 2 or Appendix A pages.
