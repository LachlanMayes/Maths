"""
06 - FOUNDATIONS: Sets, Logic, Proofs & Foundations of Mathematics
Sources:
  - https://www.mathsisfun.com/sets/index.html
  - https://www.mathsisfun.com/sets/logic-gates.html  (Boolean)
  - https://mathworld.wolfram.com/topics/FoundationsofMathematics.html
  - https://mathworld.wolfram.com/SetTheory.html, PropositionalCalculus
Run: python 06_foundations_sets_logic.py [--plot]
"""
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
except: pass
import itertools, math

PLOT = "--plot" in sys.argv

print("="*60)
print("6.1 SETS - mathsisfun.com/sets/index.html")
print("="*60)
# Wolfram: Set Theory is foundation

def set_union(a,b): return a | b
def set_intersection(a,b): return a & b
def set_difference(a,b): return a - b
def set_symmetric_diff(a,b): return a ^ b
def is_subset(a,b): return a <= b
def power_set(s):
    s=list(s)
    return [set(comb) for r in range(len(s)+1) for comb in itertools.combinations(s,r)]

A = {1,2,3,4}
B = {3,4,5,6}
U = {1,2,3,4,5,6,7,8}
print(f"A={A}, B={B}, U={U}")
print(f"  Union A|B = {set_union(A,B)}")
print(f"  Intersection A&B = {set_intersection(A,B)}")
print(f"  Difference A-B = {set_difference(A,B)}")
print(f"  Symmetric diff A^B = {set_symmetric_diff(A,B)}")
print(f"  Complement A' = {U - A}  (in U)")
print(f"  A subset of U? {is_subset(A,U)}")
print(f"  Power set of {{1,2,3}} has {len(power_set({1,2,3}))} elements: {power_set({1,2,3})}")
print(f"  Cardinality |A|={len(A)}, |power(A)|=2^|A|={2**len(A)}")

# De Morgan's Laws (Wolfram)
print("\nDe Morgan's Laws verification:")
print(f"  (A union B)' = {U - (A|B)}")
print(f"  A' intersect B' = {(U-A) & (U-B)}  -> equal? {U-(A|B) == (U-A)&(U-B)}")
print(f"  (A intersect B)' = {U - (A&B)}")
print(f"  A' union B' = {(U-A)|(U-B)} -> equal? {U-(A&B)==(U-A)|(U-B)}")

# Venn region counts (inclusion-exclusion)
print(f"\nInclusion-Exclusion: |A U B| = |A|+|B|-|A cap B| = {len(A)}+{len(B)}-{len(A&B)} = {len(A|B)} vs {len(A|B)} check {len(A|B)==len(A)+len(B)-len(A&B)}")

print("\n" + "="*60)
print("6.2 LOGIC & TRUTH TABLES")
print("="*60)
# mathsisfun: logic gates, Wolfram: Propositional Calculus

def AND(a,b): return a and b
def OR(a,b): return a or b
def NOT(a): return not a
def XOR(a,b): return a ^ b
def NAND(a,b): return not (a and b)
def NOR(a,b): return not (a or b)
def IMPLIES(a,b): return (not a) or b  # a -> b
def EQUIV(a,b): return a == b

print("Truth table for AND, OR, XOR, IMPLIES, EQUIV:")
print(" A | B | AND | OR | XOR | A->B | A<->B")
print("-"*40)
for a,b in [(False,False),(False,True),(True,False),(True,True)]:
    print(f" {int(a)} | {int(b)} |  {int(AND(a,b))}  | {int(OR(a,b))}  |  {int(XOR(a,b))}  |  {int(IMPLIES(a,b))}   |   {int(EQUIV(a,b))}")

# Tautology: (p -> q) <-> (not p or q)
print("\nTautology check: (p->q) equivalent to (!p or q)")
for p,q in itertools.product([False,True], repeat=2):
    left = IMPLIES(p,q)
    right = OR(NOT(p), q)
    print(f"  p={int(p)}, q={int(q)}: {int(left)} == {int(right)} ? {left==right}")

# Contradiction & contingency
print("\nLaw of Excluded Middle: p or not p always True:")
for p in [False, True]:
    print(f"  p={int(p)}: p or not p = {int(OR(p, NOT(p)))}")
print("Law of Non-Contradiction: p and not p always False:")
for p in [False, True]:
    print(f"  p={int(p)}: p and not p = {int(AND(p, NOT(p)))}")

print("\n" + "="*60)
print("6.3 BOOLEAN ALGEBRA & LOGIC GATES")
print("="*60)
# Wolfram: Boolean Algebra, mathsisfun: logic gates
# Simulate a half-adder (XOR=sum, AND=carry)
print("Half-adder (adds 1-bit numbers):")
print(" A B | Sum(XOR) Carry(AND)")
for a,b in [(0,0),(0,1),(1,0),(1,1)]:
    print(f" {a} {b} |   {a^b}       {a&b}")

# Full-adder using 2 half-adders
def full_adder(a,b,cin):
    s1 = a ^ b
    c1 = a & b
    s = s1 ^ cin
    c2 = s1 & cin
    cout = c1 | c2
    return s, cout

print("\nFull-adder (A+B+Cin):")
for a,b,cin in itertools.product([0,1],[0,1],[0,1]):
    s,cout = full_adder(a,b,cin)
    print(f" {a}+{b}+{cin} = cout {cout} sum {s} (= {a+b+cin}) { 'ok' if cout*2+s==a+b+cin else 'fail'}")

# Boolean simplification demo: De Morgan for gates
print("\nDe Morgan for gates: NAND = NOT(AND) = OR of NOTs")
for a,b in [(0,0),(0,1),(1,0),(1,1)]:
    nand = int(NAND(bool(a),bool(b)))
    demorgan = int(OR(NOT(bool(a)), NOT(bool(b))))
    print(f"  a={a}, b={b}: NAND={nand}, NOT(a) OR NOT(b)={demorgan} equal? {nand==demorgan}")

print("\n" + "="*60)
print("6.4 PROOFS - Direct, Contradiction, Induction")
print("="*60)
# Wolfram: Proof Theory

# Direct proof: sum of two evens is even
print("Direct proof: sum of two evens is even")
for a,b in [(2,4),(6,10),(0,8)]:
    assert a%2==0 and b%2==0
    print(f"  {a}+{b}={a+b}, is even? { (a+b)%2==0 }")

# Proof by contradiction demo: sqrt(2) irrational (sketch)
# If sqrt2 = p/q in lowest terms, then p^2=2q^2 so p even, q even -> contradiction
print("\nProof by contradiction sketch: sqrt(2) is irrational")
print("  Assume sqrt(2)=p/q lowest terms => p^2=2q^2 => p even => p=2k")
print("  Then 4k^2=2q^2 => q^2=2k^2 => q even => both even => contradicts lowest terms => irrational")
print(f"  Numeric check sqrt(2)={math.sqrt(2):.10f} not fraction")

# Induction: prove 1+2+...+n = n(n+1)/2
print("\nProof by induction: sum 1..n = n(n+1)/2")
for n in [1,5,10,100]:
    lhs = sum(range(1,n+1))
    rhs = n*(n+1)//2
    print(f"  n={n:3d}: sum={lhs}, formula={rhs} equal? {lhs==rhs}")
print("  Base case n=1: 1=1*2/2 OK; Inductive step assumes true for k, proves for k+1")

# Pigeonhole principle (Wolfram)
print("\nPigeonhole principle: 13 people => at least 2 share birth month")
print("  12 months, 13 pigeons => by pigeonhole, one hole has >=2")

print("\n" + "="*60)
print("6.5 RELATIONS, FUNCTIONS & CARDINALITY")
print("="*60)
# Wolfram: Relations, Functions

def is_function(relation, domain):
    # relation is set of (x,y), each x maps to exactly one y
    mapping={}
    for x,y in relation:
        if x in mapping and mapping[x]!=y:
            return False
        mapping[x]=y
    return set(mapping.keys())==domain

rel1 = {(1,'a'),(2,'b'),(3,'a')}
rel2 = {(1,'a'),(1,'b')}
print(f"Relation {rel1} is function on {{1,2,3}}? {is_function(rel1,{1,2,3})}")
print(f"Relation {rel2} is function? {is_function(rel2,{1})} (one x maps to two y)")

# Injective, surjective, bijective
def injective(func_dict): return len(set(func_dict.values()))==len(func_dict)
def surjective(func_dict, codomain): return set(func_dict.values())==codomain

f = {1:2,2:4,3:6}
print(f"\nf={f} injective? {injective(f)} (distinct outputs)")
print(f"  surjective onto {{2,4,6}}? {surjective(f,{2,4,6})}")
print(f"  bijective (both)? {injective(f) and surjective(f,{2,4,6})}")

# Cardinality: countable infinity demo
print(f"\nCardinality: N (natural) is countably infinite, |N| = aleph_0")
print(f"  Even though N and even numbers both infinite, they have same cardinality (bijection n<->2n)")
print(f"  Power set of N is uncountable (Cantor's diagonal)")

if PLOT:
    try:
        import matplotlib.pyplot as plt
        from matplotlib_venn import venn2
        plt.figure()
        venn2(subsets=(2,2,1), set_labels=('A','B'))
        plt.title("Venn Diagram (needs matplotlib-venn)"); plt.show()
    except ImportError:
        # Manual Venn with matplotlib circles
        import matplotlib.pyplot as plt
        import matplotlib.patches as patches
        fig, ax = plt.subplots(figsize=(6,4))
        c1 = patches.Circle((0.4,0.5),0.25, alpha=0.3, color='blue', label='A')
        c2 = patches.Circle((0.6,0.5),0.25, alpha=0.3, color='red', label='B')
        ax.add_patch(c1); ax.add_patch(c2)
        ax.text(0.3,0.5,'A only'); ax.text(0.65,0.5,'B only'); ax.text(0.5,0.5,'A cap B')
        ax.set_xlim(0,1); ax.set_ylim(0,1); ax.set_aspect('equal'); ax.axis('off')
        plt.title("Venn Diagram: A and B"); plt.legend(); plt.show()

        # Logic gate visualization: truth tables
        fig, axes = plt.subplots(2,2, figsize=(8,6))
        axes[0,0].axis('off'); axes[0,0].text(0,0.5, "AND truth: 0*0=0\n0*1=0\n1*0=0\n1*1=1", fontsize=12)
        axes[0,1].axis('off'); axes[0,1].text(0,0.5, "OR truth: 0+0=0\n0+1=1\n1+0=1\n1+1=1", fontsize=12)
        axes[1,0].axis('off'); axes[1,0].text(0,0.5, "XOR: 0+0=0\n0+1=1\n1+0=1\n1+1=0", fontsize=12)
        axes[1,1].axis('off'); axes[1,1].text(0,0.5, "IMPLIES: F->F=T\nF->T=T\nT->F=F\nT->T=T", fontsize=12)
        plt.suptitle("Logic Gates - Truth Tables"); plt.tight_layout(); plt.show()
    print("Plots done. For prettier Venn: pip install matplotlib-venn")
else:
    print("\n[Tip] Run with --plot for Venn diagram: python 06_foundations_sets_logic.py --plot")

print("\nChallenge: implement a SAT solver for 3-CNF, or prove infinity of primes (Euclid)!")
