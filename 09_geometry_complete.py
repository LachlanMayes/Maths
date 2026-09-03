"""
09 - GEOMETRY COMPLETE: Plane, Solid, Polygons, Circles, Conics, Polyhedra
Sources:
  - https://www.mathsisfun.com/geometry/index.html
  - https://www.mathsisfun.com/geometry/conic-sections.html, ellipse.html, parabola.html, hyperbola.html
  - https://mathworld.wolfram.com/topics/Geometry.html
Run: python 09_geometry_complete.py [--plot]
"""
import sys
try: sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
except: pass
import math

PLOT="--plot" in sys.argv

print("="*60)
print("9.1 PLANE GEOMETRY - Points, Lines, Angles, Polygons")
print("="*60)
# mathsisfun plane-geometry.html

# Angles around point sum 360, triangle 180
print(f"Triangle interior sum 180: 60+60+60={60+60+60}, right 90+45+45={90+45+45}")
# Polygon interior angles: (n-2)*180
for n in [3,4,5,6,8,12]:
    total=(n-2)*180
    each=total/n
    print(f"  {n}-gon interior total {total} deg, each regular {each:.1f} deg")
# Exterior always 360
print(f"  Exterior sum always 360: 6-gon each exterior {360/6} deg")

# Area formulas (mathsisfun area.html)
def area_triangle(b,h): return 0.5*b*h
def area_trapezoid(a,b,h): return 0.5*(a+b)*h
def area_polygon_regular(n, side):
    return n*side**2/(4*math.tan(math.pi/n))
def area_circle(r): return math.pi*r**2
def area_ellipse(a,b): return math.pi*a*b

print(f"\nAreas:")
print(f"  Triangle 10x6={area_triangle(10,6)}, Trapezoid a=3 b=5 h=4={area_trapezoid(3,5,4)}")
print(f"  Pentagon side 4={area_polygon_regular(5,4):.2f}, Circle r3={area_circle(3):.2f}, Ellipse 3x2={area_ellipse(3,2):.2f}")

# Perimeter
print(f"  Circle circumference r5={2*math.pi*5:.2f}, Pentagon perimeter side4 n5={5*4}")

print("\n" + "="*60)
print("9.2 TRIANGLES, QUADRILATERALS, CIRCLES")
print("="*60)

# Triangle centers (Wolfram TriangleCenters)
# centroid = average of vertices
def centroid(pts): return (sum(p[0] for p in pts)/len(pts), sum(p[1] for p in pts)/len(pts))
tri=[(0,0),(4,0),(2,3)]
print(f"Triangle {tri}: centroid {centroid(tri)}, area {abs(tri[0][0]*(tri[1][1]-tri[2][1])+tri[1][0]*(tri[2][1]-tri[0][1])+tri[2][0]*(tri[0][1]-tri[1][1]))/2}")

# Quadrilaterals classification (mathsisfun)
print(f"\nQuadrilaterals: Square (4 equal sides, 4 right), Rectangle (opposite equal), Rhombus (4 equal sides), Parallelogram, Trapezoid")
print(f"  Property: sum interior =360 for any quadrilateral")

# Circle theorems (mathsisfun circle-theorems.html)
print(f"\nCircle theorems:")
print(f"  Angle at centre =2* angle at circumference: 80 at centre => 40 at circumference")
print(f"  Tangent is perpendicular to radius")
print(f"  Two radii + chord = isosceles triangle")
r=5
chord=6
distance_from_center=math.sqrt(r**2-(chord/2)**2)
print(f"  Circle r={r}, chord length {chord}: distance from centre={distance_from_center:.2f}")
arc_angle=60  # degrees
arc_length=2*math.pi*r*arc_angle/360
sector_area=math.pi*r**2*arc_angle/360
segment_area=sector_area - 0.5*r**2*math.sin(math.radians(arc_angle))
print(f"  Arc {arc_angle} deg: length {arc_length:.2f}, sector {sector_area:.2f}, segment {segment_area:.2f}")

# Annulus
R,r=5,3
print(f"  Annulus R={R} r={r}: area {math.pi*(R**2-r**2):.2f}")

print("\n" + "="*60)
print("9.3 CONIC SECTIONS - mathsisfun/conic-sections.html")
print("="*60)
# Wolfram ConicSections

# Definition: eccentricity e = distance to focus / distance to directrix
# e=0 circle, 0<e<1 ellipse, e=1 parabola, e>1 hyperbola
print(f"Eccentricity: circle 0, ellipse 0<e<1, parabola 1, hyperbola >1")

# Ellipse: sum distances to foci =2a
def ellipse_properties(a,b): # a semi-major, b semi-minor (a>=b)
    c=math.sqrt(a**2-b**2) # focal distance
    e=c/a
    area=math.pi*a*b
    # perimeter approximation Ramanujan
    h=((a-b)/(a+b))**2
    perim=math.pi*(a+b)*(1+3*h/(10+math.sqrt(4-3*h)))
    return c,e,area,perim

a,b=5,3
c,e,area,perim=ellipse_properties(a,b)
print(f"Ellipse a={a}, b={b}: c={c:.2f}, e={e:.2f}, area={area:.2f}, perimeter approx {perim:.2f}")

# Parabola y = a x^2 (focus at (0,1/(4a)))
def parabola_focus(a): return 1/(4*a)
a=0.5
print(f"Parabola y={a}x^2: focus (0,{parabola_focus(a):.2f}), directrix y={-parabola_focus(a):.2f}, focal length {parabola_focus(a):.2f}")

# Hyperbola x^2/a^2 - y^2/b^2=1, e= sqrt(1+b^2/a^2)
def hyperbola_e(a,b): return math.sqrt(1+b**2/a**2)
a,b=4,3
print(f"Hyperbola x^2/{a}^2 - y^2/{b}^2=1: e={hyperbola_e(a,b):.2f}, asymptotes y=+-{b/a:.2f} x")

print("\n" + "="*60)
print("9.4 SOLID GEOMETRY - Polyhedra, Prisms, Spheres")
print("="*60)
# mathsisfun solid-geometry.html, common-3d-shapes.html, platonic solids

def volume_cube(s): return s**3
def volume_cuboid(l,w,h): return l*w*h
def volume_sphere(r): return 4/3*math.pi*r**3
def volume_cylinder(r,h): return math.pi*r**2*h
def volume_cone(r,h): return 1/3*math.pi*r**2*h
def volume_pyramid(base, h): return 1/3*base*h
def volume_torus(R,r): return 2*math.pi**2*R*r**2  # R major, r minor

print(f"Volume cube s3={volume_cube(3)}, cuboid 2x3x4={volume_cuboid(2,3,4)}")
print(f"Sphere r3={volume_sphere(3):.2f}, Cylinder r2 h5={volume_cylinder(2,5):.2f}")
print(f"Cone r2 h5={volume_cone(2,5):.2f}, Square pyramid base16 h6={volume_pyramid(16,6):.2f}")
print(f"Torus R5 r1={volume_torus(5,1):.2f}")

# Surface areas
def sa_sphere(r): return 4*math.pi*r**2
def sa_cylinder(r,h): return 2*math.pi*r*(r+h)
def sa_cone(r,h): return math.pi*r*(r+math.sqrt(h**2+r**2))

print(f"\nSurface area sphere r3={sa_sphere(3):.2f}, cylinder r2 h5={sa_cylinder(2,5):.2f}, cone r2 h5={sa_cone(2,5):.2f}")

# Platonic solids (mathsisfun platonic_solids.html, Wolfram)
platonic=[
    ("Tetrahedron",4,4,6),
    ("Cube",8,6,12),
    ("Octahedron",6,8,12),
    ("Dodecahedron",20,12,30),
    ("Icosahedron",12,20,30),
]
print(f"\nPlatonic solids (only 5!):")
print(f"  Name            V  F  E  V-E+F (Euler)")
for name,V,F,E in platonic:
    print(f"  {name:14s} {V:2d} {F:2d} {E:2d}  {V-E+F} (always 2 for convex)")

# Euler's formula V - E + F =2 (mathsisfun eulers-formula.html, Wolfram)
print(f"\nEuler's formula: V - E + F =2 holds for convex polyhedra")
print(f"  Cube: 8-12+6=2, Tetra:4-6+4=2, proven!")

# Cross sections (mathsisfun cross-sections.html)
print(f"\nCross sections: sphere->circle, cone->circle/ellipse/parabola/hyperbola (conics!), cylinder->rectangle/circle")

# Pythagoras in 3D
def pythag_3d(a,b,c): return math.sqrt(a**2+b**2+c**2)
print(f"\nPythagoras in 3D: diagonal of box 3x4x12 = {pythag_3d(3,4,12):.1f} (3-4-12-13 triple)")

print("\n" + "="*60)
print("9.5 TRANSFORMATIONS & SYMMETRY")
print("="*60)
# mathsisfun transformations.html, symmetry.html

# Using matrices for transformations (link to linear algebra)
def rotate_point(x,y,deg):
    rad=math.radians(deg)
    return (x*math.cos(rad)-y*math.sin(rad), x*math.sin(rad)+y*math.cos(rad))
def reflect_x(x,y): return (x,-y)
def translate(x,y,dx,dy): return (x+dx,y+dy)
def scale(x,y,sx,sy): return (x*sx, y*sy)

p=(1,0)
print(f"Point {p}:")
print(f"  Rotate 90 deg -> {rotate_point(*p,90)} (should be (0,1))")
print(f"  Reflect over x-axis -> {reflect_x(*p)}")
print(f"  Translate (2,3) -> {translate(*p,2,3)}")
print(f"  Scale 2x -> {scale(*p,2,2)}")

# Symmetry
print(f"\nSymmetry:")
print(f"  Square: 4 reflection lines, rotational order 4 (90 deg)")
print(f"  Equilateral triangle: 3 lines, order 3 (120 deg)")
print(f"  Circle: infinite lines and rotational")

# Tessellations (mathsisfun tessellation.html)
print(f"\nTessellations: only triangles, squares, hexagons tile plane regularly (360/n integer)")
print(f"  3.6.3.6 and 4.8.8 are semi-regular")
print(f"  Penrose tiles are aperiodic (arXiv style)")

# Coordinate geometry distance & midpoint (mathsisfun)
def dist(p,q): return math.dist(p,q)
def midpoint(p,q): return ((p[0]+q[0])/2,(p[1]+q[1])/2)
p,q=(1,2),(5,6)
print(f"\nCoordinates: {p} to {q}: distance {dist(p,q):.2f}, midpoint {midpoint(p,q)}")

if PLOT:
    try:
        import numpy as np, matplotlib.pyplot as plt
        # Conics
        fig, axes=plt.subplots(2,2, figsize=(10,8))
        # Ellipse
        t=np.linspace(0,2*math.pi,200)
        a,b=5,3
        axes[0,0].plot(a*np.cos(t), b*np.sin(t))
        axes[0,0].set_title(f"Ellipse a={a}, b={b}, e={math.sqrt(a**2-b**2)/a:.2f}")
        axes[0,0].set_aspect('equal'); axes[0,0].grid(True)
        # Parabola
        x=np.linspace(-5,5,200)
        axes[0,1].plot(x, 0.5*x**2)
        axes[0,1].set_title("Parabola y=0.5 x^2"); axes[0,1].grid(True)
        # Hyperbola
        x2=np.linspace(2,6,200)
        axes[1,0].plot(x2, 3*np.sqrt((x2/4)**2-1), 'b')
        axes[1,0].plot(x2, -3*np.sqrt((x2/4)**2-1), 'b')
        axes[1,0].plot(-x2, 3*np.sqrt((x2/4)**2-1), 'b')
        axes[1,0].plot(-x2, -3*np.sqrt((x2/4)**2-1), 'b')
        axes[1,0].set_title("Hyperbola x^2/16 - y^2/9=1"); axes[1,0].grid(True)
        # Circle with chord
        axes[1,1].add_patch(plt.Circle((0,0),5, fill=False, color='blue'))
        axes[1,1].plot([-3,3],[4,4],'r', label='chord len 6')
        axes[1,1].set_aspect('equal'); axes[1,1].grid(True); axes[1,1].set_title("Circle r=5 chord"); axes[1,1].legend()
        plt.tight_layout(); plt.show()

        # Polyhedra net idea
        fig=plt.figure()
        ax=fig.add_subplot(111, projection='3d')
        # Cube
        r=[0,1]
        for s,e in [[(0,0,0),(1,0,0)],[(0,0,0),(0,1,0)],[(0,0,0),(0,0,1)]]:
            ax.plot([s[0],e[0]],[s[1],e[1]],[s[2],e[2]],'k-')
        ax.set_title("Cube edges (wireframe teaser)"); plt.show()
    except Exception as e:
        print(e)
else:
    print("\n[Tip] Run with --plot for conics & circle: python 09_geometry_complete.py --plot")

print("\nChallenge: prove only 5 Platonic solids, or animate conic sections as plane cuts cone!")
