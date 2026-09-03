"""
10 - TRIGONOMETRY & COMPLEX NUMBERS
Sources:
  - https://www.mathsisfun.com/algebra/trigonometry.html
  - https://www.mathsisfun.com/algebra/trigonometry-index.html
  - https://mathworld.wolfram.com/Trigonometry.html
  - https://mathworld.wolfram.com/ComplexNumber.html
  - arXiv: math.CA (Complex Analysis)
Run: python 10_trigonometry_complex.py [--plot]
"""
import sys
try: sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
except: pass
import math, cmath

PLOT="--plot" in sys.argv

print("="*60)
print("10.1 TRIG BASICS & UNIT CIRCLE")
print("="*60)
# mathsisfun introduction

def deg2rad(d): return d*math.pi/180
def rad2deg(r): return r*180/math.pi

print("Degrees to radians: 180 deg = pi rad = ", deg2rad(180))
print("Common: 30 deg=pi/6, 45=pi/4, 60=pi/3, 90=pi/2, 360=2pi")

# SOH CAH TOA
print("\nSOH CAH TOA (right triangle):")
hyp=10
for deg in [30,45,60]:
    opp=hyp*math.sin(deg2rad(deg))
    adj=hyp*math.cos(deg2rad(deg))
    print(f"  {deg} deg, hyp {hyp}: opp={opp:.2f}, adj={adj:.2f}, check opp^2+adj^2={math.sqrt(opp**2+adj**2):.1f}")

print("\nUnit circle values (exact from math):")
for deg in [0,30,45,60,90,120,180,270,360]:
    rad=deg2rad(deg)
    print(f"  {deg:3d} deg: sin {math.sin(rad):7.4f}, cos {math.cos(rad):7.4f}, tan {math.tan(rad) if abs(math.cos(rad))>1e-9 else float('inf'):7.4f}")

print("\n" + "="*60)
print("10.2 TRIG IDENTITIES (MathWorld Trigonometry)")
print("="*60)
# Pythagorean, double-angle, sum, etc. - verify numeric

def verify(a=0.6,b=0.8):
    # use radians
    checks=[]
    # sin^2+cos^2=1
    checks.append(("sin^2+cos^2=1", abs(math.sin(a)**2+math.cos(a)**2-1)<1e-9))
    # sin(A+B)=sinA cosB+cosA sinB
    checks.append(("sin(a+b)", abs(math.sin(a+b)-(math.sin(a)*math.cos(b)+math.cos(a)*math.sin(b)))<1e-9))
    checks.append(("cos(a+b)", abs(math.cos(a+b)-(math.cos(a)*math.cos(b)-math.sin(a)*math.sin(b)))<1e-9))
    # double angle
    checks.append(("sin2a", abs(math.sin(2*a)-2*math.sin(a)*math.cos(a))<1e-9))
    checks.append(("cos2a", abs(math.cos(2*a)-(math.cos(a)**2-math.sin(a)**2))<1e-9))
    # tan
    checks.append(("tan = sin/cos", abs(math.tan(a)-math.sin(a)/math.cos(a))<1e-9 if math.cos(a)!=0 else True))
    return checks

for name, ok in verify():
    print(f"  {name:20s}: {'PASS' if ok else 'FAIL'}")

print("\nDerived identities:")
print("  1+tan^2 = sec^2, 1+cot^2=csc^2")
a=0.7
print(f"    a=0.7: 1+tan^2={1+math.tan(a)**2:.4f}, sec^2={1/math.cos(a)**2:.4f}")

# Law of sines/cosines already in 02, quick recall
print(f"\nLaw of Sines: a/sinA = b/sinB =2R (circumradius)")
a,b,A_deg=7,10,40
A=deg2rad(A_deg)
# find B using law of sines if known? demo
print(f"  Example: a=7, b=10, A=40deg -> sinB = b*sinA/a = {10*math.sin(A)/7:.4f} => B approx {rad2deg(math.asin(10*math.sin(A)/7)):.1f} or {180-rad2deg(math.asin(10*math.sin(A)/7)):.1f} (ambiguous!)")

print("\n" + "="*60)
print("10.3 COMPLEX NUMBERS (MathWorld ComplexNumber)")
print("="*60)
# mathsisfun: not indexed but Wolframex extensive; also algebra/complex

z1=3+4j
z2=1-2j
print(f"z1={z1}, |z1|={abs(z1)} (modulus), arg={cmath.phase(z1):.4f} rad = {rad2deg(cmath.phase(z1)):.1f} deg")
print(f"z2={z2}")
print(f"  z1+z2={z1+z2}, z1*z2={z1*z2}, z1/z2={z1/z2:.4f}")
print(f"  conjugate z1* = {z1.conjugate()}, z1 * conj = {z1*z1.conjugate()} = |z1|^2 = {abs(z1)**2}")
print(f"  Re={z1.real}, Im={z1.imag}")

# Polar form: r(cos theta + i sin theta)
r=abs(z1); theta=cmath.phase(z1)
print(f"\nPolar: z1 = {r:.2f} * (cos {theta:.3f} + i sin {theta:.3f}) = {r*math.cos(theta):.1f}+{r*math.sin(theta):.1f}i check {z1}")

# Euler's formula: e^{i theta} = cos theta + i sin theta (Wolfram)
print(f"\nEuler's formula: e^(i theta)=cos theta + i sin theta")
for deg in [0,90,180,270]:
    th=deg2rad(deg)
    euler=cmath.exp(1j*th)
    print(f"  e^(i*{deg}deg) = {euler:.4f}, cos+ i sin = {math.cos(th):.4f}+{math.sin(th):.4f}i")
# Famous: e^{i pi}+1=0
print(f"  Euler's identity: e^(i pi)+1 = {cmath.exp(1j*math.pi)+1:.4f} (should be 0)")
# De Moivre: (cos+ i sin)^n = cos n theta + i sin n theta
n=3; th=deg2rad(30)
left=(math.cos(th)+1j*math.sin(th))**n
right=math.cos(n*th)+1j*math.sin(n*th)
print(f"\nDe Moivre: (cos30+i sin30)^3 = {left:.4f} vs cos90+i sin90={right:.4f} equal? {abs(left-right)<1e-9}")

# Roots of unity
print(f"\nRoots of unity: solutions to z^5=1")
for k in range(5):
    root=cmath.exp(2j*math.pi*k/5)
    print(f"  k={k}: {root:.4f} magnitude {abs(root):.1f}, power 5 = {root**5:.4f}")

# Complex quadratic: x^2+1=0 => +/- i
print(f"\nComplex solves x^2+1=0: roots {cmath.sqrt(-1)}, {-cmath.sqrt(-1)} (both i)")
# Quadratic with complex roots: x^2+2x+5=0
a,b,c=1,2,5
disc=b*b-4*a*c
r1=(-b+cmath.sqrt(disc))/(2*a)
r2=(-b-cmath.sqrt(disc))/(2*a)
print(f"  x^2+2x+5=0: disc {disc}, roots {r1:.3f}, {r2:.3f}")

print("\n" + "="*60)
print("10.4 TRIG EQUATIONS & INVERSE TRIG")
print("="*60)
# Solve sin x =0.5 => x=30deg +360k or 150deg+360k
print(f"Solve sin x=0.5: x=30 deg +360k or 150 deg+360k")
for k in [0,1]:
    for base in [30,150]:
        print(f"  k={k}: {base+360*k} deg -> sin={math.sin(deg2rad(base+360*k)):.4f}")

print(f"\nInverse trig (principal values):")
print(f"  arcsin(0.5)={rad2deg(math.asin(0.5)):.1f} deg, arccos(0.5)={rad2deg(math.acos(0.5)):.1f}, arctan(1)={rad2deg(math.atan(1)):.1f}")
print(f"  atan2(y,x) for quadrant: atan2(1,-1)={rad2deg(math.atan2(1,-1)):.1f} deg (135)")
# atan2 handles all quadrants

print("\n" + "="*60)
print("10.5 APPLICATIONS: Waves & Phasors")
print("="*60)
# Trig models waves
print(f"Wave: y= A sin(omega t + phi), A amplitude, omega=2pi f")
A,f=2,1
for t in [0,0.25,0.5,0.75,1]:
    y=A*math.sin(2*math.pi*f*t)
    print(f"  t={t:.2f}: y={y:.3f}")

# Phasor: complex represents wave
print(f"\nPhasor: wave as complex e^{{i wt}} real part is wave")
t=0.25
phasor=cmath.exp(2j*math.pi*f*t)
print(f"  t=0.25, phasor={phasor:.3f}, real={phasor.real:.3f} (sin phase shifted)")

# Fourier preview (link to 11)
print(f"  Sum of waves = complex superposition (Fourier)")

if PLOT:
    try:
        import numpy as np, matplotlib.pyplot as plt
        x=np.linspace(-2*math.pi,2*math.pi,500)
        fig, axes=plt.subplots(2,2, figsize=(12,8))
        axes[0,0].plot(x, np.sin(x), label='sin'); axes[0,0].plot(x, np.cos(x), label='cos')
        axes[0,0].plot(x, np.tan(x), label='tan'); axes[0,0].set_ylim(-3,3)
        axes[0,0].set_title("Basic Trig"); axes[0,0].legend(); axes[0,0].grid(True)

        # Unit circle with complex
        th=np.linspace(0,2*math.pi,100)
        axes[0,1].plot(np.cos(th), np.sin(th), 'b')
        for deg in [0,30,45,60,90,180]:
            r=deg2rad(deg); axes[0,1].plot([0,math.cos(r)],[0,math.sin(r)],'r--')
            axes[0,1].text(math.cos(r)*1.1, math.sin(r)*1.1, f"{deg}°")
        axes[0,1].set_aspect('equal'); axes[0,1].grid(True); axes[0,1].set_title("Complex as unit circle e^{i theta}")

        # Euler's spiral?
        axes[1,0].plot(x, np.sin(x)+np.sin(3*x)/3, label='square approx')
        axes[1,0].set_title("Fourier sum: sin x + sin 3x/3 (square wave 2 terms)"); axes[1,0].grid(True); axes[1,0].legend()

        # Inverse trig
        xs=np.linspace(-1,1,200)
        axes[1,1].plot(xs, np.arcsin(xs), label='arcsin')
        axes[1,1].plot(xs, np.arccos(xs), label='arccos')
        axes[1,1].set_title("Inverse trig"); axes[1,1].legend(); axes[1,1].grid(True)

        plt.tight_layout(); plt.show()

        # 3D complex plane
        fig=plt.figure()
        ax=fig.add_subplot(111, projection='3d')
        th=np.linspace(0,4*math.pi,200)
        ax.plot(np.cos(th), np.sin(th), th/ (2*math.pi), label='helix e^{i t}')
        ax.set_title("Helix: complex exponential over t"); plt.show()
    except Exception as e: print(e)
else:
    print("\n[Tip] --plot for unit circle & waves: python 10_trigonometry_complex.py --plot")

print("\nChallenge: implement FFT, or solve triangle with complex numbers!")
