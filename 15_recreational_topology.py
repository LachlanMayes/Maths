"""
15 - RECREATIONAL MATHS, TOPOLOGY & HISTORY
Sources:
  - https://mathworld.wolfram.com/topics/RecreationalMathematics.html
  - https://mathworld.wolfram.com/topics/Topology.html
  - https://mathworld.wolfram.com/topics/HistoryandTerminology.html
  - https://www.mathsisfun.com/activity/index.html, puzzles
  - https://www.mathsisfun.com/geometry/tessellation.html, symmetry.html
Run: python 15_recreational_topology.py [--plot]
"""
import sys
try: sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
except: pass
import math, random, itertools

PLOT="--plot" in sys.argv

print("="*60)
print("15.1 RECREATIONAL MATHS - Puzzles & Games (Wolfram)")
print("="*60)
# Wolfram Recreational: puzzles, magic squares, etc.

# Magic square 3x3 (Lo Shu)
magic=[[8,1,6],[3,5,7],[4,9,2]]
print(f"Magic square 3x3 (Lo Shu):")
for row in magic: print(" ",row, "sum",sum(row))
print(f"  Cols {[sum(magic[r][c] for r in range(3)) for c in range(3)]}, diags {magic[0][0]+magic[1][1]+magic[2][2]}, {magic[0][2]+magic[1][1]+magic[2][0]} all 15!")

# 15-puzzle idea, Tower of Hanoi
def hanoi(n, source, target, aux, moves=None):
    if moves is None: moves=[]
    if n==1: moves.append((source,target))
    else:
        hanoi(n-1, source, aux, target, moves)
        moves.append((source,target))
        hanoi(n-1, aux, target, source, moves)
    return moves
moves=hanoi(3,'A','C','B')
print(f"\nTower of Hanoi 3 disks minimum moves {len(moves)} (=2^3-1): {moves[:5]}...")

# Game theory (mathsisfun)
print(f"\nGame Theory (mathsisfun sets/game-theory.html):")
print(f"  Zero-sum: Tic-Tac-Toe, optimal play => draw")
print(f"  Winning strategy: take-last-stone (Nim) - XOR of piles (Sprague-Grundy)")

def nim_xor(piles): 
    x=0
    for p in piles: x^=p
    return x
print(f"  Nim piles [3,4,5] xor={nim_xor([3,4,5])} (non-zero => winning for next player)")

# Benford's Law (mathsisfun, Wolfram)
print(f"\nBenford's Law: first digit frequencies (1 is ~30%, not 11%)")
print(f"  Found in natural data, used for fraud detection (arXiv style)")

print("\n" + "="*60)
print("15.2 TESSALATIONS & SYMMETRY (mathsisfun)")
print("="*60)

print(f"Regular tessellations only 3: triangles (6 around point), squares (4), hexagons (3)")
print(f"  Because interior angle must divide 360: 60,90,120")
print(f"Semi-regular (Archimedean): 8 types e.g., 3.6.3.6 (tri+hex), 4.8.8 (square+octagon)")
print(f"Escher-style: distorted tessellations via translation/rotation")
print(f"Penrose: aperiodic 2 tiles (kite+darts) never repeats - won Nobel-related (quasicrystals)")

# Symmetry demo counting
def count_symmetry(shape):
    # toy: square has D4
    return {"triangle": ("3 rotations (120), 3 reflections"), "square": ("4 rotations, 4 reflections, D4"), "circle": ("infinite")}
for s in ["triangle","square","circle"]:
    print(f"  {s}: {count_symmetry(s)[s] if s in count_symmetry(s) else 'many'}")

print("\n" + "="*60)
print("15.3 TOPOLOGY - Coffee cup = donut (Wolfram Topology)")
print("="*60)

print(f"Topology: studies properties preserved under stretching (not tearing) = homeomorphism")
print(f"  Famous: coffee cup homeomorphic to donut (both genus 1, one hole)")
print(f"  Sphere genus 0, torus genus 1, double torus genus 2")

# Euler characteristic: V - E + F = 2 - 2g (g=genus)
for genus, name in [(0,"sphere"),(1,"torus"),(2,"double torus")]:
    chi=2-2*genus
    print(f"  {name}: genus {genus}, Euler chi={chi}")

# Knot theory (Wolfram Knot)
print(f"\nKnot theory (Wolfram):")
print(f"  Unknot (trivial), trefoil (3_1) simplest nontrivial, figure-eight (4_1)")
print(f"  Crossing number, invariants: Jones polynomial (Fields medal)")
print(f"  Demo: trefoil cannot be untied without cutting")

# Mobius strip (mathsisfun activity)
print(f"\nMobius strip: take paper strip, half-twist, join ends => one side, one edge")
print(f"  Cut along centre: becomes one long loop with 2 twists (not two loops!)")
print(f"  Klein bottle: Mobius extended, no inside/outside, needs 4D to embed without self-intersection")

# Four Color Theorem (Wolfram, mathsisfun coloring)
print(f"\nFour Color Theorem: any planar map needs <=4 colors (no adjacent same)")
print(f"  First theorem proved by computer (Appel-Haken 1976, 1478 cases), now formal proof")
print(f"  Example: map of USA needs 4 (Nevada touches 5 states in ring)")

def greedy_coloring(graph):
    colors={}
    for v in graph:
        used={colors[nb] for nb in graph[v] if nb in colors}
        c=0
        while c in used: c+=1
        colors[v]=c
    return colors

graph_map={
    'A':['B','C','D'],
    'B':['A','C','E'],
    'C':['A','B','D','E'],
    'D':['A','C','E'],
    'E':['B','C','D']
}
col=greedy_coloring(graph_map)
print(f"  Greedy coloring of 5-region map: {col} uses {max(col.values())+1} colors")

print("\n" + "="*60)
print("15.4 HISTORY & CONSTANTS (Wolfram History & Constants)")
print("="*60)

history=[
    ("~3000 BCE","Egypt/Babylon: pi approx 3, Pythagorean triples"),
    ("~500 BCE","Pythagoras, Euclid Elements (axioms)"),
    ("~250 BCE","Archimedes: pi bounds, lever, calculus precursor"),
    ("~1637","Descartes: coordinate geometry"),
    ("1687","Newton/Leibniz: calculus"),
    ("1800s","Gauss, Euler, Riemann: number theory, analysis"),
    ("1900s","Hilbert problems, Godel incompleteness, Turing, Computers"),
    ("1976","Four Color Theorem computer proof"),
    ("2000s","arXiv era: Perelman Poincare, Zhang primes"),
]
for date, event in history:
    print(f"  {date:12s} {event}")

print(f"\nFamous constants (Wolfram Constants, mathsisfun pi, e, phi):")
constants=[
    ("pi", math.pi, "circle circumference/diameter, transcendental"),
    ("e", math.e, "base natural log, (1+1/n)^n, transcendental"),
    ("phi", (1+math.sqrt(5))/2, "golden ratio, Fibonacci limit"),
    ("gamma", 0.5772156649, "Euler-Mascheroni, harmonic vs log"),
    ("Catalan", 0.915965594, "Catalan's constant, sum (-1)^n/(2n+1)^2"),
    ("Apéry", 1.202056903, "zeta(3), proved irrational"),
]
for name,val,desc in constants:
    print(f"  {name:8s}={val:.9f} - {desc}")

# Hilbert's problems teaser
print(f"\nHilbert's 23 problems (1900): e.g., Riemann Hypothesis still unsolved (Clay Millennium $1M)")
print(f"  arXiv: recent progress on prime gaps (Zhang 2013, Maynard) - search math.NT")

print("\n" + "="*60)
print("15.5 FRACTAL ART & RECREATION EXTRA")
print("="*60)
# Link to 05 fractals but new variants

# Sierpinski via chaos game
print(f"Chaos game generates Sierpinski: random midpoint of triangle vertices")
def chaos_sierpinski(iterations=10000):
    verts=[(0,0),(1,0),(0.5,0.866)]
    x,y=0.5,0.5
    pts=[]
    for _ in range(iterations):
        vx,vy=random.choice(verts)
        x=(x+vx)/2; y=(y+vy)/2
        pts.append((x,y))
    return pts

pts=chaos_sierpinski(5000)
# count roughly
print(f"  Generated {len(pts)} points, bounding box x in [{min(p[0] for p in pts):.2f},{max(p[0] for p in pts):.2f}]")

# Dragon curve, Hilbert curve mention
print(f"  Other fractals: Dragon curve, Hilbert space-filling, Koch (from 05)")

print(f"\nRecreational puzzles to code:")
print(f"  - Sudoku solver (backtracking)")
print(f"  - Maze generation (DFS/Prim)")
print(f"  - Conway's Game of Life (cellular automaton)")

def game_of_life_step(board):
    # board set of live cells {(x,y)}
    neigh_counts={}
    for x,y in board:
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if dx==0 and dy==0: continue
                neigh_counts[(x+dx,y+dy)] = neigh_counts.get((x+dx,y+dy),0)+1
    new=set()
    for cell,cnt in neigh_counts.items():
        if cell in board and cnt in [2,3]:
            new.add(cell)
        elif cell not in board and cnt==3:
            new.add(cell)
    return new

glider={(1,0),(2,1),(0,2),(1,2),(2,2)}
print(f"\nGame of Life: glider start {glider}")
for gen in range(5):
    print(f"  Gen {gen}: {len(glider)} cells")
    glider=game_of_life_step(glider)
print(f"  Glider moves diagonally forever (Wolfram, arXiv nlin.CG)")

if PLOT:
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        # Sierpinski chaos game
        xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
        plt.figure(figsize=(5,5))
        plt.scatter(xs,ys,s=1,c='black')
        plt.axis('equal'); plt.axis('off'); plt.title("Sierpinski via Chaos Game"); plt.show()

        # Magic square color
        plt.figure()
        plt.imshow(magic, cmap='viridis')
        plt.title("Magic Square 3x3"); plt.colorbar()
        for i in range(3):
            for j in range(3):
                plt.text(j,i,magic[i][j], ha='center', va='center', color='white', fontsize=16)
        plt.show()

        # Mobius strip 3D
        fig=plt.figure()
        ax=fig.add_subplot(111, projection='3d')
        u=np.linspace(0,2*math.pi,50)
        v=np.linspace(-0.5,0.5,10)
        U,V=np.meshgrid(u,v)
        # param
        X=(1+V*np.cos(U/2))*np.cos(U)
        Y=(1+V*np.cos(U/2))*np.sin(U)
        Z=V*np.sin(U/2)
        ax.plot_surface(X,Y,Z, cmap='coolwarm', alpha=0.8)
        ax.set_title("Mobius Strip"); plt.show()

        # Four color map
        # simple demo: plot graph
        plt.figure()
        # positions
        pos={'A':(0,0),'B':(1,1),'C':(1,0),'D':(0,1),'E':(2,0)}
        for node,(x,y) in pos.items():
            plt.scatter(x,y,s=600, c=['C'+str(col[node])], edgecolors='black')
            plt.text(x,y,node, ha='center', va='center', fontsize=14, color='white')
        for a in graph_map:
            for b in graph_map[a]:
                if a<b:
                    plt.plot([pos[a][0],pos[b][0]],[pos[a][1],pos[b][1]],'k-')
        plt.title(f"Map Coloring using {max(col.values())+1} colors"); plt.axis('off'); plt.show()

        # Game of Life animation frames
        board={(1,0),(2,1),(0,2),(1,2),(2,2)}
        fig, axes=plt.subplots(1,5, figsize=(12,3))
        for idx, ax in enumerate(axes):
            # plot
            if board:
                xs=[c[0] for c in board]; ys=[c[1] for c in board]
                ax.scatter(xs,ys,s=80,c='black')
            ax.set_xlim(-1,4); ax.set_ylim(-1,4); ax.set_title(f"Gen {idx}"); ax.set_aspect('equal'); ax.axis('off')
            board=game_of_life_step(board)
        plt.suptitle("Game of Life Glider Evolution"); plt.tight_layout(); plt.show()
    except Exception as e:
        print(e)
else:
    print("\n[Tip] --plot for Sierpinski, Mobius, Game of Life: python 15_recreational_topology.py --plot")

print("\nChallenge: implement Sudoku solver, generate Hilbert curve, or classify knots!")
