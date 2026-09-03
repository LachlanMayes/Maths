"""
14 - APPLIED MATH & NUMERICAL METHODS
Sources:
  - https://www.mathsisfun.com/measure/index.html
  - https://www.mathsisfun.com/algebra/linear-programming.html
  - https://mathworld.wolfram.com/topics/AppliedMathematics.html
  - https://mathworld.wolfram.com/topics/NumericalMethods.html
  - arXiv: math.NA, math.OC
Run: python 14_applied_numerical.py [--plot]
"""
import sys
try: sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
except: pass
import math, random

PLOT="--plot" in sys.argv

print("="*60)
print("14.1 MEASUREMENT & UNITS (mathsisfun measure)")
print("="*60)
# SI units, conversions

def celsius_to_fahrenheit(c): return c*9/5+32
def km_to_miles(km): return km*0.621371
def kg_to_pounds(kg): return kg*2.20462

print(f"0C={celsius_to_fahrenheit(0)}F, 100C={celsius_to_fahrenheit(100)}F")
print(f"10km={km_to_miles(10):.2f} miles, 5kg={kg_to_pounds(5):.2f} lb")

# Error & precision (Wolfram Numerical)
true= math.pi
approx=3.14
abs_err=abs(true-approx)
rel_err=abs_err/true
print(f"\nPi true {true:.10f}, approx {approx}: abs err {abs_err:.4f}, rel {rel_err:.2%}")

# Significant figures
print(f"  3.14 has 3 sig figs, 3.141 has 4. More digits => more precision but not necessarily accuracy")

print("\n" + "="*60)
print("14.2 OPTIMIZATION & LINEAR PROGRAMMING")
print("="*60)
# mathsisfun linear-programming.html, Wolfram Optimization

# Linear programming: maximize profit given constraints
# Example: make x chairs (profit $20, wood 5, labor 2) and y tables (profit $30, wood 20, labor 6)
# Wood <=100, Labor <=36
print("Linear Programming: maximize 20x+30y s.t. 5x+20y<=100, 2x+6y<=36, x,y>=0")
# Brute force search (real simplex is more efficient, but brute for demo)
best=(0,0,0)
for x in range(0,21):
    for y in range(0,6):
        if 5*x+20*y<=100 and 2*x+6*y<=36:
            profit=20*x+30*y
            if profit>best[2]: best=(x,y,profit)
print(f"  Best brute: x={best[0]} chairs, y={best[1]} tables, profit ${best[2]}")
print(f"  Feasible region is polygon; optimum at vertex (corner) of region")

# Calculus optimization: find max of -x^2+4x+5 by derivative=0 => x=2
def f_opt(x): return -x**2+4*x+5
def fp(x): return -2*x+4
opt_x=2  # fp=0
print(f"\nCalculus opt: f(x)=-x^2+4x+5 vertex at x={opt_x}, max {f_opt(opt_x)}")
# Gradient descent for comparison
x=0.0; lr=0.2
for i in range(10):
    grad=fp(x)
    x+=lr*grad
print(f"  Gradient ascent from 0 after 10 steps x={x:.4f}, f={f_opt(x):.4f} -> approaches 2")

print("\n" + "="*60)
print("14.3 NUMERICAL ROOT FINDING")
print("="*60)
# Wolfram Numerical Methods: Newton, Bisection

def bisection(f,a,b, tol=1e-7, maxiter=50):
    assert f(a)*f(b)<0, "need sign change"
    for _ in range(maxiter):
        mid=(a+b)/2
        if abs(f(mid))<tol or (b-a)/2<tol:
            return mid
        if f(a)*f(mid)<0: b=mid
        else: a=mid
    return (a+b)/2

def newton(f, fp, x0, tol=1e-10, maxiter=50):
    x=x0
    for _ in range(maxiter):
        fx=f(x)
        if abs(fx)<tol: return x
        fpx=fp(x)
        if fpx==0: break
        x = x - fx/fpx
    return x

f=lambda x: x**2-2
fp=lambda x: 2*x
print(f"Solve x^2=2 => sqrt(2)={math.sqrt(2):.10f}")
print(f"  Bisection on [1,2]: {bisection(f,1,2):.10f}")
print(f"  Newton from 1: {newton(f,fp,1):.10f}")

# More complex: x^3 -2x -5=0 (classic Newton example)
f2=lambda x: x**3-2*x-5
fp2=lambda x: 3*x**2-2
print(f"\nSolve x^3-2x-5=0:")
print(f"  Bisection [2,3]: {bisection(f2,2,3):.8f}")
print(f"  Newton from 2: {newton(f2,fp2,2):.8f}")
print(f"  Check f(root)={f2(newton(f2,fp2,2)):.2e}")

print("\n" + "="*60)
print("14.4 NUMERICAL INTEGRATION")
print("="*60)
# mathsisfun integral-approximations.html, Wolfram Numerical Integration

def riemann_left(f,a,b,n): return sum(f(a+i*(b-a)/n)*(b-a)/n for i in range(n))
def trapezoid(f,a,b,n):
    h=(b-a)/n
    s=0.5*(f(a)+f(b))
    for i in range(1,n): s+=f(a+i*h)
    return s*h
def simpson(f,a,b,n):
    if n%2: n+=1
    h=(b-a)/n
    s=f(a)+f(b)
    for i in range(1,n):
        s+= (4 if i%2 else 2)*f(a+i*h)
    return s*h/3
def monte_carlo_int(f,a,b,samples=10000):
    # average f * width
    s=sum(f(random.random()*(b-a)+a) for _ in range(samples))
    return s/samples*(b-a)

true_int=2  # int 0..pi sin =2
print(f"Integral sin 0..pi true {true_int}:")
for n in [10,100]:
    print(f"  n={n}: Left Riemann {riemann_left(math.sin,0,math.pi,n):.6f}, Trap {trapezoid(math.sin,0,math.pi,n):.6f}, Simpson {simpson(math.sin,0,math.pi,n):.6f}")
print(f"  Monte Carlo 100k: {monte_carlo_int(math.sin,0,math.pi,100000):.6f}")

# Gaussian quadrature preview (more accurate)

print("\n" + "="*60)
print("14.5 ORDINARY DIFFERENTIAL EQUATIONS - Euler vs RK4")
print("="*60)
# mathsisfun differential equations, Wolfram ODE

def euler(f, y0, t0, tn, steps):
    h=(tn-t0)/steps
    t,y=t0,y0
    traj=[(t,y)]
    for _ in range(steps):
        y+=h*f(t,y)
        t+=h
        traj.append((t,y))
    return traj

def rk4(f, y0, t0, tn, steps):
    h=(tn-t0)/steps
    t,y=t0,y0
    traj=[(t,y)]
    for _ in range(steps):
        k1=f(t,y)
        k2=f(t+h/2, y+h*k1/2)
        k3=f(t+h/2, y+h*k2/2)
        k4=f(t+h, y+h*k3)
        y+=h*(k1+2*k2+2*k3+k4)/6
        t+=h
        traj.append((t,y))
    return traj

# ODE: y' = y, y(0)=1 => y=e^t
f_ode=lambda t,y: y
true=lambda t: math.exp(t)
eul=euler(f_ode,1,0,1,10)[-1][1]
rk=rk4(f_ode,1,0,1,10)[-1][1]
print(f"y'=y, y0=1, up to t=1 (10 steps): Euler {eul:.6f}, RK4 {rk:.6f}, true e={math.e:.6f}")
print(f"  Error Euler {abs(eul-math.e):.4f}, RK4 {abs(rk-math.e):.8f} (RK4 vastly better!)")

# Second: y' = -2 y, decay
f2=lambda t,y: -2*y
print(f"\nDecay y'=-2y, y0=10, t=1: true {10*math.exp(-2):.4f}, Euler 10 steps {euler(f2,10,0,1,10)[-1][1]:.4f}, RK4 {rk4(f2,10,0,1,10)[-1][1]:.4f}")

print("\n" + "="*60)
print("14.6 INTERPOLATION & CURVE FITTING")
print("="*60)

# Linear interpolation
def lerp(x0,y0,x1,y1,x): return y0 + (y1-y0)*(x-x0)/(x1-x0)
print(f"Linear interp between (0,0) and (2,4) at x=1 => {lerp(0,0,2,4,1)} (true line y=2x)")

# Lagrange polynomial interpolation (Wolfram Interpolating Polynomial)
def lagrange_interpolate(points, x):
    total=0
    for i,(xi, yi) in enumerate(points):
        term=yi
        for j,(xj, _) in enumerate(points):
            if i!=j:
                term*= (x - xj)/(xi - xj)
        total+=term
    return total

pts=[(0,0),(1,1),(2,4)]  # y=x^2
for x in [0.5,1.5,3]:
    print(f"  Interp {pts} at x={x}: {lagrange_interpolate(pts,x):.3f} (true {x**2:.1f})")

# Least squares already in 13

# Rates (mathsisfun rates.html)
print(f"\nRates: speed = distance/time")
print(f"  120 km in 2h = {120/2} km/h")

if PLOT:
    try:
        import matplotlib.pyplot as plt, numpy as np
        # Optimization contour
        xs=np.linspace(0,5,100)
        plt.figure(figsize=(10,4))
        plt.subplot(1,2,1)
        # feasible region
        plt.fill_between([0,20], 0, [ (100-5*x)/20 if 100-5*x>0 else 0 for x in [0,20]], alpha=0.2, label='wood <=100')
        plt.fill_between([0,18], 0, [ (36-2*x)/6 if 36-2*x>0 else 0 for x in [0,18]], alpha=0.2, label='labor <=36')
        # profit lines
        for profit in [40,80,120]:
            ys=[ (profit-20*x)/30 for x in xs]
            plt.plot(xs, ys, '--', label=f'profit {profit}')
        plt.plot(best[0], best[1], 'ro', label=f'opt {best}')
        plt.xlim(0,10); plt.ylim(0,6); plt.xlabel("x chairs"); plt.ylabel("y tables")
        plt.title("Linear Programming Feasible Region"); plt.legend(); plt.grid(True)

        plt.subplot(1,2,2)
        xs=np.linspace(-1,4,200); ys=[f_opt(x) for x in xs]
        plt.plot(xs,ys, label='-x^2+4x+5')
        plt.plot(opt_x, f_opt(opt_x), 'ro', label='max')
        plt.legend(); plt.grid(True); plt.title("Optimization vertex")
        plt.tight_layout(); plt.show()

        # Convergence of methods
        xs=np.linspace(0,1,5)
        # Show RK4 vs Euler trajectory
        t_e=[p[0] for p in euler(f_ode,1,0,2,10)]
        y_e=[p[1] for p in euler(f_ode,1,0,2,10)]
        t_r=[p[0] for p in rk4(f_ode,1,0,2,10)]
        y_r=[p[1] for p in rk4(f_ode,1,0,2,10)]
        t_true=np.linspace(0,2,100); y_true=np.exp(t_true)
        plt.figure()
        plt.plot(t_true, y_true, 'k-', label='true e^t')
        plt.plot(t_e, y_e, 'o-', label='Euler')
        plt.plot(t_r, y_r, 's-', label='RK4')
        plt.legend(); plt.grid(True); plt.title("ODE y'=y: Euler vs RK4 (10 steps)"); plt.show()

        # Interpolation
        xs=np.linspace(-0.5,2.5,200)
        ys=[lagrange_interpolate(pts,x) for x in xs]
        plt.figure()
        plt.plot(xs, ys, label='Lagrange (through 3 points)')
        plt.plot(xs, [x**2 for x in xs], '--', label='true x^2')
        plt.scatter([p[0] for p in pts], [p[1] for p in pts], c='red', s=80)
        plt.legend(); plt.grid(True); plt.title("Lagrange Interpolation"); plt.show()
    except Exception as e: print(e)
else:
    print("\n[Tip] --plot for LP region & ODE: python 14_applied_numerical.py --plot")

print("\nChallenge: implement simplex algorithm, or solve 2D heat equation via finite differences!")
