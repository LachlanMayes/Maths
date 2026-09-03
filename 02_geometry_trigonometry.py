"""
02 - GEOMETRY & TRIGONOMETRY
Source: https://www.mathsisfun.com/geometry/index.html
        https://www.mathsisfun.com/algebra/trigonometry.html
Run: python 02_geometry_trigonometry.py
Add --plot to show graphs (needs matplotlib)
"""
import math
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except: pass

PLOT = "--plot" in sys.argv

print("="*60)
print("2.1 GEOMETRY - Areas & Volumes")
print("="*60)

# 2D shapes - mathsisfun.com/area.html
def circle_area(r): return math.pi * r**2
def circle_circumference(r): return 2 * math.pi * r
def triangle_area(base, height): return 0.5 * base * height
def triangle_area_heron(a,b,c):
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
def rectangle_area(w,h): return w*h
def trapezoid_area(a,b,h): return 0.5*(a+b)*h
def polygon_area_regular(n, side):  # n sides
    return (n * side**2) / (4 * math.tan(math.pi/n))

print(f"Circle r=5: area={circle_area(5):.2f}, circumference={circle_circumference(5):.2f}")
print(f"Triangle base=10 height=6: area={triangle_area(10,6):.2f}")
print(f"Triangle 3-4-5 via Heron: area={triangle_area_heron(3,4,5):.2f}")
print(f"Rectangle 8x6: area={rectangle_area(8,6)}")
print(f"Regular hexagon side=4: area={polygon_area_regular(6,4):.2f}")

# 3D volumes
def sphere_volume(r): return (4/3)*math.pi*r**3
def cylinder_volume(r,h): return math.pi*r**2*h
def cone_volume(r,h): return (1/3)*math.pi*r**2*h
def pyramid_volume(base_area, h): return (1/3)*base_area*h

print(f"\nSphere r=3: volume={sphere_volume(3):.2f}")
print(f"Cylinder r=2 h=5: volume={cylinder_volume(2,5):.2f}")
print(f"Cone r=2 h=5: volume={cone_volume(2,5):.2f}")

# Pythagoras - mathsisfun.com/pythagoras.html
def pythag_hypotenuse(a,b): return math.sqrt(a**2 + b**2)
def pythag_leg(c,a): return math.sqrt(c**2 - a**2)
print(f"\nPythagoras: 3^2+4^2 = {pythag_hypotenuse(3,4)}^2  -> hypotenuse 5? {pythag_hypotenuse(3,4)==5}")
print(f"Distance between (1,2) and (4,6): {math.dist([1,2],[4,6]):.2f}  # = sqrt((3)^2+(4)^2)=5")

# Estimating Pi - Archimedes & Monte Carlo (mathsisfun.com/geometry/circle.html)
print("\n" + "="*60)
print("2.2 ESTIMATING PI - Two classic methods")
print("="*60)
# Method 1: Polygon approximation (Archimedes)
def estimate_pi_polygon(n_sides):
    # inscribed polygon perimeter / diameter
    # side = 2 * sin(pi/n)
    return n_sides * math.sin(math.pi/n_sides)  # actually n*sin(pi/n) -> pi

for n in [6, 12, 96, 1000, 10000]:
    print(f"  {n:5d}-gon estimate: {estimate_pi_polygon(n):.8f} (error {abs(math.pi-estimate_pi_polygon(n)):.2e})")

# Method 2: Monte Carlo (also used later)
import random
def estimate_pi_monte_carlo(samples):
    inside = sum(1 for _ in range(samples) if random.random()**2 + random.random()**2 <= 1)
    return 4 * inside / samples

random.seed(0)
for s in [1000, 10000, 100000]:
    print(f"  Monte Carlo {s:6d} samples: {estimate_pi_monte_carlo(s):.5f}")

print("\n" + "="*60)
print("2.3 TRIGONOMETRY - Unit circle")
print("="*60)
# mathsisfun.com/algebra/trigonometry.html
# SOH CAH TOA
def deg2rad(d): return d * math.pi / 180
def rad2deg(r): return r * 180 / math.pi

print("Angle |   sin   |   cos   |   tan   |")
print("-"*40)
for deg in [0, 30, 45, 60, 90, 180, 270, 360]:
    rad = deg2rad(deg)
    s, c = math.sin(rad), math.cos(rad)
    t = math.tan(rad) if abs(c) > 1e-10 else float('inf')
    print(f"{deg:4d} deg | {s:7.4f} | {c:7.4f} | {t:7.4f}")

# Trig identities verification
print("\nTrig identities (check for 37 deg):")
angle = deg2rad(37)
print(f"  sin^2+cos^2 = {math.sin(angle)**2 + math.cos(angle)**2:.10f} (should be 1)")
print(f"  sin(2t)=2 sin(t)cos(t): {math.sin(2*angle):.6f} vs {2*math.sin(angle)*math.cos(angle):.6f}")
print(f"  cos(2t)=cos^2-sin^2: {math.cos(2*angle):.6f} vs {math.cos(angle)**2 - math.sin(angle)**2:.6f}")

# Solving triangles
print("\nSolving triangle: know 2 sides, find angles (SOH CAH TOA)")
# Right triangle, opposite=3 adjacent=4 hypotenuse=5
opp, adj, hyp = 3, 4, 5
angle_opposite_3 = rad2deg(math.asin(opp/hyp))  # opposite side 3
angle_opposite_4 = rad2deg(math.asin(adj/hyp))  # opposite side 4
print(f"  Right triangle 3-4-5: angle opposite 3 = {angle_opposite_3:.2f} deg, opposite 4 = {angle_opposite_4:.2f} deg (sum 90? {angle_opposite_3+angle_opposite_4:.1f})")

# Law of Cosines & Sines
print("\nLaws for ANY triangle:")
print("  Law of Cosines: c^2 = a^2+b^2-2ab*cos(C)")
a,b,C_deg = 7, 8, 60
C = deg2rad(C_deg)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
print(f"    a=7,b=8,C=60 deg -> c={c:.4f}")
print("  Law of Sines: a/sin(A)=b/sin(B)=c/sin(C)")
# Now we know all 3 sides, find angles
A = rad2deg(math.acos((b**2+c**2-a**2)/(2*b*c)))
B = rad2deg(math.acos((a**2+c**2-b**2)/(2*a*c)))
print(f"    Angles: A={A:.2f} deg, B={B:.2f} deg, C={C_deg} deg (sum={A+B+C_deg:.1f})")

print("\n" + "="*60)
print("2.4 COORDINATE GEOMETRY")
print("="*60)
def midpoint(p1,p2): return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
def slope(p1,p2): return (p2[1]-p1[1])/(p2[0]-p1[0]) if p2[0]!=p1[0] else float('inf')
def line_intersection(m1,b1,m2,b2): # y=mx+b
    if m1==m2: return None
    x = (b2-b1)/(m1-m2)
    return (x, m1*x+b1)

p1, p2 = (1,2), (5,10)
print(f"Points {p1} and {p2}: midpoint={midpoint(p1,p2)}, distance={math.dist(p1,p2):.2f}, slope={slope(p1,p2):.2f}")
print(f"Line y=2x+1 intersects y=-x+7 at {line_intersection(2,1,-1,7)}")

# --- Optional plots ---
if PLOT:
    try:
        import numpy as np
        import matplotlib.pyplot as plt

        x = np.linspace(-2*math.pi, 2*math.pi, 500)
        plt.figure(figsize=(10,4))
        plt.plot(x, np.sin(x), label='sin(x)')
        plt.plot(x, np.cos(x), label='cos(x)')
        plt.plot(x, np.tan(x), label='tan(x)', alpha=0.5)
        plt.ylim(-2,2)
        plt.axhline(0,color='black',linewidth=0.5)
        plt.axvline(0,color='black',linewidth=0.5)
        plt.title("Sine, Cosine, Tangent (Unit Circle Waves)")
        plt.legend(); plt.grid(True); plt.show()

        # Unit circle
        theta = np.linspace(0, 2*math.pi, 400)
        plt.figure(figsize=(5,5))
        plt.plot(np.cos(theta), np.sin(theta), label='Unit circle')
        for deg in [0,30,45,60,90,180,270]:
            r=deg2rad(deg)
            plt.plot([0,math.cos(r)],[0,math.sin(r)],'--')
            plt.text(math.cos(r)*1.05, math.sin(r)*1.05, f"{deg}°")
        plt.axis('equal'); plt.grid(True); plt.title("Unit Circle"); plt.show()

        # Pi estimation convergence
        ns = [6,12,24,48,96,200,500,1000,5000]
        pis = [estimate_pi_polygon(n) for n in ns]
        plt.figure()
        plt.semilogx(ns, pis, 'o-')
        plt.axhline(math.pi, color='red', linestyle='--', label='True pi')
        plt.title("Archimedes Polygon Pi Approximation"); plt.xlabel("n sides"); plt.ylabel("estimate")
        plt.legend(); plt.grid(True); plt.show()

    except ImportError:
        print("Install matplotlib + numpy for plots: pip install matplotlib numpy")
else:
    print("\n[Tip] Run with --plot to see graphs: python 02_geometry_trigonometry.py --plot")

print("\n[Challenge] Can you?")
print(" - Compute area of a star polygon?")
print(" - Animate a point moving around the unit circle?")
print(" - Prove pi is irrational? (see arxiv.org/abs/math/0609485)")
