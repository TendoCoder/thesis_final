# Ramification of `q` along `V_F` — research suggestions

A standalone note (`q_ramification_along_VF.tex`) with concrete suggestions for
the open step in the inductive proof of
`theorem:ramification_after_blowup_is_tame_for_p_power`
(the red *"not clear how to finish"* at `RamificationAfterBlowupIsTame.tex:671`).

## The question

You want to investigate the ramification of the symmetrisation morphism

> `q : (𝒫_{G/H})^{(d)} → (𝒫_{G/H})^{[d]}`,  i.e. the field extension `K_{C'} / F`,

**along the place `V_F = V_{C'}|_F`**, and relate it to the global hypotheses
that `𝒫 → U` has ramification **bounded by `d`** and that `G = ℤ/pʳ` with
**`r < d`**.

## What the note argues

1. **This is exactly the missing input.** `a_wrong_path.tex` already reduced the
   theorem to *"E/F unramified at V_F"* and showed the only obstruction is the
   ramification `q` introduces in `K_{C'}/F` at `V_{C'}|V_F` (it can *absorb*
   the ramification of `E/F`). Its closing remark says ruling this out *"for a
   given (𝒫,d) is exactly the global input the inductive argument lacks"* — and
   neither the bound `d` nor `r < d` was used there. Supplying them is the task.

2. **Key observations.**
   - The known counterexamples live at the boundary `r = d`; `r < d` is the
     first regime they do **not** cover.
   - `r < d` is essentially **free**: for a totally ramified `ℤ/pʳ` with bound
     `d`, Hasse–Arf forces `r ≤ uᵣ < d`.
   - Aim for a **break bound**, not "q unramified" (q *is* genuinely ramified
     along `V_F` in general — shown in `inertia_symmetry_obstruction.tex`).

3. **Four strategies** (ranked). The recommended one (A) computes the break
   `β_q` of the q-defect directly in the weighted-blowup local model — the same
   method that already proves the `r = 1` case — and targets the inequality
   `β_q < β_E`, which forbids the absorption. (B) packages it via the different;
   (C) rules out `K̂_{C'} = Ê` by a global invariant; (D) re-resolves so the
   codimension-one lemma applies.

4. **A decisive small computation** (§5): do `G = ℤ/p²`, `d = 3` (smallest
   `r < d`), compute `β_q` and check `β_q < β_E`. It either proves the first
   case (template for the induction) or yields a sharper-than-`r<d` hypothesis.

## Subfolder: `strategy_D_dead_end/`

A post-mortem proving **Strategy D cannot work**. The key is a one-line invariant:

> `e(V_{C'} | V_F) = p^{r-1}`  (Theorem in the note),

a **wild** ramification index (for `r ≥ 2`) that is a **birational invariant** of the
fixed place `V_{C'}|V_F` — no resolution changes it to `1`, so `q` is never
unramified there and the codimension-one lemma (which only ever yields `e = 1`,
at boundary divisors where just one of the `d` points collides) cannot reach the
full-collision valuation `V_{C'}`. This upgrades observation (O2) to a theorem.

It also answers the follow-up *"can a wild `q`-defect still absorb `E/F`?"*:
**yes — wildness is what enables absorption.** Base-change multiplies the break
to `p^{r-1}·β_E ≡ 0 (mod p)`, which opens Artin–Schreier reduction over
`K̂_{C'}`; absorption *completes* only if `Ê ⊆ K̂_{C'}` (a leading-coefficient
coincidence). So the fight is over a class in `F̂/℘(F̂)`, not over a ramification
index — sharpening Strategy C and the `r = 2, d = 3` test.

Build: `TEXINPUTS=../..: latexmk -pdf strategy_D_dead_end.tex`

## Subfolder: `first_case_r2_d3/`

The first open case past the boundary, **computed and machine-verified**
(`wittcheck.py`): `p = 2`, `G = ℤ/4` (`r = 2`), `d = 3`.

**Result — the class survives, theorem holds for `(r,d)=(2,3)`.** The symmetric
power `P^{[3]_G}` has Witt datum `α = (e₂/e₃, Σa₁(xᵢ) + e₁/e₃)`, both components
**integral** at `V_C`, so `E/K_C` is unramified — no absorption.

The mechanism is exact: the *only* new obstruction is the length-2 **Witt carry**
`e₂(x^{-m₀})`, and it loses its pole at `V_C` **iff `2m₀ < d`, i.e. iff the
ramification bound `u₂ < d` holds**. At the boundary `d = r = 2` the carry is
`1/e₂` (a pole) → ramified, reproducing the `a_wrong_path` counterexample. So for
`p=2, r=2` the theorem holds *exactly* under the bound. (`p ≥ 3` is forced out at
`d=3` since `u₂ ≥ p`; the next genuine test is `p=3, r=2, d=4`.)

Build: `TEXINPUTS=../..: latexmk -pdf first_case_r2_d3.tex` · verify: `python3 wittcheck.py`

## Subfolder: `general_witt_proof/`  ← candidate proof of the open theorem

Pushing the `first_case_r2_d3` computation to its conclusion gives a **direct
proof of `theorem:ramification_after_blowup_is_tame_for_p_power` for all
`G = ℤ/pʳ`** — bypassing the inductive route that stalls in `a_wrong_path`.

**Engine.** `P^{[d]_G}` has, at `V_C`, the Artin–Schreier–**Witt** datum
`α = Σᵂᵢ a(xᵢ)` (d-fold Witt sum). Its `j`-th component `S_j` is **isobaric of
weight `pʲ`**, so its pole order (degree in `y=1/x`) is `≤ max_l p^{j-l} m_l =
u_{j+1}`, the `(j+1)`-th upper break. A symmetric Laurent poly with all poles
`< d` is integral at `V_C`. So the bound `u_r < d` makes the **whole** Witt datum
integral ⟹ `E/K_C` unramified at `η_C`. Carries and all — killed in one shot,
with no base change along `q`, hence no absorption to fight.

**Verified** (`witt_general.py`, `witt_r3.py`):
- `p=3, r=2, d=4` (the requested next case): **unramified, class survives.**
- `r=2`, all `p∈{2,3,5}`: `deg_y(α₁) = max(p·m₀, m₁) = u₂` **exactly**.
- `r=3` (`p=2`): `deg_y(αⱼ) = u_{j+1}` exactly, nested carries included
  (e.g. `(m₀,m₁,m₂)=(1,1,1) → (1,2,4)`, `(1,3,1) → (1,3,6)`).
- Boundary `p=3, d=3=u₂`: ramified (`v_C(α₁) = −1`) — note `r<d` *holds* here, so
  the right hypothesis is the **bound `u_r<d`**, not `r<d`.

**Status:** candidate proof. The structural `Lemma 1` (datum = Witt sum) mirrors
the thesis's own `ℤ/p` computation and deserves the author's scrutiny; see §6 of
the note for the precise open points.

Build: `TEXINPUTS=../..: latexmk -pdf general_witt_proof.tex`

## Build

```
latexmk -pdf q_ramification_along_VF.tex
```

(uses `../includes.tex`, `../MacrosAndFigures.tex`, `../Bib.bib`; same preamble
as `inertia_symmetry_obstruction.tex`. Cross-references to thesis labels resolve
to `??` in standalone mode, as in the other scratch notes.)
