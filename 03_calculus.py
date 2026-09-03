"""
03 - CALCULUS: Limits, Derivatives & Integrals
Source: https://www.mathsisfun.com/calculus/index.html
Run: python 03_calculus.py [--plot]
"""
import math
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except: pass
PLOT = "--plot" in sys.argv

print("="*60)
print("3.1 LIMITS - The foundation")
print("="*60)
# mathsisfun.com/calculus/limits.html
# Classic limit: sin(x)/x -> 1 as x->0
print("Limit sin(x)/x as x->0:")
for x in [1, 0.5, 0.1, 0.01, 0.001, 0.0001]:
    print(f"  x={x:.4f} -> sin(x)/x = {math.sin(x)/x:.8f}  (approaches 1)")

# Another: (1 + 1/n)^n -> e
print("\nLimit (1+1/n)^n as n->inf -> e:")
for n in [1, 10, 100, 1000, 10000, 100000]:
    val = (1+1/n)**n
    print(f"  n={n:6d} -> {val:.8f} (e={math.e:.8f}, error {abs(val-math.e):.2e})")

# Derivative as limit: f'(x) = lim h->0 [f(x+h)-f(x)]/h
print("\nDerivative as limit of slope:")
def derivative_limit(f, x, h=1e-7):
    return (f(x+h)-f(x))/h

def f(x): return x**2  # f' = 2x
for x in [1,2,3,5]:
    approx = derivative_limit(f, x, h=1e-8)
    true = 2*x
    print(f"  f(x)=x² at x={x}: approx f'={approx:.6f}, true={true}, error {abs(approx-true):.2e}")

print("\n" + "="*60)
print("3.2 DERIVATIVES - Rules & intuition")
print("="*60)
# mathsisfun.com/calculus/derivatives-rules.html

# Numerical derivative helpers
def deriv(f, x, h=1e-7):
    return (f(x+h)-f(x-h))/(2*h)  # central difference (more accurate)

# Power rule: d/dx x^n = n*x^(n-1)
print("Power rule tests:")
tests = [
    (lambda x: x**3, lambda x: 3*x**2, "x³ -> 3x²"),
    (lambda x: x**4, lambda x: 4*x**3, "x⁴ -> 4x³"),
    (lambda x: math.sqrt(x), lambda x: 0.5/math.sqrt(x), "√x -> 1/(2√x)"),
    (lambda x: 1/x, lambda x: -1/x**2, "1/x -> -1/x²"),
]
for f, f_prime_true, label in tests:
    x=2
    num = deriv(f, x)
    true = f_prime_true(x)
    print(f"  {label:20s} at x={x}: numeric {num:.6f}, formula {true:.6f} {'✓' if abs(num-true)<1e-5 else '✗'}")

# Product, chain rule demo via sympy if available
try:
    import sympy as sp
    x = sp.symbols('x')
    print("\n  [sympy] Symbolic derivatives:")
    for expr in [x**3 + 2*x, sp.sin(x)*sp.cos(x), sp.exp(x**2), sp.log(x), 1/(x**2+1)]:
        print(f"    d/dx {str(expr):15s} = {sp.diff(expr, x)}")
    # Chain rule example: d/dx sin(x²) = 2x cos(x²)
    print(f"    Chain rule: d/dx sin(x²) = {sp.diff(sp.sin(x**2), x)}")
except ImportError:
    print("  (pip install sympy for symbolic derivatives)")

# Exponential & trig derivatives
print("\nSpecial derivatives:")
x=1.0
print(f"  d/dx e^x at x=1: {deriv(math.exp, 1):.6f} (true e^1={math.e:.6f})")
print(f"  d/dx sin(x) at x=0: {deriv(math.sin, 0):.6f} (true cos(0)=1)")
print(f"  d/dx ln(x) at x=2: {deriv(math.log, 2):.6f} (true 1/2=0.5)")

# Second derivative -> curvature
def second_deriv(f, x, h=1e-5):
    return (f(x+h) - 2*f(x) + f(x-h)) / h**2

print(f"\nSecond derivative of x³ at x=2: {second_deriv(lambda x: x**3, 2):.4f} (true 6x = 12)")
print(f"Second derivative tells concavity: >0 concave up, <0 concave down")

# Gradient descent preview (uses derivatives to find minima)
print("\nGradient descent teaser (find min of x²+3x+5):")
def g(x): return x**2 + 3*x + 5
def g_prime(x): return 2*x + 3
x = 5.0
lr = 0.3
for i in range(8):
    grad = g_prime(x)
    x -= lr * grad
    print(f"  step {i+1}: x={x:.6f}, g(x)={g(x):.6f}, grad={grad:.4f}")
print(f"  True minimum at x=-1.5, g(-1.5)={g(-1.5)} (where g'=0)")

print("\n" + "="*60)
print("3.3 INTEGRALS - Area under curve")
print("="*60)
# mathsisfun.com/calculus/integration-introduction.html

def riemann_sum(f, a, b, n, method='midpoint'):
    dx = (b-a)/n
    total = 0
    for i in range(n):
        if method == 'left': x = a + i*dx
        elif method == 'right': x = a + (i+1)*dx
        else: x = a + (i+0.5)*dx  # midpoint
        total += f(x)*dx
    return total

def f2(x): return x**2  # integral 0..1 = 1/3
print("Integral of x² from 0 to 1 (true = 1/3 ≈ 0.3333):")
for n in [10, 100, 1000, 10000]:
    approx = riemann_sum(f2, 0, 1, n, 'midpoint')
    print(f"  n={n:5d} midpoint: {approx:.8f} (error {abs(approx-1/3):.2e})")

# Fundamental theorem check: integral of f' = f
print("\nDefinite integrals (exact via antiderivative):")
def integrate_power(n, a, b):
    # integral x^n dx = x^(n+1)/(n+1)
    return (b**(n+1) - a**(n+1))/(n+1)

print(f"  ∫₀¹ x² dx = {integrate_power(2,0,1):.6f} ( = 1/3 )")
print(f"  ∫₀² x³ dx = {integrate_power(3,0,2):.6f} ( = 16/4 = 4 )")
print(f"  ∫₀^π sin(x) dx = {-math.cos(math.pi) - (-math.cos(0)):.6f} ( = 2 )")
print(f"    numeric check: {riemann_sum(math.sin, 0, math.pi, 10000):.6f}")

# Area between curves
print(f"\nArea between y=x and y=x² from 0..1:")
f_top = lambda x: x
f_bot = lambda x: x**2
area = riemann_sum(lambda x: f_top(x)-f_bot(x), 0, 1, 10000)
print(f"  ∫₀¹ (x - x²) dx = {area:.6f} (true 1/2 - 1/3 = 1/6 ≈ 0.1667)")

try:
    import sympy as sp
    x = sp.symbols('x')
    print("\n  [sympy] Symbolic integrals:")
    for expr in [x**2, sp.sin(x), sp.exp(x), 1/x, x*sp.exp(x)]:
        print(f"    ∫ {str(expr):12s} dx = {sp.integrate(expr, x)}")
    print(f"    Definite ∫₀^π sin(x) dx = {sp.integrate(sp.sin(x), (x, 0, sp.pi))}")
except ImportError:
    pass

print("\n" + "="*60)
print("3.4 TAYLOR SERIES - Approximate anything!")
print("="*60)
# mathsisfun.com/calculus/taylor-series.html
# e^x = 1 + x + x²/2! + x³/3! + ...
def taylor_exp(x, terms=10):
    return sum(x**n / math.factorial(n) for n in range(terms))

def taylor_sin(x, terms=7):
    # sin(x) = x - x³/3! + x⁵/5! - ...
    return sum((-1)**k * x**(2*k+1) / math.factorial(2*k+1) for k in range(terms))

print(f"e^1 via Taylor (true {math.e:.8f}):")
for t in [3,5,10,15]:
    print(f"  {t:2d} terms: {taylor_exp(1, t):.8f}")

print(f"\nsin(0.5) via Taylor (true {math.sin(0.5):.8f}):")
for t in [1,2,3,5]:
    print(f"  {t} terms: {taylor_sin(0.5, t):.8f}")

if PLOT:
    import numpy as np
    import matplotlib.pyplot as plt

    # Function + derivative visualization
    xs = np.linspace(-2, 3, 400)
    ys = xs**3 - 3*xs  # f(x) = x^3 - 3x
    dys = 3*xs**2 - 3  # f'(x)
    plt.figure(figsize=(10,4))
    plt.plot(xs, ys, label="f(x)=x³-3x")
    plt.plot(xs, dys, label="f'(x)=3x²-3", linestyle='--')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    # Mark critical points where f'=0
    plt.plot([-1,1], [2,-2], 'ro', label="critical points (f'=0)")
    plt.title("Function and its Derivative")
    plt.legend(); plt.grid(True); plt.show()

    # Riemann sum visualization
    fig, axes = plt.subplots(1,3, figsize=(12,3), sharey=True)
    f = lambda x: x**2
    for idx, n in enumerate([5, 20, 100]):
        ax = axes[idx]
        xs2 = np.linspace(0,1,200)
        ax.plot(xs2, f(xs2), 'r', label='x²')
        dx = 1/n
        for i in range(n):
            x = i*dx
            ax.bar(x, f(x), width=dx, alpha=0.3, align='edge', edgecolor='blue')
        ax.set_title(f"Left Riemann n={n}, sum={riemann_sum(f,0,1,n,'left'):.4f}")
        ax.set_ylim(0,1)
    plt.suptitle("Riemann Sums Converge to 1/3"); plt.tight_layout(); plt.show()

    # Taylor series convergence
    xs = np.linspace(-2, 2, 200)
    plt.figure()
    plt.plot(xs, np.exp(xs), 'k-', label='e^x (true)', linewidth=2)
    for terms in [2,3,5,8]:
        ys = [taylor_exp(x, terms) for x in xs]
        plt.plot(xs, ys, '--', label=f'{terms} terms')
    plt.ylim(-1, 7); plt.legend(); plt.grid(True)
    plt.title("Taylor Series for e^x"); plt.show()

    # Gradient descent path
    xs = np.linspace(-4, 2, 200)
    ys = xs**2 + 3*xs + 5
    plt.figure()
    plt.plot(xs, ys, label='g(x)=x²+3x+5')
    # replay descent
    x = 5.0
    path_x, path_y = [x], [x**2+3*x+5]
    for _ in range(10):
        x -= 0.3*(2*x+3)
        path_x.append(x); path_y.append(x**2+3*x+5)
    plt.plot(path_x, path_y, 'ro-', label='gradient descent')
    plt.legend(); plt.grid(True); plt.title("Gradient Descent to Minimum"); plt.show()
else:
    print("\n[Tip] Run with --plot for visuals: python 03_calculus.py --plot")

print("\nChallenge: implement Simpson's rule (more accurate) and compare!")
