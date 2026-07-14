# Shared Preliminaries and Torsor Dictionary Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give thesis-wide torsor constructions their own preliminary chapter, keep specialized local ramification background in Chapter 1, and make the local-system/torsor language switch explicit and rigorous.

**Architecture:** Split the existing monolithic preliminary source at the start of the local ramification material. The new shared chapter contains torsors, the rank-one local-system dictionary, and symmetric powers; Chapter 1 retains ramification and algebraic-geometry prerequisites. Update the introduction and chapter openings so the new dependency order is visible to the reader.

**Tech Stack:** LaTeX (`report` class), `latexmk`, Biber, Poppler.

## Global Constraints

- Preserve all existing mathematical labels and cross-references.
- Preserve the user's existing removal of the unused “Scheme Quotients in general” placeholder.
- State GCFT in local-system language and use torsors for geometric and ramification calculations.
- Do not alter the mathematical proofs beyond the language bridges required by the restructuring.

---

### Task 1: Split and Reorder the Preliminary Material

**Files:**
- Create: `sections/Preliminaries/GeneralPreliminaries.tex`
- Create: `sections/Preliminaries/LocalRamificationPreliminaries.tex`
- Delete: `sections/Preliminaries/Preliminaries.tex`
- Modify: `main.tex`

**Interfaces:**
- Produces: Chapter-level shared background before the ramification chapter, and Chapter 1-local prerequisite sections.

- [ ] Add a `General Preliminaries` chapter before the ramification chapter in `main.tex`.
- [ ] Move torsors and symmetric powers into `GeneralPreliminaries.tex`, promoting their headings by one level.
- [ ] Move ramification and algebraic-geometry prerequisites into `LocalRamificationPreliminaries.tex`, promoting their headings by one level.
- [ ] Include the local prerequisite file at the beginning of the ramification chapter.
- [ ] Run `latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex`; expect exit code 0.

### Task 2: Rewrite the Torsor Motivation and Dictionary

**Files:**
- Modify: `sections/Preliminaries/GeneralPreliminaries.tex`

**Interfaces:**
- Produces: `prop:torsor_module_equivalence` with explicit frame and associated-module functors, plus a declared language convention used by both research chapters.

- [ ] Add the approved opening motivation before the first torsor definition.
- [ ] Restrict the claimed rank-one correspondence to `G=Lambda^times`.
- [ ] Write the associated-module functor as `P times^G Lambda` and the inverse as the frame torsor.
- [ ] Add a local-triviality proof and state compatibility with pullback and tensor products.
- [ ] Define the symmetric power of a rank-one local system through the symmetric power of its frame torsor.
- [ ] Explain that the common monodromy character makes ramification bounds agree.
- [ ] Compile with `latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex`; expect exit code 0.

### Task 3: Update the Thesis Roadmap and Language Bridges

**Files:**
- Modify: `sections/Introduction.tex`
- Modify: `main.tex`
- Modify: `sections/RamificationAfterBlowupIsTame.tex`
- Modify: `sections/GeometricCFT/ProofOfReducedTheorem.tex`

**Interfaces:**
- Consumes: `prop:torsor_module_equivalence` and the shared-chapter organization from Tasks 1–2.
- Produces: Consistent chapter numbering and explicit translations at the two main proof boundaries.

- [ ] Update the organization paragraph to list the new preliminary chapter and renumber the two research chapters.
- [ ] At the start of the ramification chapter, explain why the sheaf theorem reduces to the torsor theorem.
- [ ] In the reduced GCFT proof, explicitly introduce the local system associated with the torsor before invoking sheaf-language results.
- [ ] Run `rg -n "Chapter [123]" sections/Introduction.tex` and confirm the roadmap matches the compiled chapter order.
- [ ] Compile with `latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex`; expect exit code 0.

### Task 4: Verify the Compiled Thesis

**Files:**
- Verify: `main.pdf`
- Verify: `main.toc`

**Interfaces:**
- Consumes: all preceding changes.
- Produces: a structurally and visually checked thesis PDF.

- [ ] Run `rg -n "General Preliminaries|Ramification After Blowup Is Tame|Geometric Class Field Theory" main.toc`; confirm the chapters occur in that order.
- [ ] Run `rg -n "undefined references|multiply defined|LaTeX Error" main.log`; expect no matches.
- [ ] Render the relevant chapter-opening pages with `pdftoppm -f <page> -l <page> -png -r 120 main.pdf tmp/pdfs/main`.
- [ ] Inspect the rendered pages for heading hierarchy, page breaks, and malformed text.
- [ ] Run one final `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`; expect exit code 0 and an up-to-date target.
