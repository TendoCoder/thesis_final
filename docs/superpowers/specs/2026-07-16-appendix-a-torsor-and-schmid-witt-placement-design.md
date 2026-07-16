# Appendix A Torsor and Schmid--Witt Placement Design

## Goal

Make the treatment of Kummer, Artin--Schreier, and
Artin--Schreier--Witt equations structurally parallel without referring to
Witt-vector coordinates before Witt vectors have been introduced, and place
the Schmid--Witt reference discussion beside the theorem in Chapter 2 where
the formula is stated and used.

## Étale-torsor exposition

Appendix A.1 will retain the common abstract construction: pulling back a
finite étale surjective homomorphism of commutative group schemes with kernel
\(G\) produces a \(G\)-torsor. It will not contain the coordinate proof for
Artin--Schreier--Witt equations, because the reader has not yet met Witt
vectors, their addition law, Frobenius, or the operator \(F-\mathrm{id}\).

At the end of Appendix A.2, after both classical theories have been
introduced, a two-part lemma will record their concrete scheme-level
realizations:

1. If \(n\) is invertible in a ring \(A\) and \(a\in A^\times\), then
   \(A[T]/(T^n-a)\) is finite free and étale over \(A\), with basis
   \(1,T,\ldots,T^{n-1}\), and its spectrum is a \(\mu_n\)-torsor under
   multiplication of \(T\).
2. If \(A\) is an \(\mathbf F_p\)-algebra and \(a\in A\), then
   \(A[X]/(X^p-X-a)\) is finite free and étale over \(A\), with basis
   \(1,X,\ldots,X^{p-1}\), and its spectrum is a
   \(\mathbf Z/p\mathbf Z\)-torsor under translation of \(X\).

The proof will use monicity for finite freeness, the derivatives
\(nT^{n-1}\) and \(-1\) for étaleness, and the kernel actions for the torsor
statements.

The existing ASW lemma will remain in Appendix A.4.2, after the necessary
Witt-vector algebra and ASW operator have been defined. A transition will
identify it as the Witt-vector analogue of the classical lemma and explain
that its triangular-coordinate proof is the additional ingredient required
because Witt addition is not componentwise. Its existing label
`lemma:asw_etale_torsor` and its finite-free basis statement will be
preserved because Chapter 2 uses both.

## Schmid--Witt placement

The subsection “The Schmid--Witt formula: reference and scope” will be
removed from Appendix A. Its two explanatory paragraphs will be moved to
`sections/Preliminaries/CyclicRamificationTheories.tex`, immediately after
`theorem:schmid_witt_break_formula`. This places the attribution, scope of
use, no-minimization observation, and reducedness/no-cancellation explanation
beside the theorem itself.

The current cross-reference from Chapter 2 to
`appendix:schmid_witt_reference` will be removed, and that appendix label will
be retired after confirming that it has no other compiled consumers.

The remark `rem:realization_Wr_sanity` will move out of the former
Schmid--Witt subsection and appear immediately after the “Parallel
realization over \(\mathbf G_m\)” lemma in Chapter 2. There, the symbols
\(d\), \(f_j\), and the weighted pole bounds have already been introduced,
so the remark will read as a direct consequence of that lemma.

After removing the ramification-reference material, Appendix A.4.3 will be
titled “Reduced polynomial representatives” and will contain only the
integral-surjectivity and reduced-representative results proved in the
appendix. The Appendix A roadmap will say that the Schmid--Witt theorem is
stated in Chapter 2 rather than suggesting that its reference discussion is
developed in the appendix.

## Compatibility and verification

Existing mathematical labels used elsewhere will be preserved, except for
the appendix-only Schmid--Witt scope label that becomes unnecessary. All
compiled references to the moved material will be updated.

Verification will consist of:

- scanning the repository for stale references and duplicate labels;
- compiling the complete thesis with `latexmk`;
- checking the log for undefined references, citations, and fatal errors;
- checking the source diff for whitespace errors; and
- rendering and visually reviewing the affected Chapter 2 and Appendix A
  pages.
