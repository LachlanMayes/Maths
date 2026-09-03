"""
04 - LINEAR ALGEBRA & PROBABILITY / STATISTICS
Sources: https://www.mathsisfun.com/algebra/vectors.html
         https://www.mathsisfun.com/data/index.html
Run: python 04_linear_algebra_probability.py [--plot]
"""
import math, random, sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except: pass
PLOT = "--plot" in sys.argv
try:
    import numpy as np
    HAS_NP = True
except ImportError:
    HAS_NP = False
    print("Tip: pip install numpy for full matrix power")

print("="*60)
print("4.1 VECTORS")
print("="*60)

def vec_add(a,b): return [x+y for x,y in zip(a,b)]
def vec_sub(a,b): return [x-y for x,y in zip(a,b)]
def vec_dot(a,b): return sum(x*y for x,y in zip(a,b))
def vec_mag(v): return math.sqrt(sum(x*x for x in v))
def vec_scale(v,s): return [x*s for x in v]
def vec_normalize(v): m=vec_mag(v); return [x/m for x in v]
def vec_cross(a,b): # 3D only
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def angle_between(a,b):
    return math.degrees(math.acos(vec_dot(a,b)/(vec_mag(a)*vec_mag(b))))

v1, v2 = [3,4], [1,2]
print(f"v1={v1}, v2={v2}")
print(f"  v1+v2={vec_add(v1,v2)}, v1-v2={vec_sub(v1,v2)}")
print(f"  dot={vec_dot(v1,v2)}, |v1|={vec_mag(v1):.2f} (3-4-5 triangle!)")
print(f"  angle between={angle_between(v1,v2):.2f}°")
print(f"  3D cross [1,2,3] x [4,5,6] = {vec_cross([1,2,3],[4,5,6])}")
print(f"  normalize [3,4] = {vec_normalize([3,4])} (length {vec_mag(vec_normalize([3,4])):.1f})")

if HAS_NP:
    print("\n  [numpy] Vectorized:")
    a = np.array([3,4]); b = np.array([1,2])
    print(f"    numpy dot={np.dot(a,b)}, norm={np.linalg.norm(a)}")
    # Projection: proj of a onto b = (a·b / |b|²) * b
    proj = np.dot(a,b)/np.dot(b,b) * b
    print(f"    projection of {a} onto {b} = {proj}")

print("\n" + "="*60)
print("4.2 MATRICES")
print("="*60)

# Pure python matrix multiply
def mat_mul(A,B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    assert cols_A==rows_B
    C=[[0]*cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k]*B[k][j]
    return C

def mat_transpose(A): return [list(row) for row in zip(*A)]
def mat_print(M, name="Matrix"):
    print(f"  {name}:")
    for row in M: print("   ", row)

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
mat_print(A,"A"); mat_print(B,"B")
mat_print(mat_mul(A,B), "A×B")
mat_print(mat_transpose(A), "Aᵀ")

# Determinant & inverse (2x2)
def det2(M): return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def inv2(M):
    d=det2(M)
    assert d!=0
    return [[M[1][1]/d, -M[0][1]/d], [-M[1][0]/d, M[0][0]/d]]

print(f"\n  det(A)={det2(A)}")
invA = inv2(A)
mat_print(invA, "A⁻¹")
mat_print(mat_mul(A, invA), "A×A⁻¹ (should be I)")
print(f"  Solving linear system: 1x+2y=5, 3x+4y=11 -> use A⁻¹×b")
b = [[5],[11]]
sol = mat_mul(invA, b)
print(f"    solution x={sol[0][0]:.1f}, y={sol[1][0]:.1f}")

if HAS_NP:
    print("\n  [numpy] Matrix power:")
    Anp = np.array(A, dtype=float)
    print(f"    det = {np.linalg.det(Anp):.1f}")
    print(f"    inv =\n{np.linalg.inv(Anp)}")
    print(f"    eigenvalues of A = {np.linalg.eigvals(Anp)}")
    # Rotation matrix
    theta = math.radians(90)
    R = np.array([[math.cos(theta), -math.sin(theta)],[math.sin(theta), math.cos(theta)]])
    v = np.array([1,0])
    print(f"    Rotate [1,0] by 90°: {R @ v} (should be [0,1])")
    # 3D transformation demo
    print(f"    Matrix @ vector demo complete")

print("\n" + "="*60)
print("4.3 PROBABILITY")
print("="*60)
# mathsisfun.com/data/probability.html
print("Basic: coin flip P(H)=0.5, dice P(6)=1/6≈0.1667")
# Conditional probability: Bayes' theorem
print("\nBayes' theorem: P(A|B) = P(B|A)P(A)/P(B)")
# Medical test example
p_disease = 0.01
p_pos_given_disease = 0.95
p_pos_given_no_disease = 0.05
p_pos = p_pos_given_disease*p_disease + p_pos_given_no_disease*(1-p_disease)
p_disease_given_pos = p_pos_given_disease*p_disease / p_pos
print(f"  Disease rate 1%, test 95% accurate, 5% false positive:")
print(f"  P(disease|positive) = {p_disease_given_pos:.4f} (~16%!)  Surprising but true")

# Expected value
def expected_value(outcomes): # [(value, prob), ...]
    return sum(v*p for v,p in outcomes)
print(f"\nExpected value dice roll: {expected_value([(i,1/6) for i in range(1,7)]):.2f} ( = 3.5)")
print(f"Lottery: win $1000 with 1/1000, else 0: EV = ${expected_value([(1000,0.001),(0,0.999)]):.2f}")

# Binomial distribution
def binomial_p(n,k,p): return math.comb(n,k)*(p**k)*((1-p)**(n-k))
print(f"\nBinomial: 10 coin flips, P(exactly 3 heads)={binomial_p(10,3,0.5):.4f}")
print(f"  P(at least 8 heads)={sum(binomial_p(10,k,0.5) for k in range(8,11)):.4f}")

# Monty Hall simulation
def monty_hall(simulations=10000, switch=True):
    wins=0
    for _ in range(simulations):
        car = random.randint(0,2)
        pick = random.randint(0,2)
        # host opens a goat door
        # if switch, you win if initial pick != car
        win = (pick != car) if switch else (pick == car)
        wins+=win
    return wins/simulations

random.seed(1)
print(f"\nMonty Hall ({10000} sims):")
print(f"  Win rate if SWITCH: {monty_hall(10000, True):.3f} (theory 0.666)")
print(f"  Win rate if STAY:   {monty_hall(10000, False):.3f} (theory 0.333)")

# Birthday paradox
def birthday_prob(n=23):
    # P(at least one shared birthday) = 1 - P(all different)
    p_diff = 1
    for i in range(n):
        p_diff *= (365-i)/365
    return 1-p_diff

print(f"\nBirthday paradox:")
for n in [5,10,23,30,50,70]:
    print(f"  {n:2d} people: P(shared birthday)={birthday_prob(n):.4f}")

print("\n" + "="*60)
print("4.4 STATISTICS")
print("="*60)

data = [2,4,4,4,5,5,7,9]
print(f"Data: {data}")
def mean(d): return sum(d)/len(d)
def median(d): s=sorted(d); n=len(s); return (s[n//2] if n%2 else (s[n//2-1]+s[n//2])/2)
def mode(d): return max(set(d), key=d.count)
def variance(d): m=mean(d); return sum((x-m)**2 for x in d)/len(d)
def stddev(d): return math.sqrt(variance(d))
def pop_variance(d): m=mean(d); return sum((x-m)**2 for x in d)/(len(d)-1)  # sample

print(f"  Mean={mean(data):.2f}, Median={median(data)}, Mode={mode(data)}")
print(f"  Variance={variance(data):.2f}, StdDev={stddev(data):.2f}")
print(f"  Range={max(data)-min(data)}, IQR demo below")

# Standard deviation & normal distribution
# 68-95-99.7 rule
print(f"\nNormal distribution (68-95-99.7 rule):")
print(f"  For mean=0, std=1: 68% within [-1,1], 95% within [-2,2]")

# Correlation
def correlation(x,y):
    mx, my = mean(x), mean(y)
    num = sum((xi-mx)*(yi-my) for xi,yi in zip(x,y))
    den = math.sqrt(sum((xi-mx)**2 for xi in x) * sum((yi-my)**2 for yi in y))
    return num/den if den else 0

x_vals = [1,2,3,4,5]
y_vals = [2,4,5,4,5]  # roughly correlated
y_random = [random.randint(1,5) for _ in x_vals]
print(f"\nCorrelation:")
print(f"  x={x_vals}, y={y_vals} -> r={correlation(x_vals, y_vals):.3f} (positive)")
print(f"  Perfect linear y=2x: r={correlation(x_vals,[2*v for v in x_vals]):.3f}")
print(f"  Perfect negative: r={correlation(x_vals,list(reversed(x_vals))):.3f}")

# Law of large numbers demo
print(f"\nLaw of Large Numbers (dice average -> 3.5):")
random.seed(0)
for n in [10,100,1000,10000]:
    rolls=[random.randint(1,6) for _ in range(n)]
    print(f"  {n:5d} rolls: avg={mean(rolls):.4f}")

# Central Limit Theorem preview
print(f"\nCentral Limit Theorem teaser: avg of 30 dice rolls -> approx Normal")
if HAS_NP:
    samples = [mean([random.randint(1,6) for _ in range(30)]) for _ in range(5000)]
    print(f"  5000 samples of avg(30 dice): mean={mean(samples):.3f}, std={stddev(samples):.3f} (theory std~ {1.7078/math.sqrt(30):.3f})")

if PLOT and HAS_NP:
    import matplotlib.pyplot as plt

    # Vector plot
    plt.figure(figsize=(5,5))
    plt.quiver(0,0,3,4, angles='xy', scale_units='xy', scale=1, color='blue', label='v1=[3,4]')
    plt.quiver(0,0,1,2, angles='xy', scale_units='xy', scale=1, color='red', label='v2=[1,2]')
    plt.xlim(0,5); plt.ylim(0,5); plt.grid(True); plt.legend()
    plt.title("Vectors"); plt.gca().set_aspect('equal'); plt.show()

    # Normal distribution
    xs = np.linspace(-4,4,200)
    ys = 1/math.sqrt(2*math.pi) * np.exp(-xs**2/2)
    plt.figure()
    plt.plot(xs, ys)
    plt.fill_between(xs, ys, where=(np.abs(xs)<=1), alpha=0.3, label='68%')
    plt.fill_between(xs, ys, where=(np.abs(xs)<=2), alpha=0.15, label='95%')
    plt.title("Standard Normal Distribution (Bell Curve)"); plt.legend(); plt.grid(True); plt.show()

    # Correlation scatter
    fig, axes = plt.subplots(1,3, figsize=(12,3))
    axes[0].scatter(x_vals, y_vals); axes[0].set_title(f"Correlated r={correlation(x_vals,y_vals):.2f}")
    axes[1].scatter(x_vals, [2*v for v in x_vals]); axes[1].set_title("Perfect r=1.0")
    axes[2].hist(samples, bins=30, edgecolor='black'); axes[2].set_title("CLT: Avg 30 dice (Normal)")
    plt.tight_layout(); plt.show()

    # Monty Hall convergence
    # Birthday curve
    ns = list(range(1,60))
    probs = [birthday_prob(n) for n in ns]
    plt.figure()
    plt.plot(ns, probs, 'o-')
    plt.axhline(0.5, color='red', linestyle='--')
    plt.axvline(23, color='red', linestyle='--')
    plt.title("Birthday Paradox"); plt.xlabel("n people"); plt.ylabel("P(shared)"); plt.grid(True); plt.show()
else:
    print("\n[Tip] Run with --plot: python 04_linear_algebra_probability.py --plot")

print("\nChallenge: Build a simple linear regression y=mx+b using gradient descent!")
