# Chapter 2 Opening Design

## Goal

Restore the displaced Chapter 2 introduction to the beginning of the chapter, improve its mathematical precision and prose, and keep auxiliary material near the part of the thesis that uses it.

## Placement

The chapter setup will appear as an unnumbered preamble immediately after the Chapter 2 heading and before `Local Ramification Preliminaries`. It will live in a focused source file, `sections/RamificationAfterBlowupIntroduction.tex`, included from `main.tex`.

The preamble will:

- fix the curve, modulus, and open curve used throughout the chapter;
- define the point in the symmetric power, the blowup, its exceptional divisor, and its generic point;
- explain the reduction from the rank-one local-system theorem to the torsor formulation;
- state the torsor theorem; and
- give a roadmap matching the actual proof: tame and Artin--Schreier cases, the Artin--Schreier--Witt case, and the finite abelian reduction.

## Chapter structure

After the unnumbered preamble, Chapter 2 will have the following numbered sections:

1. Local Ramification Preliminaries.
2. Ramification of G-Torsors.
3. Proof of the Torsor Formulation.
4. Ramification on Products of Blowups.

The short Galois base-change lemma will be removed from the Chapter 2 preliminaries and placed in Appendix A before its first use, because only Appendix A cites it.

## Editorial corrections

The revision will distinguish the single-point submoduli `\ndls=n_iP_i` used in the theorem from arbitrary submoduli. It will replace the undefined `d` in the exceptional-divisor fiber product with `d_\ndls=\deg(\ndls)`, state the frame-torsor comparison as a canonical identification, remove sentence fragments, and align the roadmap with the proof currently present in the chapter.

## Elementary description of the exceptional divisor

The Chapter 1 `Blowups` subsection will include a proposition describing the exceptional divisor of the blowup of a smooth scheme at a closed point. Its proof will avoid projectivized normal bundles and associated graded algebras. Instead, it will use étale local coordinates, flat base change for blowups, and the explicit incidence-equation model of the blowup of affine space at the origin. The Chapter 2 opening will cite this proposition when asserting that $E_\ndls$ is projective space, irreducible, and of codimension one.

## Verification

The thesis will be compiled with the repository's existing LaTeX workflow. The resulting log will be checked for undefined references, multiply defined labels, and fatal errors, and the table of contents will be inspected to confirm that the base-change lemma no longer appears as a Chapter 2 section.
