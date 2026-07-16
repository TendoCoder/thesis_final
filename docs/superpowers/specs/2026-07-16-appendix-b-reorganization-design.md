# “A Failure of an Artin--Schreier Induction Strategy” Design

**Goal:** Reorganize Appendix B so that it begins with the proposed induction from the Chapter 2 Artin--Schreier calculation, introduces the exact geometric and torsor-theoretic setup only after the motivation, follows the two induction inputs through the valuation tower, and ends with an explicit example showing why the inference does not close.

**Title:** Appendix B will be renamed **“A Failure of an Artin--Schreier Induction Strategy.”** The preposition “of” is used because the appendix analyzes the failure of a particular strategy, not a failure to perform an action.

## Scope and mathematical claim

The appendix will explain the failure of a proof strategy, not contradict the Artin--Schreier--Witt theorem proved in Chapter 2. Its final example will show that unramifiedness of the top degree-$p$ layer after a wild base change does not imply unramifiedness before that base change. The conclusion will not claim that the example itself arises from the original symmetric-power geometry unless that stronger fact is separately proved.

The substantial quotient, field, valuation, and inertia arguments already present in `a_wrong_path/a_wrong_path.tex` will be preserved. The work is primarily structural and editorial: move material, remove duplicated setup, rename the failed ``theorem'' as a proposed induction step, clarify what each hypothesis contributes, and consolidate the two absorption examples.

## Reader-facing organization

### B.1. Motivation: Can the Artin--Schreier calculation be iterated?

Recall that Chapter 2 proves the order-$p$ case by an explicit Artin--Schreier calculation and the order-$p^r$ case by a direct Artin--Schreier--Witt calculation. For
\[
G=\mathbf Z/p^r\mathbf Z,
\qquad
H=p^{r-1}G\cong\mathbf Z/p\mathbf Z,
\qquad
G/H\cong\mathbf Z/p^{r-1}\mathbf Z,
\]
factor the torsor as
\[
\mathcal P\longrightarrow\mathcal P/H\longrightarrow U.
\]
Present the tempting strategy immediately: use induction for the $G/H$-torsor, use the degree-$p$ calculation for the remaining $H$-torsor, and try to combine the two conclusions. End with the exact implication that the appendix will test.

### B.2. Preliminaries for the attempted induction

This section will contain, in dependency order:

1. the summation kernels $K_H$, $K_G$, and $K_{G/H}$;
2. the four symmetric quotient schemes;
3. the Cartesian quotient-tower proposition;
4. the compactification $C'\to C$, the two blowups, exceptional generic points, and DVRs;
5. one master diagram combining the torsor and geometric towers;
6. the base-change lemma needed to pass to function fields.

The existing smaller quotient diagram will not be repeated after the master diagram. The remark that the two comparison maps need not be torsors under constant groups will remain, but it will be shortened to the point needed later: these maps may introduce ramification not controlled by the two torsor layers.

The current unlabeled theorem will be recast as a **proposed induction step** or **question**. Its assumptions will be named according to their origin:

- **(IH$_{r-1}$):** the $G/H$ symmetric-power torsor is unramified at $\eta_C$;
- **(AS):** the symmetric degree-$p$ layer is unramified at $\eta_{C'}$.

The desired conclusion is that the $G$ symmetric-power torsor is unramified at $\eta_C$.

### B.3. Following the hypotheses through the valuation tower

After reducing to a connected torsor with $H\ne0$, introduce
\[
K_C\subset F\subset E,
\qquad
F\subset K_{C'},
\qquad
E K_{C'},
\]
and the corresponding places and valuation rings. Display the field and valuation towers together.

Immediately translate the inputs and goal:

| Source | Extension | What is known or required |
|---|---|---|
| Induction on $r-1$ | $F/K_C$ | unramified at $V_C$ |
| Degree-$p$ calculation after base change | $EK_{C'}/K_{C'}$ | unramified at $V_{C'}$ |
| Missing step | $E/F$ | must be shown unramified at $V_F$ |
| Desired conclusion | $E/K_C$ | would then be unramified at $V_C$ |

Use the inertia lemma to obtain only an injection
\[
I(v_\star\mid V_{C'})\hookrightarrow I(v_E\mid V_F).
\]
The second input makes the source trivial, but says nothing about the target without a surjectivity or ramification-preservation statement. Identify $K_{C'}/F$, induced by the symmetric comparison map $q$, as the uncontrolled base change.

### B.4. Failure under wild base change

Give a single example in two stages. First translate the pattern into the $G=\mathbf Z/p^2\mathbf Z$ tower notation. Then make absorption explicit with
\[
F=k((t)),\qquad K=k((\pi)),\qquad
t=\frac{\pi^p}{1-\pi^{p-1}},
\]
and
\[
E=F(y),\qquad y^p-y=t^{-1}.
\]
Over $F$, $E/F$ is a ramified Artin--Schreier extension. Over $K$,
\[
t^{-1}=\pi^{-p}-\pi^{-1}=\wp(\pi^{-1}),
\]
so the class becomes trivial. Thus the base-changed inertia is trivial although the original inertia is $\mathbf Z/p\mathbf Z$.

This single example replaces the current abstract counterexample followed by a largely duplicative explicit example.

### B.5. What the example proves

Conclude with four precise points:

1. the example does not contradict the theorem proved in Chapter 2;
2. the two proposed induction inputs do not determine the missing inertia group;
3. a wild base change can absorb the Artin--Schreier ramification by supplying an element of intermediate valuation;
4. the direct Artin--Schreier--Witt calculation in Chapter 2 avoids this gap.

## Editorial constraints

- Preserve existing theorem, proposition, lemma, equation, and example labels when the corresponding content survives.
- Add a label to the proposed induction step if later cross-references require one.
- Do not duplicate definitions already stated in Chapters 1--2; recall them only in the specialized notation of this appendix.
- Use consistent notation for $H$ as the unique order-$p$ subgroup of $G$.
- In Chapter 2, add a forward reference at the transition from the degree-$p$ Artin--Schreier calculation to the $p^r$ Artin--Schreier--Witt calculation. The reference will say that Appendix B studies the tempting attempt to derive the latter case inductively from the former and explains why wild base change prevents the argument from closing.
- Correct the Introduction so that the existing Witt-vector chapter is Appendix A and Appendix B is “A Failure of an Artin--Schreier Induction Strategy.”
- Compile the complete thesis and inspect the rendered Appendix B pages after editing.

## Verification

The completed edit must:

1. compile with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`;
2. produce the five Appendix B sections above in `main.toc`;
3. introduce no undefined or multiply defined references;
4. preserve the logical distinction between failure of the induction inference and truth of the Chapter 2 theorem;
5. render without broken diagrams, headings, or page layout in Appendix B.
