import sympy as sp

p, d = 2, 3
x1,x2,x3 = sp.symbols('x1 x2 x3')
e1 = x1+x2+x3
e2 = x1*x2+x1*x3+x2*x3
e3 = x1*x2*x3

def mod2(expr):
    expr = sp.expand(expr)
    syms = sorted(expr.free_symbols, key=str)
    if not syms:
        return sp.Integer(int(expr) % 2)
    return sp.Poly(expr, *syms).trunc(2).as_expr()

# (A) W_2 carry, char 2:  C(a,b) = (a^2+b^2-(a+b)^2)/2 = -ab  == ab (mod 2)
a0,b0 = sp.symbols('a0 b0')
C = sp.expand((a0**p+b0**p-(a0+b0)**p)/p)
print("[A] Witt carry C(a0,b0) =", C, "; mod2 =", mod2(C), " (expect a0*b0)")

# (B) accumulate over d=3 points; top W-component should be sum t_i + e2(s)
s1,s2,s3,t1,t2,t3 = sp.symbols('s1 s2 s3 t1 t2 t3')
def wadd(A,B):
    (A0,A1),(B0,B1)=A,B
    c = mod2((A0**p+B0**p-(A0+B0)**p)/p)
    return (mod2(A0+B0), mod2(A1+B1+c))
S = wadd(wadd((s1,t1),(s2,t2)),(s3,t3))
top_minus_sumt = mod2(S[1]-(t1+t2+t3))
e2s = s1*s2+s1*s3+s2*s3
print("[B] (top W-comp) - (sum t_i) =", top_minus_sumt, "; equals e2(s)?", mod2(top_minus_sumt-e2s)==0)

# (C) substitute bottom datum s_i = a0(x_i)=x_i^{-1} (m0=1):
carry3 = sp.simplify(e2s.subs({s1:1/x1,s2:1/x2,s3:1/x3}))
alpha0 = sp.simplify(1/x1+1/x2+1/x3)
print("[C] alpha0 = sum 1/x_i  =", sp.together(alpha0), "; = e2/e3?", sp.simplify(alpha0-e2/e3)==0)
print("    carry  = e2(1/x)    =", sp.together(carry3), "; = e1/e3?", sp.simplify(carry3-e1/e3)==0)

# (D) valuations at V_C:  v_C(e_i)=1, v_C(e_i/e_j)=0  (thesis model)
def vC(num_edeg, den_edeg): return num_edeg-den_edeg
print("\n[D] d=3 (r<d):  alpha0=e2/e3 (v_C=%d),  carry=e1/e3 (v_C=%d)"%(vC(1,1),vC(1,1)))
print("    BOTH Witt components integral at V_C  =>  E/K_C UNRAMIFIED  =>  [a] SURVIVES (theorem holds)")

# (E) contrast d=2 boundary (r=d):
carry2 = sp.simplify((s1*s2).subs({s1:1/x1,s2:1/x2}))
print("\n[E] d=2 (r=d):  carry=s1*s2|_{s=1/x} =", sp.together(carry2),
      "= 1/e2  (v_C=%d  POLE) => E/K_C RAMIFIED => absorption/counterexample"%vC(0,1))

# (F) general p=2 statement: carry = e2(s), s_i=x_i^{-m0}; pole killed iff 2*m0<d
print("\n[F] general p=2,r=2: top obstruction = e2(x^{-m0}) = sym poly deg 2*m0 in 1/x")
for m0 in (1,2):
    for dd in (2,3,4,5):
        killed = 2*m0 < dd      # integral in kappa_C iff 2*m0 < d (thesis lemma)
        print("     m0=%d (u2=2m0=%d), d=%d : carry pole killed? %s  -> %s"
              %(m0,2*m0,dd,killed, "UNRAMIFIED" if killed else "RAMIFIED"))
