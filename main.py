"""
MAIN - Your Maths Journey Hub (FULL - 15 modules)
Sources ONLY: mathsisfun.com + mathworld.wolfram.com + arxiv.org
Run: python main.py
"""
import subprocess, sys, os

MENU = """
======================================================
   PYTHON MATHS LAB - Complete (15 Modules)
   Sources: mathsisfun.com + mathworld.wolfram.com + arxiv.org
------------------------------------------------------
  1  Basics (arithmetic, algebra, primes, Fib)
  2  Geometry & Trigonometry (pi, triangles)
  3  Calculus (derivatives, integrals, Taylor)
  4  Linear Algebra & Probability
  5  Advanced (fractals, chaos, Fourier, RSA)
  6  Foundations (sets, logic, proofs)
  7  Number Systems & Modular (bases, CRT, primes)
  8  Algebra Advanced (exponents, logs, polynomials)
  9  Geometry Complete (conics, polyhedra, Euler)
 10  Trigonometry & Complex (Euler, De Moivre)
 11  Calculus Analysis (series, diff eq, Fourier)
 12  Discrete Mathematics (combinatorics, graphs)
 13  Probability & Statistics Complete (regression)
 14  Applied & Numerical (optimization, Newton, RK4)
 15  Recreational & Topology (knots, maps, Life)
------------------------------------------------------
  a  Run ALL 1-15 sequentially (no plots)
  p  Run ALL 1-15 with PLOTS
  q  Quit
======================================================
"""

SCRIPTS = {
    "1": ("01_basics.py", "Basics"),
    "2": ("02_geometry_trigonometry.py", "Geometry & Trig"),
    "3": ("03_calculus.py", "Calculus"),
    "4": ("04_linear_algebra_probability.py", "LinAlg & Probability"),
    "5": ("05_advanced.py", "Advanced"),
    "6": ("06_foundations_sets_logic.py", "Foundations/Logic"),
    "7": ("07_number_systems_modular.py", "Number Systems"),
    "8": ("08_algebra_advanced.py", "Algebra Adv"),
    "9": ("09_geometry_complete.py", "Geometry Complete"),
    "10": ("10_trigonometry_complex.py", "Trig & Complex"),
    "11": ("11_calculus_analysis.py", "Calculus Analysis"),
    "12": ("12_discrete_mathematics.py", "Discrete Maths"),
    "13": ("13_probability_statistics_complete.py", "Probability Complete"),
    "14": ("14_applied_numerical.py", "Applied/Numerical"),
    "15": ("15_recreational_topology.py", "Recreational/Topology"),
}

def run(script, with_plot=False):
    cmd = [sys.executable, script]
    if with_plot:
        cmd.append("--plot")
    print(f"\n{'='*30} Running {script} {'='*30}\n")
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"
    result = subprocess.run(cmd, cwd=os.path.dirname(__file__), env=env)
    print(f"\n{'-'*60} Exit code: {result.returncode}\n")
    return result.returncode==0

def main():
    print(MENU)
    print("Quick start: python 06_foundations_sets_logic.py  -> etc.")
    print("Or 'a' to run everything, 'p' for all with plots.\n")
    while True:
        try:
            choice = input("Choose [1-15/a/p/q] (Enter=a): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
        if choice == "":
            choice = "a"
        if choice == "q":
            print("Happy maths!")
            break
        elif choice == "a":
            for k in map(str, range(1,16)):
                run(SCRIPTS[k][0], with_plot=False)
            print("\nAll 15 done! Try 'p' for plots.")
        elif choice == "p":
            for k in map(str, range(1,16)):
                run(SCRIPTS[k][0], with_plot=True)
        elif choice in SCRIPTS:
            plot = input("  Show plots? [y/N]: ").strip().lower() == "y"
            run(SCRIPTS[choice][0], with_plot=plot)
        else:
            print("Invalid. Try 1-15, a, p or q.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in SCRIPTS:
        run(SCRIPTS[sys.argv[1]][0], with_plot="--plot" in sys.argv)
    elif len(sys.argv) > 1 and sys.argv[1] == "all":
        for k in map(str, range(1,16)):
            run(SCRIPTS[k][0])
    elif len(sys.argv) > 1 and sys.argv[1] == "plotall":
        for k in map(str, range(1,16)):
            run(SCRIPTS[k][0], with_plot=True)
    else:
        main()
