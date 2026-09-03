"""
01 - BASICS: Numbers, Algebra & Patterns
Source inspiration: https://www.mathsisfun.com/numbers/index.html
                    https://www.mathsisfun.com/algebra/index.html
Run: python 01_basics.py
"""

import math
import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except: pass

# --- 1.1 Arithmetic & Number Types ---
print("="*60)
print("1.1 ARITHMETIC & NUMBER TYPES")
print("="*60)
# Integers, floats, complex, fractions
a, b = 17, 5
print(f"a={a}, b={b} -> a+b={a+b}, a-b={a-b}, a*b={a*b}, a/b={a/b:.2f}, a//b={a//b}, a%b={a%b}, a**b={a**b}")
print(f"Square root of 50 = {math.sqrt(50):.4f}, pi = {math.pi:.5f}, e = {math.e:.5f}")

# Order of operations (BODMAS/BEDMAS) - mathsisfun.com/operation-order-bodmas.html
expr = 3 + 6 * (5 + 4) / 3 - 7
print(f"BODMAS: 3 + 6 * (5+4)/3 - 7 = {expr}  # brackets first, then multiply/divide")

# --- 1.2 Algebra: Solving equations ---
print("\n" + "="*60)
print("1.2 ALGEBRA - Solving linear & quadratic equations")
print("="*60)

def solve_linear(a, b):
    """Solve ax + b = 0 -> x = -b/a"""
    if a == 0:
        return None
    return -b / a

print(f"Solve 2x + 6 = 0 -> x = {solve_linear(2, 6)}")
print(f"Solve 5x - 15 = 0 -> x = {solve_linear(5, -15)}")

def solve_quadratic(a, b, c):
    """Solve ax^2 + bx + c = 0 using quadratic formula"""
    disc = b**2 - 4*a*c
    print(f"  Quadratic {a}x² + {b}x + {c}=0, discriminant = {disc}")
    if disc < 0:
        # complex roots
        real = -b/(2*a)
        imag = math.sqrt(-disc)/(2*a)
        return (complex(real, imag), complex(real, -imag))
    elif disc == 0:
        return (-b/(2*a),)
    else:
        x1 = (-b + math.sqrt(disc)) / (2*a)
        x2 = (-b - math.sqrt(disc)) / (2*a)
        return (x1, x2)

for coeffs in [(1, -3, 2), (1, 2, 1), (1, 0, 1)]:
    roots = solve_quadratic(*coeffs)
    print(f"  Roots: {roots}")

# Using sympy for symbolic algebra (more advanced)
try:
    import sympy as sp
    x = sp.symbols('x')
    print("\n  [sympy] Expanding (x+2)(x+3):", sp.expand((x+2)*(x+3)))
    print("  [sympy] Factoring x^2+5x+6:", sp.factor(x**2+5*x+6))
    print("  [sympy] Solving x^2-5x+6=0:", sp.solve(x**2-5*x+6, x))
except ImportError:
    print("  (install sympy for symbolic maths)")

# --- 1.3 Number Theory: Primes, Factors, GCD ---
print("\n" + "="*60)
print("1.3 NUMBER THEORY - Primes & Factors")
print("="*60)

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    for i in range(3, int(math.isqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    d = 2
    while d*d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append(n)
    return factors

print(f"Primes up to 30: {[n for n in range(30) if is_prime(n)]}")
print(f"Prime factors of 84: {prime_factors(84)}  # 84 = 2*2*3*7")
print(f"Prime factors of 360: {prime_factors(360)}")
print(f"GCD of 48 and 18 = {math.gcd(48, 18)}, LCM = {math.lcm(48, 18) if hasattr(math,'lcm') else 48*18//math.gcd(48,18)}")

# Sieve of Eratosthenes - classic prime algorithm
def sieve(n):
    is_prime_arr = [True]*(n+1)
    is_prime_arr[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if is_prime_arr[i]:
            for j in range(i*i, n+1, i):
                is_prime_arr[j] = False
    return [i for i, p in enumerate(is_prime_arr) if p]

print(f"Sieve primes to 50: {sieve(50)}")

# --- 1.4 Sequences & Series ---
print("\n" + "="*60)
print("1.4 SEQUENCES - Fibonacci, Arithmetic, Geometric")
print("="*60)

def fibonacci(n):
    """Return first n Fibonacci numbers - mathsisfun.com/numbers/fibonacci-sequence.html"""
    seq = [0, 1]
    for _ in range(n-2):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

fib10 = fibonacci(15)
print(f"Fibonacci (15): {fib10}")
print(f"  Ratio F(n)/F(n-1) -> Golden Ratio phi ~ {fib10[-1]/fib10[-2]:.6f} (phi = {(1+math.sqrt(5))/2:.6f})")

# Golden ratio check
phi = (1+math.sqrt(5))/2
print(f"  Golden ratio phi = {phi:.10f}, phi^2 = phi+1? {abs(phi**2 - (phi+1)) < 1e-10}")

def arithmetic_sequence(a1, d, n):
    return [a1 + i*d for i in range(n)]

def geometric_sequence(a1, r, n):
    return [a1 * (r**i) for i in range(n)]

print(f"Arithmetic a1=3, d=4 (8 terms): {arithmetic_sequence(3, 4, 8)}")
print(f"Geometric  a1=2, r=3 (8 terms): {geometric_sequence(2, 3, 8)}")
print(f"Sum of geometric 2,6,18,... (n=8) = {sum(geometric_sequence(2,3,8))}")
# Formula: S = a1*(r^n -1)/(r-1)
n=8; a1=2; r=3
print(f"  Formula check: S = a1*(r^n-1)/(r-1) = {a1*(r**n -1)/(r-1)}")

# --- 1.5 Factorials & Combinatorics ---
print("\n" + "="*60)
print("1.5 FACTORIALS & COMBINATORICS")
print("="*60)
print(f"5! = {math.factorial(5)}, 10! = {math.factorial(10)}")
def nCr(n, r): return math.comb(n, r) if hasattr(math,'comb') else math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
def nPr(n, r): return math.perm(n, r) if hasattr(math,'perm') else math.factorial(n)//math.factorial(n-r)
print(f"C(10,3) = {nCr(10,3)}  # combinations (order doesn't matter)")
print(f"P(10,3) = {nPr(10,3)}  # permutations (order matters)")
print(f"Pascal's triangle row 6: {[nCr(6,k) for k in range(7)]}")

# --- Challenge ---
print("\n" + "="*60)
print("CHALLENGES - Try these!")
print("="*60)
print("1. Modify is_prime to count primes up to 1,000,000 and time it")
print("2. Find the 1000th prime")
print("3. Prove sum of first n integers = n(n+1)/2 for n=100")
print(f"   Check: sum 1..100 = {sum(range(1,101))}, formula = {100*101//2}")
print("4. Explore Collatz conjecture: start at 27, how many steps to 1?")
def collatz(n):
    steps=0
    seq=[n]
    while n!=1:
        n = n//2 if n%2==0 else 3*n+1
        seq.append(n)
        steps+=1
    return steps, seq

steps, seq = collatz(27)
print(f"   Collatz(27): {steps} steps, peaks at {max(seq)}")
