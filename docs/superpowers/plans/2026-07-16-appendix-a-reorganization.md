# Appendix A Reorganization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganize Appendix A so that the common cyclic-torsor framework and the classical cases lead into the Witt-vector and Artin--Schreier--Witt developments, without changing the mathematical statements.

**Architecture:** Preserve the existing chapter and theorem labels while changing only section hierarchy, section order, roadmap prose, and the stale appendix description in the introduction. Keep the substantial proofs in their current source files, moving only the classical introductory block into the appendix driver so the compiled reading order matches the approved outline.

**Tech Stack:** LaTeX (`report`, `cleveref`, `biblatex`), `latexmk`, Poppler PDF rendering.

## Global Constraints

- Preserve all theorem, proposition, lemma, equation, and cross-reference labels.
- Do not alter mathematical claims or proof text except for short transitional sentences required by the new order.
- Keep the Schmid--Witt formula explicitly identified as an externally cited theorem.
- Compile the full thesis and visually inspect every rendered Appendix A page.

---

### Task 1: Reorganize the Appendix A hierarchy

**Files:**
- Modify: `witt/WittVectorAlgebraAppendix.tex`
- Modify: `witt/WittVectorPrerequisites.tex`

**Interfaces:**
- Consumes: Existing labels referenced by Chapter 2, especially `appendix:cyclic_torsor_theories`, `appendix:asw_development`, and `appendix:schmid_witt_reference`.
- Produces: A five-part reader-facing sequence: common framework; classical cases; Witt-vector algebra; ASW theory; weighted Witt addition.

- [ ] **Step 1: Move the common construction and classical cases before the Witt-vector material**

Move the existing “common group-scheme construction” and “Kummer and Artin--Schreier theory” blocks from `WittVectorPrerequisites.tex` into `WittVectorAlgebraAppendix.tex` immediately after the appendix roadmap. Add separate Kummer and Artin--Schreier subsections without changing either proof.

- [ ] **Step 2: Consolidate the Witt-vector algebra**

Use one top-level section, `Witt-vector algebra`, with subsections for ring structure and for Frobenius--Verschiebung--truncation. Move the isobaricity lemma to the final top-level section, `Weighted Witt addition in the cyclic calculation`.

- [ ] **Step 3: Consolidate the ASW development**

Use one top-level section, `Artin--Schreier--Witt theory`, carrying `appendix:asw_development`, with subsections for the operator/bookkeeping, torsors/classification, and reduced representatives/ramification. Place the reduced-representative existence proof before the short Schmid--Witt reference discussion.

- [ ] **Step 4: Check labels and headings mechanically**

Run:

```bash
rg -n '^\\(chapter|section|subsection)\{|appendix:asw_development|appendix:schmid_witt_reference' witt/WittVectorAlgebraAppendix.tex witt/WittVectorPrerequisites.tex
```

Expected: five top-level sections in the approved order, with both ASW navigation labels still present exactly once.

---

### Task 2: Align the thesis roadmap

**Files:**
- Modify: `sections/Introduction.tex`

**Interfaces:**
- Consumes: The appendix order established in `main.tex` (`A` for cyclic torsors/Witt vectors, `B` for the abandoned approach).
- Produces: An accurate thesis-organization list.

- [ ] **Step 1: Replace the stale Appendix A entry**

Describe Appendix A as the supporting cyclic-torsor and Witt-vector theory used in Chapter 2, and add a separate Appendix B entry for “A Wrong Path.”

- [ ] **Step 2: Verify the roadmap text**

Run:

```bash
rg -n 'Appendix A|Appendix B' sections/Introduction.tex
```

Expected: exactly one accurate entry for each appendix.

---

### Task 3: Compile and verify the reader-facing result

**Files:**
- Verify: `main.pdf`
- Verify: `main.toc`

**Interfaces:**
- Consumes: The reorganized LaTeX sources.
- Produces: A compiling thesis whose Appendix A table of contents and rendered pages match the approved hierarchy.

- [ ] **Step 1: Compile the thesis**

Run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Expected: exit status 0 with no undefined-reference or multiply-defined-label warnings.

- [ ] **Step 2: Verify the table of contents**

Run:

```bash
rg -n 'appendix.A|section.A\\.|subsection.A\\.' main.toc
```

Expected: five Appendix A sections in the approved order and the intended subsections beneath them.

- [ ] **Step 3: Render and inspect Appendix A**

Locate the physical PDF page range containing Appendix A, render that range with `pdftoppm`, and inspect every page for broken headings, widows/orphans caused by the moves, clipped text, and malformed cross-references.

- [ ] **Step 4: Review the final diff**

Run:

```bash
git diff --check
git diff -- witt/WittVectorAlgebraAppendix.tex witt/WittVectorPrerequisites.tex sections/Introduction.tex
```

Expected: no whitespace errors and only the approved structural/editorial changes.
