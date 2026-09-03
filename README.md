# Python Maths Lab — Complete (15 Modules)

Learn maths **by coding it** — from arithmetic to topology, fractals & knots. **Every topic maps to Wolfram MathWorld + MathsIsFun + arXiv**.

**Trust policy:** Research for this lab used ONLY:
- https://www.mathsisfun.com
- https://mathworld.wolfram.com
- https://arxiv.org

## Files & Coverage

| # | File | Topic | Main Sources | Key Ideas |
|---|------|-------|--------------|-----------|
| 01 | `01_basics.py` | Basics | mathsisfun numbers/algebra | BODMAS, linear/quadratic, primes & sieve, Fibonacci & phi, combinatorics |
| 02 | `02_geometry_trigonometry.py` | Geometry & Trig Intro | mathsisfun geometry/trig | Areas/volumes, Pythagoras, pi (Archimedes+Monte Carlo), unit circle, law of cos/sin |
| 03 | `03_calculus.py` | Calculus Intro | mathsisfun calculus | Limits, derivatives, integrals (Riemann), Taylor, gradient descent |
| 04 | `04_linear_algebra_probability.py` | LinAlg & Prob Intro | mathsisfun algebra/vectors, data | Vectors, matrices, Bayes, Monty Hall, CLT |
| 05 | `05_advanced.py` | Advanced | Wolfram dynamical systems + mathsisfun fractals | Koch/Mandelbrot, chaos, Fourier, RSA, zeta |
| **06** | `06_foundations_sets_logic.py` | **Foundations** | Wolfram Foundations, mathsisfun sets/logic-gates | Sets, Venn, truth tables, Boolean, half-adder, proofs (induction/contradiction) |
| **07** | `07_number_systems_modular.py` | **Numbers Deep** | mathsisfun binary/hex/bases, Wolfram Number Theory | Bases, Roman, modular arithmetic, Euclid, CRT, Miller-Rabin, phi, continued fractions, perfect numbers |
| **08** | `08_algebra_advanced.py` | **Algebra Complete** | mathsisfun algebra, Wolfram Algebra/Polynomials | Exponent laws, logs, polynomials (mul/div), factoring, quadratics, sequences/series, inequalities |
| **09** | `09_geometry_complete.py` | **Geometry Complete** | mathsisfun geometry, Wolfram Geometry | Polygons, circle theorems, conics (ellipse/parabola/hyperbola), polyhedra & Euler V-E+F=2, transformations, tessellations |
| **10** | `10_trigonometry_complex.py` | **Trig & Complex** | mathsisfun trig, Wolfram Trig/Complex | Identities, Euler `e^{i pi}+1=0`, De Moivre, roots of unity, phasors, waves |
| **11** | `11_calculus_analysis.py` | **Calculus Analysis** | mathsisfun calculus, Wolfram Calculus&Analysis | L'Hôpital, series convergence, partial derivatives, integration tricks, arc length, solids, ODEs (Euler/RK), Fourier series |
| **12** | `12_discrete_mathematics.py` | **Discrete** | Wolfram Discrete, mathsisfun combinatorics/graph-theory | Perm/combi, Catalan, binomial, graphs (BFS/DFS/Dijkstra), Eulerian/Hamiltonian, Hamming |
| **13** | `13_probability_statistics_complete.py` | **Probability Complete** | mathsisfun data, Wolfram Probability | Histograms, quartiles, weighted/GM/HM, distributions, CLT, least-squares regression, confidence intervals, chi/t-tests |
| **14** | `14_applied_numerical.py` | **Applied & Numerical** | mathsisfun linear-programming/measure, Wolfram Applied/Numerical | Units, linear programming (feasible region), bisection/Newton, Simpson/Monte Carlo, Euler vs RK4, Lagrange interpolation |
| **15** | `15_recreational_topology.py` | **Recreational & Topology** | Wolfram Recreational/Topology/History, mathsisfun tessellation | Magic squares, Hanoi, Nim, Penrose, Mobius/Klein, knots, 4-color theorem, history timeline, Game of Life |

> Mapping to Wolfram MathWorld top-level categories: Calculus & Analysis (03,11), Algebra (01,08), Geometry (02,09), Discrete (12), Foundations (06), Number Theory (01,07), Probability & Stats (04,13), Applied (14), Topology (15), Recreational (15), History (15) — **all 11 covered**.

## Quick Start

```powershell
cd C:\Users\lachl\Maths
pip install -r requirements.txt   # numpy, matplotlib, sympy (optional: networkx, matplotlib-venn)

# Text mode (works anywhere)
python 01_basics.py
python 06_foundations_sets_logic.py
python 09_geometry_complete.py

# With plots (recommended - visual!)
python 02_geometry_trigonometry.py --plot
python 05_advanced.py --plot --fractal   # Mandelbrot ~5s
python 07_number_systems_modular.py --plot  # Ulam spiral
python 12_discrete_mathematics.py --plot
python 15_recreational_topology.py --plot  # Sierpinski, Mobius, Life

# Hub
python main.py          # menu 1-15, a=all, p=all+plots
python main.py all      # run all 1-15 without plots
python main.py plotall  # all with plots
python main.py 11       # single module (add --plot for graphs)
```

## Learning Path

1. **Beginner:** 01 → 02 → 03 → 04 → 06 → 07 → 08
2. **Intermediate:** 09 → 10 → 11 → 12 → 13
3. **Advanced/ArXiv:** 05 → 14 → 15 (then search arXiv: `math.NT`, `nlin.CD`, `math.CO`)
4. Each file has **Challenges** at end — do them!

## Research Links Used (only these)

- MathsIsFun indexes: `/numbers`, `/algebra`, `/geometry`, `/calculus`, `/data`, `/sets`, `/combinatorics`
- MathWorld topics: `/Algebra`, `/CalculusandAnalysis`, `/Geometry`, `/NumberTheory`, `/DiscreteMathematics`, `/FoundationsofMathematics`, `/ProbabilityandStatistics`, `/AppliedMathematics`, `/Topology`, `/RecreationalMathematics`, `/HistoryandTerminology`
- arXiv hints in file headers (e.g., `1909.01423` Fourier, `math.NT` primes)

## Tips

- All scripts force UTF-8 so Windows `cp1252` won't crash; still `chcp 65001` for perfect symbols.
- No internet needed after install — everything runs offline.
- Edit the files! Change `r=3.9` to `4.0` in chaos and watch divergence.

Happy maths!
