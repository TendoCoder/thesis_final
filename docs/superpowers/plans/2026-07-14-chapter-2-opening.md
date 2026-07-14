# Chapter 2 Opening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Put the theorem setup at the beginning of Chapter 2, improve its precision, and relocate the appendix-only Galois base-change lemma.

**Architecture:** A new focused LaTeX source file will contain the unnumbered Chapter 2 preamble and will be included before the local ramification preliminaries. The Galois base-change lemma will move from the Chapter 2 preliminary file into Appendix A before its first citation. Existing theorem and equation labels will be preserved so downstream references continue to resolve.

**Tech Stack:** LaTeX, `latexmk`, Git.

## Global Constraints

- Preserve `theorem:torsors_after_blowup_is_tame`, `equation:blowup_diagram_ndls`, and `lem:galois-base-change`.
- Do not edit or discard unrelated generated-file changes already present in the worktree.
- Keep the Chapter 2 setup unnumbered and before `Local Ramification Preliminaries`.

---

### Task 1: Create and include the Chapter 2 preamble

**Files:**
- Create: `sections/RamificationAfterBlowupIntroduction.tex`
- Modify: `main.tex:53-63`
- Modify: `sections/RamificationAfterBlowupIsTame.tex:1-37`

**Interfaces:**
- Consumes: theorem and definition labels from Chapter 1 and the Introduction.
- Produces: the unchanged labels `equation:blowup_diagram_ndls` and `theorem:torsors_after_blowup_is_tame` for later chapters.

- [x] **Step 1: Add the revised setup, diagram, torsor theorem, and proof roadmap to the new preamble file.**
- [x] **Step 2: Replace the short duplicate prose in `main.tex` with an input of the new preamble before the local preliminary input.**
- [x] **Step 3: Remove the displaced opening from `RamificationAfterBlowupIsTame.tex`, leaving it to begin with the `Ramification of G-Torsors` section.**
- [x] **Step 4: Search for duplicate theorem and equation labels.**

Run: `rg -n "equation:blowup_diagram_ndls|theorem:torsors_after_blowup_is_tame" main.tex sections`

Expected: one definition of each label and any legitimate cross-references.

### Task 2: Relocate the Galois base-change lemma and retitle Chapter 2 sections

**Files:**
- Modify: `sections/Preliminaries/LocalRamificationPreliminaries.tex:172-209`
- Modify: `a_wrong_path/a_wrong_path.tex:1-163`
- Modify: `sections/RamificationAfterBlowupIsTame.tex:433,873`

**Interfaces:**
- Consumes: the Appendix A field notation introduced in `Setup and notation`.
- Produces: the unchanged label `lem:galois-base-change` for the two Appendix A citations.

- [x] **Step 1: Remove the base-change section from the local ramification preliminary file.**
- [x] **Step 2: Insert the lemma as an Appendix A subsection before its first citation.**
- [x] **Step 3: Rename the proof section to `Proof of the Torsor Formulation` and the final section to `Ramification on Products of Blowups`.**
- [x] **Step 4: Confirm that the lemma is defined once and cited only after its definition.**

Run: `rg -n "lem:galois-base-change|Base-Change Lemma" sections a_wrong_path`

Expected: one definition in Appendix A and two later citations there.

### Task 3: Compile and inspect the revised thesis

**Files:**
- Verify: `main.tex`
- Verify: `main.log`
- Verify: `main.toc`

**Interfaces:**
- Consumes: all LaTeX sources changed in Tasks 1 and 2.
- Produces: a compiled `main.pdf` with resolved structure and references.

- [x] **Step 1: Compile the thesis.**

Run: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`

Expected: exit status 0 and a regenerated `main.pdf`.

- [x] **Step 2: Check the log for structural reference errors.**

Run: `rg -n "Undefined control sequence|LaTeX Error|multiply defined|undefined references|Citation .* undefined" main.log`

Expected: no matches caused by this restructuring.

- [x] **Step 3: Check the Chapter 2 table-of-contents sequence.**

Run: `rg -n "chapter.2|section.2" main.toc`

Expected: Local Ramification Preliminaries, Ramification of G-Torsors, Proof of the Torsor Formulation, and Ramification on Products of Blowups, with no Chapter 2 base-change section.

### Task 4: Explain the exceptional divisor using elementary coordinates

**Files:**
- Modify: `sections/Preliminaries/GeneralPreliminaries.tex:747-767`
- Modify: `sections/RamificationAfterBlowupIntroduction.tex:26-38`
- Verify: `main.pdf`

**Interfaces:**
- Consumes: `theorem:blowup_flat_base_change` and the smoothness of symmetric powers from `prop:relative_symmetric_power_smooth`.
- Produces: `prop:exceptional_divisor_smooth_point`, cited by the Chapter 2 preamble.

- [x] **Step 1: Add a proposition in the Chapter 1 blowup subsection stating that the exceptional divisor of the blowup of a smooth $d$-dimensional scheme at a $k$-rational closed point $z$ is $\mathbb P^{d-1}_k$, irreducible, and of codimension one.**
- [x] **Step 2: Prove the proposition by choosing étale local coordinates, applying flat base change for blowups, and identifying the fiber over the origin in the incidence model $x_i u_j=x_j u_i$.**
- [x] **Step 3: Replace the unsupported assertion in the Chapter 2 opening with a citation to `prop:exceptional_divisor_smooth_point`.**
- [x] **Step 4: Compile with `latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error main.tex` and visually inspect the affected Chapter 1 and Chapter 2 pages.**
