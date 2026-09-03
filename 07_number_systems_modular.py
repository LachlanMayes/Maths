"""
07 - NUMBERS: Systems, Bases, Modular & Number Theory Deep Dive
Sources:
  - https://www.mathsisfun.com/numbers/index.html
  - https://www.mathsisfun.com/binary-digits.html, hexadecimals.html, bases.html
  - https://mathworld.wolfram.com/topics/NumberTheory.html
  - https://mathworld.wolfram.com/ContinuedFraction.html
  - arXiv: math.NT (Number Theory)
Run: python 07_number_systems_modular.py [--plot]
"""
import sys
try: sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
except: pass
import math, random

PLOT = "--plot" in sys.argv

print("="*60)
print("7.1 NUMBER BASES - Binary, Hex, Roman, Arbitrary")
print("="*60)
# mathsisfun: binary, hex, bases, roman

def to_base(n, base):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n==0: return "0"
    neg=n<0; n=abs(n)
    res=""
    while n>0:
        res=digits[n%base]+res
        n//=base
    return ("-" if neg else "")+res

def from_base(s, base):
    return int(s, base)  # python handles up to 36

for n in [42, 255, 1023, 2026]:
    print(f"  {n:4d} -> binary {to_base(n,2):12s} hex {to_base(n,16):4s} oct {to_base(n,8):5s} base12 {to_base(n,12):4s}")

# Binary arithmetic demo
a,b=0b1011,0b0110  # 11 + 6
print(f"\nBinary: {bin(a)} ({a}) + {bin(b)} ({b}) = {bin(a+b)} ({a+b})")
print(f"  Hex: {hex(255)} = {to_base(255,16)}, RGB #FF00FF = {int('FF00FF',16)}")

# Roman numerals (mathsisfun Roman)
roman_map=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
def to_roman(n):
    res=""
    for val,sym in roman_map:
        while n>=val:
            res+=sym; n-=val
    return res
for n in [4,9,58,1994,2026]:
    print(f"  {n} -> Roman {to_roman(n)}")

# Arbitrary base floating?
print(f"\nBase 36 demo: {to_base(123456,36)} (max single-char digit)")

print("\n" + "="*60)
print("7.2 MODULAR ARITHMETIC - Wolfram Congruences")
print("="*60)
# mathsisfun modulo, Wolfram Congruences (57 entries)

def mod(a,m): return a % m

print(f"  17 mod 5 = {mod(17,5)}, -3 mod 7 = {mod(-3,7)} (Python wraps positive)")
print(f"  Clock arithmetic: 8 + 7 mod 12 = {(8+7)%12} (8am +7h = 3pm)")

# Modular exponentiation (fast)
def modpow(b,e,m):
    r=1; b%=m
    while e>0:
        if e&1: r=r*b%m
        b=b*b%m; e>>=1
    return r
print(f"  3^200 mod 100 = {modpow(3,200,100)}")
print(f"  Fermat's little: 2^6 mod 7 = {modpow(2,6,7)} (should be 1 for prime 7)")

# GCD via Euclid & extended Euclid (Wolfram)
def egcd(a,b):
    if b==0: return (a,1,0)
    g,x1,y1=egcd(b, a%b)
    return (g, y1, x1 - (a//b)*y1)

a,b=240,46
g,x,y=egcd(a,b)
print(f"\nExtended Euclid: gcd({a},{b})={g}, {a}*{x} + {b}*{y} = {a*x+b*y} (=g)")

def modinv(a,m):
    g,x,y=egcd(a,m)
    return x % m if g==1 else None
print(f"  Modular inverse of 3 mod 11 = {modinv(3,11)} (3*4=12=1 mod11)")
print(f"  Solve 3x = 7 mod 11 => x = {7*modinv(3,11)%11}")

# Chinese Remainder Theorem (Wolfram)
def crt(remainders, moduli):
    # x = a_i mod m_i, moduli coprime
    M=math.prod(moduli)
    x=0
    for a,m in zip(remainders, moduli):
        Mi=M//m
        x += a * modinv(Mi,m) * Mi
    return x % M
print(f"\nCRT: x=2 mod3, x=3 mod5, x=2 mod7 => x={crt([2,3,2],[3,5,7])} mod105")
print(f"  Check: {crt([2,3,2],[3,5,7])%3}, {crt([2,3,2],[3,5,7])%5}, {crt([2,3,2],[3,5,7])%7}")

# Divisibility rules (mathsisfun)
def divisibility(n):
    rules={}
    rules['2']=n%2==0
    rules['3']=sum(map(int,str(n)))%3==0
    rules['9']=sum(map(int,str(n)))%9==0
    rules['5']=str(n).endswith(('0','5'))
    return rules
print(f"\nDivisibility of 12345: {divisibility(12345)}")

print("\n" + "="*60)
print("7.3 PRIME THEORY - Deeper (Wolfram Prime Numbers)")
print("="*60)

def is_prime(n):
    if n<2: return False
    if n%2==0: return n==2
    for i in range(3,int(math.isqrt(n))+1,2):
        if n%i==0: return False
    return True

def prime_factors(n):
    d=2; f=[]
    while d*d<=n:
        while n%d==0: f.append(d); n//=d
        d+=1 if d==2 else 2
    if n>1: f.append(n)
    return f

# Miller-Rabin deterministic for <2^64
def is_probable_prime(n):
    if n<2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n%p==0: return n==p
    d=n-1; s=0
    while d%2==0: d//=2; s+=1
    for a in [2,325,9375,28178,450775,9780504,1795265022]:
        if a%n==0: continue
        x=pow(a,d,n)
        if x==1 or x==n-1: continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True

print(f"is_prime(97)={is_prime(97)}, is_prime(100)={is_prime(100)}")
print(f"Miller-Rabin 2^31-1 (Mersenne) prime? {is_probable_prime(2**31-1)}")
print(f"Prime factors of 1001={prime_factors(1001)} (7*11*13)")
print(f"Euler totient phi(10)=? count coprime: {[n for n in range(1,10) if math.gcd(n,10)==1]} -> {len([n for n in range(1,10) if math.gcd(n,10)==1])}")

def euler_phi(n):
    result=n
    for p in set(prime_factors(n)):
        result=result//p*(p-1)
    return result
for n in [10,12,100,101]:
    print(f"  phi({n})={euler_phi(n)}")
print(f"  Euler's theorem: a^phi(n)=1 mod n for coprime a. e.g., 3^phi(10)=3^4={pow(3,4,10)} mod10")

print("\n" + "="*60)
print("7.4 SPECIAL NUMBERS & CONTINUED FRACTIONS")
print("="*60)
# Wolfram Constants, ContinuedFractions, Transcendental Numbers

# Continued fraction for pi (Wolfram ContinuedFraction)
def continued_fraction(x, terms=10):
    cf=[]
    for _ in range(terms):
        a=math.floor(x)
        cf.append(a)
        f=x-a
        if f<1e-12: break
        x=1/f
    return cf

def cf_to_fraction(cf):
    num,den=1,0
    for a in reversed(cf):
        num,den = a*num+den, num
    return num,den

for val,name in [(math.pi,"pi"),(math.e,"e"),(math.sqrt(2),"sqrt2"),((1+math.sqrt(5))/2,"phi")]:
    cf=continued_fraction(val,10)
    num,den=cf_to_fraction(cf[:5])
    print(f"  {name:6s} CF={cf[:6]}... approx {cf[:5]} = {num}/{den} = {num/den:.8f} vs {val:.8f}")

# Rational approximation
print(f"\nBest rational for pi with denom <1000: 355/113={355/113:.8f} error {abs(355/113-math.pi):.2e}")
# Demonstrates pi is irrational/transcendental

# Transcendental vs algebraic
print(f"\nAlgebraic: sqrt(2) solves x^2-2=0; Transcendental: pi, e cannot be root of integer polynomial")
print(f"  Liouville: e={math.e:.10f} (transcendental)")

# Irrationality proof for e via series (Wolfram)
print(f"\nFactorial number system & e:")
print(f"  e = sum 1/n! = {[1/math.factorial(n) for n in range(6)]} sum-> {sum(1/math.factorial(n) for n in range(10)):.8f}")

# Perfect, abundant, deficient numbers (Wolfram Divisors)
def divisor_sum(n): return sum(i for i in range(1,n) if n%i==0)
for n in [6,12,28,18,496]:
    s=divisor_sum(n)
    kind="perfect" if s==n else "abundant" if s>n else "deficient"
    print(f"  {n}: sum proper divisors={s} -> {kind}")

print("\n" + "="*60)
print("7.5 NUMERAL SYSTEMS & PLACE VALUE")
print("="*60)
# mathsisfun place value
print(f"  Place value 2026 = 2*1000 +0*100+2*10+6*1")
# Floating point nuance
print(f"  0.1+0.2={0.1+0.2} (not 0.3 due to binary floating point!)")
print(f"  Decimal works base10: 0.1 = 1/10 not representable in binary exactly")
# Big integers Python handles arbitrarily
print(f"  Python big int: 100! = {math.factorial(100)} has {len(str(math.factorial(100)))} digits")
print(f"  2^1000 first 20 digits: {str(2**1000)[:20]}... ({len(str(2**1000))} digits)")

if PLOT:
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        # Ulam spiral
        def ulam(n):
            # generate spiral coords for 1..n^2
            x=y=0; dx,dy=1,0; step=1; num=1
            pts={}
            pts[1]=(0,0)
            while num < n*n:
                for _ in range(2):
                    for _ in range(step):
                        if num>=n*n: break
                        x+=dx; y+=dy; num+=1; pts[num]=(x,y)
                    dx,dy=-dy,dx
                step+=1
            return pts
        pts=ulam(21)
        xs=[pts[k][0] for k in pts if is_probable_prime(k)]
        ys=[pts[k][1] for k in pts if is_probable_prime(k)]
        plt.figure(figsize=(5,5))
        plt.scatter(xs,ys,s=10,c='black')
        plt.title("Ulam Spiral (primes as dots, 21x21) - diagonals visible")
        plt.axis('equal'); plt.axis('off'); plt.show()

        # Totient plot
        ns=list(range(1,100))
        phis=[euler_phi(n) for n in ns]
        plt.figure()
        plt.scatter(ns, phis, s=10)
        plt.plot(ns, ns, 'r--', alpha=0.3)
        plt.title("Euler Totient phi(n) <= n, equality at primes"); plt.xlabel("n"); plt.ylabel("phi(n)"); plt.grid(True); plt.show()

        # Continued fraction convergents for pi
        cf=continued_fraction(math.pi,10)
        errs=[]
        for i in range(1,7):
            num,den=cf_to_fraction(cf[:i])
            errs.append(abs(num/den-math.pi))
        plt.figure()
        plt.semilogy(range(1,7), errs, 'o-')
        plt.title("Convergents to pi: error vs terms"); plt.xlabel("terms"); plt.ylabel("error"); plt.grid(True); plt.show()
    except Exception as e:
        print(f"Plot error: {e}")
else:
    print("\n[Tip] Run with --plot for Ulam spiral & totient: python 07_number_systems_modular.py --plot")

print("\nChallenge: implement RSA keygen (1024-bit), or find continued fraction for sqrt(7) periodic!")
print("arXiv: search math.NT for recent prime gaps")
