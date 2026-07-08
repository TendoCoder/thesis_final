import sympy as sp
from itertools import combinations

def modp(expr,p):
    expr=sp.expand(expr)
    out=sp.Integer(0)
    for mono,coef in expr.as_coefficients_dict().items():
        c=int(coef)%p
        if c: out+=c*mono
    return sp.expand(out)

def witt_sum(vectors,p,r):
    def ghost(vec,n): return sum(p**i*vec[i]**(p**(n-i)) for i in range(n+1))
    Wsum=[sp.expand(sum(ghost(v,n) for v in vectors)) for n in range(r)]
    alpha=[]
    for n in range(r):
        rhs=Wsum[n]-sum(p**i*alpha[i]**(p**(n-i)) for i in range(n))
        alpha.append(sp.expand(sp.cancel(rhs/p**n)))
    return [modp(a,p) for a in alpha]

def deg_y(F,xs):
    """max pole order at the x_i=0 collision = max degree in y=1/x."""
    d=len(xs); ys=sp.symbols('y1:%d'%(d+1))
    G=sp.together(sp.expand(F.subs({xs[i]:1/ys[i] for i in range(d)})))
    n,dn=sp.fraction(G)
    Pn=sp.Poly(sp.expand(n),*ys)
    degn=max(sum(m) for m in Pn.monoms())
    if dn.free_symbols:
        Pd=sp.Poly(sp.expand(dn),*ys); degd=min(sum(m) for m in Pd.monoms())
    else: degd=0
    return degn-degd

def elem(xs,k): return sum(sp.prod(c) for c in combinations(xs,k)) if k>0 else sp.Integer(1)

def vC_exact(F,xs,p):
    """exact v_C: write symmetric F in elementary symm e_i (all v_C=1), uniformizer e_d.
       return v_C(F)."""
    d=len(xs); ed=elem(xs,d)
    F=sp.cancel(sp.together(F)); num,den=sp.fraction(F)
    # den should be ed^k * const
    k=0; cur=sp.expand(den)
    while True:
        q,rmd=sp.div(cur,sp.expand(ed),*xs)
        if rmd==0: cur=q;k+=1
        else: break
        if k>60: break
    from sympy.polys.polyfuncs import symmetrize
    se,rem,mp=symmetrize(sp.expand(num),*xs,formal=True)
    # se is expression in s1,s2,... where s_i <-> e_i(x); each has v_C=1
    se=modp(se,p)
    if se==0: return sp.oo
    gens=sorted(se.free_symbols,key=str)
    if not gens: mind=0
    else: mind=min(sum(m) for m in sp.Poly(se,*gens).monoms())
    return mind-k

print("="*72); print("PART 1:  p=3, r=2, d=4   test case  (u2 = max(3*1,m1)=3 < 4)"); print("="*72)
p,r,d=3,2,4; xs=list(sp.symbols('x1:%d'%(d+1)))
for m1 in (1,2,3):
    vecs=[[xi**(-1), xi**(-m1)] for xi in xs]
    al=witt_sum(vecs,p,r)
    dys=[deg_y(al[j],xs) for j in range(r)]
    vCs=[vC_exact(al[j],xs,p) for j in range(r)]
    print(" m0=1,m1=%d: deg_y(alpha)=%s  v_C(alpha)=%s  -> %s"
          %(m1,dys,vCs,"UNRAMIFIED" if all(v>=0 for v in vCs) else "RAMIFIED"))
print(" alpha_1 explicitly (m1=1):",sp.together(witt_sum([[xi**(-1),xi**(-1)] for xi in xs],p,r)[1]))

print(); print("="*72); print("PART 2: boundary p=3,r=2,d=3  (u2=3=d, bound fails strictly)"); print("="*72)
p,r,d=3,2,3; xs=list(sp.symbols('x1:%d'%(d+1)))
al=witt_sum([[xi**(-1),sp.Integer(0)] for xi in xs],p,r)
print(" alpha_1 (a1=0, pure carry) =",sp.together(al[1]))
print(" deg_y(alpha_1)=%d  v_C(alpha_1)=%s -> %s"
      %(deg_y(al[1],xs),vC_exact(al[1],xs,p),"RAMIFIED (pole)" if vC_exact(al[1],xs,p)<0 else "unram"))

print(); print("="*72); print("PART 3: r=2 scan -- deg_y(alpha_1) =? max(p*m0,m1); integral iff <d"); print("="*72)
allok=True
for p in (2,3,5):
  for (m0,m1) in [(1,1),(1,2),(2,1),(1,3)]:
    if m0%p==0: continue
    d=max(m0*p,m1)+2; xs=list(sp.symbols('x1:%d'%(d+1)))   # d large enough to read true deg
    al=witt_sum([[xi**(-m0),xi**(-m1)] for xi in xs],p,r if (r:=2) else 2)
    D=deg_y(al[1],xs); pred=max(p*m0,m1); ok=(D==pred); allok&=ok
    print(" p=%d m0=%d m1=%d : deg_y(alpha1)=%d  max(p*m0,m1)=%d  match=%s"%(p,m0,m1,D,pred,ok))
print(" ALL match upper-break formula u2=max(p*m0,m1):",allok)
