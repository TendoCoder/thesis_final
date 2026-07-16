# Chapter 3 Reorganization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create an isolated, reorganized Chapter 3 source file whose narrative follows the descent proof from Abel--Jacobi geometry through boundary extension to geometric class field theory.

**Architecture:** The deliverable is a new Chapter 3 body file in `chapter3_reorganized_codex/`; no existing thesis source and no file under `chapter3_reorganized/` will be changed. Existing Chapter 3 material will be copied and reordered, the approved chapter introduction will be added, duplicate proof headings will be consolidated, and the existing full extension proof will replace the included placeholder proof.

**Tech Stack:** LaTeX, the thesis's existing macros and bibliography, `latexmk`, Poppler PDF rendering.

## Global Constraints

- Do not modify any existing thesis file.
- Do not read from, write to, or otherwise touch `chapter3_reorganized/`.
- Create all persistent work under `chapter3_reorganized_codex/`.
- Keep the final Chapter 3 source in one file: `chapter3_reorganized_codex/chapter3_reorganized_codex.tex`.
- Use a disposable wrapper outside the repository deliverable to compile the new chapter in the context of the existing thesis.

---

### Task 1: Assemble the reorganized Chapter 3 source

**Files:**
- Create: `chapter3_reorganized_codex/chapter3_reorganized_codex.tex`

**Interfaces:**
- Consumes: macros, theorem environments, labels, and bibliography entries defined by the existing thesis.
- Produces: a Chapter 3 body beginning with `\chapter{Geometric Class Field Theory}` and ending with the proof of `\Cref{thm:GCFT_reduced}`.

- [x] **Step 1: Add the approved chapter introduction**

Insert an unnumbered opening after the chapter heading that states the reduced GCFT goal and previews the sequence: Abel--Jacobi geometry, Takeuchi compactification, boundary tameness, extension, and descent.

- [x] **Step 2: Reorder the geometric setup**

Place the generalized Picard scheme and Abel--Jacobi morphism first, followed by Takeuchi's compactification. Rename headings to describe their mathematical role.

- [x] **Step 3: Consolidate the ramification argument**

Collect product compatibility, the addition-map lemma, large-degree propagation, coprime-modulus reduction, and the proof of the global symmetric-power tameness theorem under one section titled `Tame Ramification Along the Full Boundary`. Because editing Chapter 2 is forbidden, copy the existing products-of-blowups result into a subordinate subsection titled `Compatibility Under Products`; it must not remain a chapter-level section between the compactification and the main argument.

- [x] **Step 4: Integrate the full boundary-extension proof**

Copy the contents of `sections/GeometricCFT/ExtensionOfTamelyRamifiedSheaf.tex` into a section titled `Extension Across the Boundary`, omitting its integration-only header comments. Do not retain the placeholder proof from `ProofOfReducedTheorem.tex`.

- [x] **Step 5: Finish with descent**

Place the étale fundamental-group exact sequence immediately before the final theorem, then copy and edit the two-case proof of reduced GCFT so that the torsor/local-system language is consistent and uniqueness is explicit.

### Task 2: Verify source structure and references

**Files:**
- Test: `chapter3_reorganized_codex/chapter3_reorganized_codex.tex`

**Interfaces:**
- Consumes: the Chapter 3 source produced by Task 1.
- Produces: structural evidence that the file contains one chapter introduction, one symmetric-power theorem proof section, one extension section, and one final descent section.

- [x] **Step 1: Check forbidden paths and source isolation**

Run:

```bash
git status --short
find chapter3_reorganized_codex -maxdepth 1 -type f -print
```

Expected: only newly created files under `chapter3_reorganized_codex/`; no changes under `chapter3_reorganized/` or existing thesis paths.

- [x] **Step 2: Check section hierarchy**

Run:

```bash
rg -n '^\\chapter|^\\section|^\\subsection' chapter3_reorganized_codex/chapter3_reorganized_codex.tex
```

Expected section order: generalized Picard/Abel--Jacobi; Takeuchi compactification; full-boundary tameness; boundary extension; descent and reduced GCFT.

- [x] **Step 3: Check placeholders and duplicate labels**

Run:

```bash
rg -n '\\textcolor\{red\}|TODO|FIXME|Route 1|Route 2' chapter3_reorganized_codex/chapter3_reorganized_codex.tex
```

Expected: no matches.

Extract labels from the new file and confirm that each label is defined at most once.

### Task 3: Compile and visually inspect the reorganized chapter

**Files:**
- Test: `chapter3_reorganized_codex/chapter3_reorganized_codex.tex`
- Temporary: `/tmp/chapter3_reorganized_codex_build/main.tex`

**Interfaces:**
- Consumes: the reorganized Chapter 3 file plus unchanged thesis sources.
- Produces: a disposable compiled PDF and log used only for verification.

- [x] **Step 1: Create a disposable full-thesis wrapper**

Copy the existing `main.tex` to `/tmp/chapter3_reorganized_codex_build/main.tex`, replace only its Chapter 3 inputs in that temporary copy with an input of the new source, and set `TEXINPUTS` so LaTeX can resolve unchanged repository files.

- [x] **Step 2: Compile**

Run `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` from the temporary build directory.

Expected: exit code `0` and a generated `main.pdf`.

- [x] **Step 3: Inspect diagnostics**

Search the build log for fatal errors, undefined references, multiply defined labels, and PDF-string warnings originating in Chapter 3. Resolve source problems in the new file and rebuild until no Chapter 3 structural error remains.

- [x] **Step 4: Render and inspect Chapter 3 pages**

Use `pdftoppm` to render the Chapter 3 page range to PNG. Inspect the opening, section transitions, diagrams, and final proof for clipping, broken headings, or unreadable content.

- [x] **Step 5: Confirm isolation**

Run `git status --short` again.

Expected: no modified existing file and no entry under `chapter3_reorganized/`.
