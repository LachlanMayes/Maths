"""
08 - ALGEBRA ADVANCED: Exponents, Logs, Polynomials, Quadratics
Sources:
  - https://www.mathsisfun.com/algebra/index.html
  - https://mathworld.wolfram.com/topics/Algebra.html
  - https://mathworld.wolfram.com/Polynomial.html, Exponent, Logarithm
Run: python 08_algebra_advanced.py [--plot]
"""
import sys
try: sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
except: pass
import math, cmath

PLOT = "--plot" in sys.argv
try:
    import sympy as sp
    HAS_SYMPY=True
except: HAS_SYMPY=False

print("="*60)
print("8.1 EXPONENTS & LAWS (mathsisfun exponent-laws.html)")
print("="*60)
# Wolfram Exponent, mathsisfun Laws of Exponents

def demo_laws():
    a,b=2,3
    x,y=4,5
    print(f"  a^m * a^n = a^(m+n): {a**x}*{a**y}={a**x * a**y}, {a}**{x+y}={a**(x+y)}")
    print(f"  (a^m)^n = a^(mn): ({a}**{x})**{y}={(a**x)**y}, {a}**{x*y}={a**(x*y)}")
    print(f"  (ab)^n = a^n b^n: ({a}*{b})**{x}={(a*b)**x}, {a}**{x}*{b}**{x}={a**x * b**x}")
    print(f"  a^0 =1: {a}**0={a**0}, 0^0? undefined, Python gives 1")
    print(f"  a^-n =1/a^n: {a}**-2={a**-2}")
    print(f"  Fractional: 9^(1/2)={9**0.5}, 8^(1/3)={8**(1/3):.4f}, 27^(2/3)={27**(2/3):.4f}")

demo_laws()
print(f"\nSurds (irrational roots): sqrt(2)={math.sqrt(2):.8f}, cube root 27={27**(1/3):.1f}")
print(f"  Simplify sqrt(72)=sqrt(36*2)=6*sqrt2={6*math.sqrt(2):.4f} vs {math.sqrt(72):.4f}")

print("\n" + "="*60)
print("8.2 LOGARITHMS (mathsisfun logarithms.html)")
print("="*60)
# Wolfram Log

for base in [2, math.e, 10]:
    print(f"  log base {base:.2f}: log({base**3:.0f})={math.log(base**3, base):.2f} (should be 3)")

print(f"\nNatural log ln(e)={math.log(math.e):.4f}, ln(1)=0, ln(0)-> -inf")
print(f"Common log log10(1000)={math.log10(1000):.1f}, log10(2)={math.log10(2):.4f}")
# Log laws
a,b=100,1000
print(f"\nLog laws:")
print(f"  log(ab)=log a+log b: log10({a}*{b})={math.log10(a*b):.2f}, {math.log10(a):.2f}+{math.log10(b):.2f}={math.log10(a)+math.log10(b):.2f}")
print(f"  log(a^n)=n log a: log10({a}^3)={math.log10(a**3):.2f}, 3*log10({a})={3*math.log10(a):.2f}")
print(f"  Change base: log2(8)={math.log2(8):.1f} = ln8/ln2={math.log(8)/math.log(2):.1f}")

# Exponential and log are inverses
x=5
print(f"\nInverse: exp(log({x}))={math.exp(math.log(x)):.4f}, 10^log10({x})={10**math.log10(x):.4f}")
# Solve exponential equation 2^x=32 -> x=log2(32)
print(f"  Solve 2^x=32 -> x={math.log2(32):.1f}")

if HAS_SYMPY:
    x=sp.symbols('x')
    print(f"\n  [sympy] log identities: expand_log(log(x*y))={sp.expand_log(sp.log(x*sp.Symbol('y')), force=True)}")

print("\n" + "="*60)
print("8.3 POLYNOMIALS (mathsisfun polynomials.html)")
print("="*60)
# Wolfram Polynomials (180 entries)

def poly_add(p,q): # coeff list low to high: [c0,c1,c2]
    n=max(len(p),len(q)); r=[0]*n
    for i,c in enumerate(p): r[i]+=c
    for i,c in enumerate(q): r[i]+=c
    return r
def poly_mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j,b in enumerate(q):
            r[i+j]+=a*b
    return r
def poly_eval(p,x):
    return sum(c*x**i for i,c in enumerate(p))
def poly_str(p):
    terms=[]
    for i,c in enumerate(p):
        if c==0: continue
        if i==0: terms.append(str(c))
        elif i==1: terms.append(f"{c}x" if c!=1 else "x")
        else: terms.append(f"{c}x^{i}" if c!=1 else f"x^{i}")
    return " + ".join(reversed(terms)) if terms else "0"
def poly_derivative(p): return [i*c for i,c in enumerate(p)][1:] if len(p)>1 else [0]
def poly_degree(p): return len(p)-1

p=[6,5,1]  # 1*x^2+5x+6 = (x+2)(x+3)
q=[1,2]    # 2x+1
print(f"  p={poly_str(p)}, degree {poly_degree(p)}")
print(f"  q={poly_str(q)}")
print(f"  p+q={poly_str(poly_add(p,q))}")
print(f"  p*q={poly_str(poly_mul(p,q))} (= (x^2+5x+6)(2x+1))")
print(f"  p(2)={poly_eval(p,2)} (should be 4+10+6=20)")
print(f"  derivative p'={poly_str(poly_derivative(p))} (power rule)")

# Factoring quadratics
print("\nFactoring quadratics (mathsisfun factoring-quadratics.html):")
# x^2+5x+6=(x+2)(x+3)
def factor_quadratic(a,b,c):
    # brute find integer factors of c that sum to b/a? simpler via discriminant
    for r1 in range(-10,11):
        if r1==0: continue
        if b*r1 + a*0: pass
    # use formula to find roots then factors
    disc=b*b-4*a*c
    if disc<0: return f"No real factors, disc {disc}"
    r1=(-b+math.sqrt(disc))/(2*a)
    r2=(-b-math.sqrt(disc))/(2*a)
    return f"({a}x roots {r1:.2f}, {r2:.2f}) -> {a}(x-{r1:.2f})(x-{r2:.2f})"

print(f"  x^2+5x+6: disc 25-24=1 roots -2,-3 -> (x+2)(x+3)")
print(f"  2x^2+7x+3: {factor_quadratic(2,7,3)} -> (2x+1)(x+3)")
print(f"  x^2-4: difference of squares -> (x-2)(x+2)")

if HAS_SYMPY:
    x=sp.symbols('x')
    print(f"\n  [sympy] factor x^2+5x+6 = {sp.factor(x**2+5*x+6)}")
    print(f"  expand (x+2)(x+3)= {sp.expand((x+2)*(x+3))}")
    print(f"  divide (x^2+5x+6)/(x+2) = {sp.div(x**2+5*x+6, x+2)}")
    print(f"  gcd x^2-1, x^2-3x+2 = {sp.gcd(x**2-1, x**2-3*x+2)}")

# Polynomial long division demo
print(f"\nPolynomial long division: (x^3+2x^2-5x+6)/(x-1)")
# Synthetic division
def synthetic_div(coeffs, root): # coeffs high to low
    out=[coeffs[0]]
    for c in coeffs[1:]:
        out.append(out[-1]*root + c)
    return out[:-1], out[-1] # quotient, remainder
coeffs=[1,2,-5,6] # x^3+2x^2-5x+6
quot,rem=synthetic_div(coeffs,1)
print(f"  Synthetic 1: quotient {quot} remainder {rem} => x^2+3x-2 remainder 4")

print("\n" + "="*60)
print("8.4 QUADRATICS & COMPLETING THE SQUARE")
print("="*60)

def solve_quadratic(a,b,c):
    disc=b*b-4*a*c
    if disc<0: return (complex(-b/(2*a), math.sqrt(-disc)/(2*a)), complex(-b/(2*a), -math.sqrt(-disc)/(2*a)))
    if disc==0: return (-b/(2*a),)
    return ((-b+math.sqrt(disc))/(2*a), (-b-math.sqrt(disc))/(2*a))

for coeffs in [(1, -5, 6), (1,2,1), (1,0,-9), (1,0,1)]:
    print(f"  {coeffs[0]}x^2+{coeffs[1]}x+{coeffs[2]}=0 -> roots {solve_quadratic(*coeffs)}")

print(f"\nCompleting square: x^2+6x+5 -> (x+3)^2 -4 -> roots -1,-5")
# Derive vertex form
def vertex_form(a,b,c):
    h=-b/(2*a); k=c - b*b/(4*a)  # vertex (h,k)
    return h,k
for coeffs in [(1,6,5),(1,-4,4),(2,8,6)]:
    a,b,c=coeffs; h,k=vertex_form(a,b,c)
    print(f"  {a}x^2+{b}x+{c}: vertex ({h:.1f},{k:.1f}), axis x={h:.1f}")

print("\n" + "="*60)
print("8.5 FUNCTIONS, SEQUENCES & SERIES (mathsisfun)")
print("="*60)

# Function definition (mathsisfun sets/function.html)
def func(f, x): return f(x)
print(f"  f(x)=x^2: f(3)={func(lambda x: x**2,3)}, f(-2)={func(lambda x:x**2,-2)}")
# Composite functions
def compose(f,g): return lambda x: f(g(x))
f=lambda x: x+2; g=lambda x: x**2
h=compose(f,g)
print(f"  f(g(x)) where f=x+2, g=x^2: f(g(3))={h(3)} (=11)")

# Sequences finding rule (mathsisfun sequences-finding-rule.html)
print(f"\nSequences:")
print(f"  Arithmetic 2,5,8,11... nth=3n-1, sum S=n/2*(2a+(n-1)d)")
def arithmetic_nth(a,d,n): return a+(n-1)*d
def arithmetic_sum(a,d,n): return n/2*(2*a+(n-1)*d)
print(f"    a=2,d=3,n=10 -> term {arithmetic_nth(2,3,10)}, sum {arithmetic_sum(2,3,10)}")
print(f"  Geometric 3,6,12... ratio 2")
def geometric_nth(a,r,n): return a*r**(n-1)
def geometric_sum(a,r,n): return a*(r**n-1)/(r-1) if r!=1 else a*n
print(f"    a=3,r=2,n=10 -> term {geometric_nth(3,2,10)}, sum {geometric_sum(3,2,10)}")

# Special sequences
print(f"\nSpecial: Fibonacci (from 01), Triangular numbers")
triangular=[n*(n+1)//2 for n in range(1,11)]
print(f"  Triangular: {triangular}")
square=[n*n for n in range(1,11)]
print(f"  Square: {square}")
# Power series sum
print(f"\nInfinite geometric r=0.5: sum =1/(1-r)=2, partial 1+0.5+0.25+...={sum(0.5**n for n in range(10)):.4f}")

# Inequalities
print(f"\nInequalities (mathsisfun inequality.html):")
print(f"  2x+3<7 -> x<2: test x=1 {2*1+3<7}, x=3 {2*3+3<7}")
print(f"  Quadratic x^2-3x+2>0 -> x<1 or x>2: test 0 {0-0+2>0}, 1.5 {2.25-4.5+2>0}, 3 {9-9+2>0}")

if PLOT:
    try:
        import numpy as np, matplotlib.pyplot as plt
        xs=np.linspace(-4,4,400)
        # Quadratics family
        plt.figure(figsize=(10,4))
        for coeffs, label in [((1,0,0),"x^2"),((1,2,1),"(x+1)^2"),((1,-2,-3),"x^2-2x-3"),((2,0,-2),"2x^2-2")]:
            a,b,c=coeffs
            ys=a*xs**2+b*xs+c
            plt.plot(xs,ys,label=label)
        plt.axhline(0,color='black',linewidth=0.5); plt.axvline(0,color='black',linewidth=0.5)
        plt.ylim(-6,10); plt.legend(); plt.grid(True); plt.title("Quadratic Family"); plt.show()

        # Exponential vs log
        xs2=np.linspace(0.1,4,200)
        plt.figure()
        plt.plot(xs2, np.exp(xs2), label='e^x')
        plt.plot(xs2, np.log(xs2), label='ln x')
        plt.plot(xs2, xs2, 'k--', label='y=x')
        plt.legend(); plt.grid(True); plt.title("Exp and Log are inverses (mirror y=x)"); plt.ylim(-2,6); plt.show()

        # Polynomial degree
        fig, axes=plt.subplots(1,3, figsize=(12,3))
        for i, coeffs in enumerate([[2,1],[ -3,0,1],[1,-6,11,-6]]): # degree 1,2,3
            # need convert low-high to polyval: reverse
            p=np.poly1d(list(reversed(coeffs)))
            # better eval via numpy poly
            pass
        print("Add more plots freely!")
    except Exception as e:
        print(e)
else:
    print("\n[Tip] --plot for quadratic family: python 08_algebra_advanced.py --plot")

print("\nChallenge: implement cubic solver (Cardano), or polynomial GCD via Euclidean algorithm")
