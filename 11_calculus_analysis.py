"""
11 - CALCULUS & ANALYSIS ADVANCED
Sources:
  - https://www.mathsisfun.com/calculus/index.html
  - https://www.mathsisfun.com/calculus/fourier-series.html
  - https://mathworld.wolfram.com/topics/CalculusandAnalysis.html
  - arXiv: math.CA, math.AP, nlin.CD
Run: python 11_calculus_analysis.py [--plot]
"""
import sys
try: sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
except: pass
import math, cmath

PLOT="--plot" in sys.argv
try: import sympy as sp; HAS_SYMPY=True
except: HAS_SYMPY=False

print("="*60)
print("11.1 LIMITS ADVANCED & L'HOPITAL")
print("="*60)
# mathsisfun limits-formal.html, l-hopitals-rule.html, Wolfram Limits

# Formal epsilon-delta idea demo via sequence approaching limit
print("Formal limit: sequence  (n/(n+1)) ->1 as n->inf")
for n in [1,2,5,10,100,1000]:
    print(f"  n={n:4d}: {n/(n+1):.6f}")

# L'Hopital: lim x->0 sin x / x = cos0/1=1 (0/0 form)
print("\nL'Hopital's rule: 0/0 or inf/inf => limit = limit f'/g'")
def lhopital_sin_over_x():
    # limit x->0 sin x / x, derivative cos x /1 ->1
    for x in [0.1,0.01,0.001]:
        print(f"  x={x}: sin x / x={math.sin(x)/x:.8f}, cos x={math.cos(x):.8f} (->1)")
lhopital_sin_over_x()
print("  lim x->0 (1-cos x)/x^2 = sin x /2x -> cos x/2=1/2")
for x in [0.5,0.1,0.01]:
    print(f"    x={x}: {(1-math.cos(x))/x**2:.6f}")

# Limits to infinity
print("\nLimits at infinity:")
for n in [1,10,100,1000]:
    print(f"  (3n^2+2)/(n^2+5) at n={n}: {(3*n*n+2)/(n*n+5):.6f} ->3 (leading coeffs)")
print("  Growth: exp >> poly >> log . e.g., n=100: n^2=10000, 2^n huge, ln n=4.6")

print("\n" + "="*60)
print("11.2 SERIES & CONVERGENCE (Wolfram Series)")
print("="*60)
# mathsisfun sequences-series.html extension + Wolfram Series, Harmonic

# P-series: sum 1/n^p converges if p>1
def p_series(p, terms=10000):
    return sum(1/(n**p) for n in range(1,terms+1))
for p in [1,2,3]:
    val=p_series(p,10000)
    kind="diverges (harmonic)" if p==1 else "converges"
    print(f"  sum 1/n^{p} (10000 terms)={val:.5f} {kind}")
print(f"  Harmonic diverges slowly: sum 1/n ~ ln n + gamma")
# Geometric series already done
# Alternating harmonic converges to ln 2
alt=sum((-1)**(n+1)/n for n in range(1,10000))
print(f"  Alternating harmonic sum -> ln2: {alt:.6f} vs {math.log(2):.6f}")
# Exponential series
print(f"  e = sum 1/n! : {sum(1/math.factorial(n) for n in range(12)):.8f}")
# Basel already in 05

# Convergence tests preview
print("\nTests: ratio test, root test, comparison, integral test (Wolfram)")

print("\n" + "="*60)
print("11.3 DERIVATIVES ADVANCED")
print("="*60)
# mathsisfun derivatives-rules.html, second-derivative, chain, partial, implicit

def deriv(f,x,h=1e-7): return (f(x+h)-f(x-h))/(2*h)
def second(f,x,h=1e-5): return (f(x+h)-2*f(x)+f(x-h))/h**2

# Rules demo via numeric vs formula
print("Chain rule: d/dx sin(x^2)=2x cos(x^2)")
for x in [0.5,1,2]:
    f=lambda x: math.sin(x**2)
    num=deriv(f,x)
    true=2*x*math.cos(x**2)
    print(f"  x={x}: numeric {num:.5f}, formula {true:.5f}")

print("\nProduct rule: d/dx x^2 sin x =2x sin x + x^2 cos x")
for x in [1,2]:
    f=lambda x: x**2*math.sin(x)
    num=deriv(f,x)
    true=2*x*math.sin(x)+x**2*math.cos(x)
    print(f"  x={x}: {num:.5f} vs {true:.5f}")

print("\nImplicit differentiation: circle x^2+y^2=25 => 2x+2y y'=0 => y'=-x/y")
for x,y in [(3,4),(5,0),(0,5)]:
    if y!=0: print(f"  at ({x},{y}): y'={-x/y:.2f} (slope of tangent)")

print("\nSecond derivative & concavity:")
for x in [-1,0,1]:
    f=lambda x: x**3-3*x
    print(f"  f=x^3-3x at {x}: f''={second(f,x):.2f} {'concave up' if second(f,x)>0 else 'concave down' if second(f,x)<0 else 'inflection'}")

print("\nPartial derivatives: f(x,y)=x^2 y + sin y")
def f2(x,y): return x**2*y+math.sin(y)
def partial_x(f,x,y,h=1e-7): return (f(x+h,y)-f(x-h,y))/(2*h)
def partial_y(f,x,y,h=1e-7): return (f(x,y+h)-f(x,y-h))/(2*h)
for x,y in [(1,0),(2, math.pi/2)]:
    print(f"  at ({x},{y:.2f}): df/dx={partial_x(f2,x,y):.3f} (=2xy={2*x*y:.3f}), df/dy={partial_y(f2,x,y):.3f} (=x^2+cos y={x**2+math.cos(y):.3f})")

if HAS_SYMPY:
    x,y=sp.symbols('x y')
    expr=x**2*sp.sin(x)
    print(f"\n  [sympy] derivative {expr} = {sp.diff(expr,x)}")
    print(f"  partial x^2*y+sin y: dx={sp.diff(x**2*y+sp.sin(y), x)}, dy={sp.diff(x**2*y+sp.sin(y), y)}")

print("\n" + "="*60)
print("11.4 INTEGRATION TECHNIQUES")
print("="*60)
# mathsisfun integration-rules, by-parts, by-substitution, definite

def riemann(f,a,b,n): return sum(f(a+(i+0.5)*(b-a)/n)*(b-a)/n for i in range(n))
def simpson(f,a,b,n):
    # n must be even
    if n%2: n+=1
    h=(b-a)/n
    s=f(a)+f(b)
    for i in range(1,n):
        coeff=4 if i%2==1 else 2
        s+=coeff*f(a+i*h)
    return s*h/3

print("Integration methods for x^2 on [0,1] (true 1/3):")
for n in [4,8,20]:
    print(f"  n={n}: Riemann {riemann(lambda x:x**2,0,1,n):.6f}, Simpson {simpson(lambda x:x**2,0,1,n):.6f}")

print("\nIntegration by parts: int u dv = uv - int v du")
print("  Example int x e^x dx = (x-1)e^x +C")
for x in [0,1,2]:
    true=(x-1)*math.exp(x)
    print(f"    at {x}: {true:.3f}, derivative check: d/dx = x e^x? {x*math.exp(x):.3f}")

print("\nSubstitution: int 2x cos(x^2) dx = sin(x^2)+C")
for x in [0,1,1.5]:
    print(f"  F={math.sin(x**2):.4f}, F'={2*x*math.cos(x**2):.4f} (= integrand)")

print("\nDefinite + FTC: integral of derivative = change")
a,b=0, math.pi
val = -math.cos(b) - (-math.cos(a))  # int sin
print(f"  int_0^pi sin x dx = {val:.4f} (numeric {simpson(math.sin,0,math.pi,100):.4f})")

# Arc length (mathsisfun arc-length.html): integral sqrt(1+(dy/dx)^2)
def arc_length(f, fp, a,b,n=1000):
    return simpson(lambda x: math.sqrt(1+fp(x)**2), a,b,n)
f=lambda x: x**2
fp=lambda x: 2*x
print(f"\nArc length of y=x^2 from 0..1 = {arc_length(f,fp,0,1):.6f}")

# Solids of revolution (disk method): volume pi int [f(x)^2]
vol=math.pi*simpson(lambda x: (x**2)**2, 0,1,200)  # y=x^2 revolved around x-axis
print(f"Volume solid y=x^2 revolved x-axis 0..1 (disks): pi int x^4 = pi/5={math.pi/5:.4f} vs numeric {vol:.4f}")

if HAS_SYMPY:
    x=sp.symbols('x')
    print(f"\n  [sympy] integrate x*sin(x) = {sp.integrate(x*sp.sin(x), x)}")
    print(f"  integrate 1/(1+x^2) = {sp.integrate(1/(1+x**2), x)} (= arctan)")

print("\n" + "="*60)
print("11.5 DIFFERENTIAL EQUATIONS (mathsisfun)")
print("="*60)
# Separation, first order linear, etc.

# 1) Separation: dy/dx = k y => y= C e^{kt}
print("Separation: dy/dx = 0.5 y => y= C e^{0.5 x}, y(0)=2")
def y_exp(x): return 2*math.exp(0.5*x)
for x in [0,1,2,4]:
    print(f"  x={x}: y={y_exp(x):.3f}, check dy/dx={0.5*y_exp(x):.3f}")

# Euler method for ODE dy/dx = x + y, y(0)=1 (Wolfram DifferentialEquations)
def euler_ode(f, y0, x0, xn, steps):
    h=(xn-x0)/steps
    x,y=x0,y0
    ys=[(x,y)]
    for _ in range(steps):
        y += h*f(x,y)
        x += h
        ys.append((x,y))
    return ys

def f_ode(x,y): return x+y
traj=euler_ode(f_ode,1,0,1,10)
print(f"\nEuler for dy/dx=x+y, y(0)=1, up to x=1 (10 steps): y(1) approx {traj[-1][1]:.4f}")
print(f"  True (analytic y=2e^x - x -1): {2*math.exp(1)-1-1:.4f}")

# Second order: y''+y=0 => y= A cos x + B sin x (harmonic)
print(f"\nSecond order y''+y=0: y=cos x")
for x in [0, math.pi/2, math.pi]:
    print(f"  x={x:.2f}: y={math.cos(x):.3f}, y''={-math.cos(x):.3f} => y''+y=0? {abs(-math.cos(x)+math.cos(x))<1e-9}")

print("\n" + "="*60)
print("11.6 FOURIER SERIES (mathsisfun fourier-series.html)")
print("="*60)
# Wolfram FourierSeries

# Square wave: 4/pi * sum sin((2k-1)x)/(2k-1)
def square_wave(x, terms=5):
    s=0
    for k in range(1, terms+1):
        n=2*k-1
        s+= math.sin(n*x)/n
    return 4/math.pi * s

for terms in [1,3,10]:
    vals=[square_wave(x, terms) for x in [math.pi/4, math.pi/2, 3*math.pi/4]]
    print(f"  {terms} terms square approx at pi/4, pi/2, 3pi/4: {[f'{v:.3f}' for v in vals]} (ideal 1,1,1 overshoot near jumps=Gibs)")

print(f"  Gibbs phenomenon: overshoot ~9% near discontinuity no matter terms")

if PLOT:
    try:
        import numpy as np, matplotlib.pyplot as plt
        xs=np.linspace(-math.pi, math.pi, 400)
        plt.figure(figsize=(10,4))
        for t in [1,3,10,50]:
            ys=[square_wave(x,t) for x in xs]
            plt.plot(xs, ys, label=f"{t} terms")
        plt.plot(xs, np.sign(np.sin(xs)), 'k--', label='ideal square')
        plt.ylim(-1.5,1.5); plt.legend(); plt.grid(True); plt.title("Fourier Series Square Wave (Gibbs)"); plt.show()

        # ODE direction field
        xs=np.linspace(0,2,10)
        ys=np.linspace(0,5,10)
        X,Y=np.meshgrid(xs,ys)
        U=1 ; V= X+Y
        plt.figure()
        plt.quiver(X,Y,U,V, color='blue', alpha=0.5)
        traj=np.array(euler_ode(f_ode,1,0,2,50))
        plt.plot(traj[:,0], traj[:,1], 'r-', label='Euler y(0)=1')
        plt.legend(); plt.grid(True); plt.title("ODE dy/dx=x+y direction field"); plt.show()

        # Arc length visualization
        x=np.linspace(0,1,100); y=x**2
        plt.figure()
        plt.plot(x,y, label='y=x^2')
        plt.fill_between(x,0,y, alpha=0.2)
        plt.title(f"Area under x^2 and arc length {arc_length(f,fp,0,1):.3f}"); plt.grid(True); plt.legend(); plt.show()
    except Exception as e: print(e)
else:
    print("\n[Tip] --plot for Fourier & ODE field: python 11_calculus_analysis.py --plot")

print("\nChallenge: implement Runge-Kutta 4, or compute Fourier for sawtooth/triangle!")
