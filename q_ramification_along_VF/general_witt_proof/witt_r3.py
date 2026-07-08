import sympy as sp
def modp(e,p):
    e=sp.expand(e); o=sp.Integer(0)
    for m,c in e.as_coefficients_dict().items():
        c=int(c)%p
        if c:o+=c*m
    return sp.expand(o)
def witt_sum(vectors,p,r):
    def ghost(v,n): return sum(p**i*v[i]**(p**(n-i)) for i in range(n+1))
    W=[sp.expand(sum(ghost(v,n) for v in vectors)) for n in range(r)]
    a=[]
    for n in range(r):
        rhs=W[n]-sum(p**i*a[i]**(p**(n-i)) for i in range(n))
        a.append(sp.expand(sp.cancel(rhs/p**n)))
    return [modp(x,p) for x in a]
def deg_y(F,xs):
    d=len(xs); ys=sp.symbols('y1:%d'%(d+1))
    G=sp.together(sp.expand(F.subs({xs[i]:1/ys[i] for i in range(d)})))
    n,dn=sp.fraction(G); Pn=sp.Poly(sp.expand(n),*ys)
    degn=max(sum(m) for m in Pn.monoms())
    degd=min(sum(m) for m in sp.Poly(sp.expand(dn),*ys).monoms()) if dn.free_symbols else 0
    return degn-degd
print("r=3, p=2 : deg_y(alpha_j) vs predicted breaks u_{j+1}=max_l 2^{j-l} m_l")
for (m0,m1,m2) in [(1,1,1),(1,1,3),(1,3,1)]:
    u1=m0; u2=max(2*m0,m1); u3=max(4*m0,2*m1,m2)
    d=u3+1; xs=list(sp.symbols('x1:%d'%(d+1)))
    al=witt_sum([[xi**(-m0),xi**(-m1),xi**(-m2)] for xi in xs],2,3)
    dys=[deg_y(al[j],xs) for j in range(3)]
    print(" (m0,m1,m2)=(%d,%d,%d): deg_y=%s  breaks=(%d,%d,%d)  match=%s  d=%d>u3 -> integral=%s"
          %(m0,m1,m2,dys,u1,u2,u3,dys==[u1,u2,u3],d,all(x<d for x in dys)))
