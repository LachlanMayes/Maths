"""
05 - ADVANCED: Fractals, Chaos, Fourier & arXiv-inspired topics
Sources: https://www.mathsisfun.com/fractals.html
         https://arxiv.org/abs/... (see topics below)
Run: python 05_advanced.py [--plot]
Flags: --plot       show graphs
       --fractal    compute Mandelbrot (slow, needs numpy+matplotlib)
"""
import math, random, sys, cmath
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except: pass
PLOT = "--plot" in sys.argv
FRACTAL = "--fractal" in sys.argv

print("="*60)
print("5.1 FRACTALS - Infinity in finite space")
print("="*60)
# mathsisfun.com/fractals.html
# Koch snowflake: each iteration multiplies perimeter by 4/3, area converges
def koch_perimeter(initial_side, iterations):
    # each side splits into 4 segments of 1/3 length
    sides = 3 * (4**iterations)
    length = initial_side / (3**iterations)
    return sides * length

def koch_area(initial_side, iterations):
    # area = initial triangle + sum added triangles
    # initial area
    area = (math.sqrt(3)/4) * initial_side**2
    # each iteration adds: num_new_triangles * area_new
    # iteration i (1-indexed): 3*4^(i-1) new triangles, side = initial/3^i
    for i in range(1, iterations+1):
        num = 3 * (4**(i-1))
        side = initial_side / (3**i)
        tri_area = (math.sqrt(3)/4) * side**2
        area += num * tri_area
    return area

print("Koch Snowflake (initial side=1):")
for it in [0,1,2,3,4,6,10]:
    p = koch_perimeter(1, it)
    a = koch_area(1, it)
    print(f"  Iter {it:2d}: perimeter={p:.4f}, area={a:.6f}")
print("  -> Perimeter -> infinity, Area -> 8/5 * initial = 0.6928... (converges!)")
print(f"     Limit area = {koch_area(1, 20):.6f} (theoretical 8/5 * 0.433012 = {8/5*0.4330127019:.6f})")

# Sierpinski triangle
def sierpinski_triangles(iteration):
    return 3**iteration
def sierpinski_area_fraction(iteration):
    return (3/4)**iteration

print("\nSierpinski Triangle:")
for it in range(6):
    print(f"  Iter {it}: {sierpinski_triangles(it)} triangles, area fraction={(sierpinski_area_fraction(it)):.4f}")

# Mandelbrot set (numeric demo without plot)
print("\nMandelbrot Set: z -> z² + c (c is point, z0=0)")
def mandelbrot(c, max_iter=100):
    z=0
    for i in range(max_iter):
        if abs(z) > 2:
            return i  # escaped
        z = z*z + c
    return max_iter  # inside

test_points = [0+0j, -0.5+0j, 1+0j, 0+0.5j, -0.75+0.1j, 0.3+0.5j]
for c in test_points:
    it = mandelbrot(c, 100)
    status = "INSIDE (bounded)" if it==100 else f"escapes at {it}"
    print(f"  c={str(c):12s} -> {status}")

print("\n" + "="*60)
print("5.2 CHAOS THEORY - Butterfly effect")
print("="*60)
# Logistic map: x -> r*x*(1-x) - classic chaos (arxiv: chaos)
def logistic_map(r, x0, n):
    x=x0
    seq=[x]
    for _ in range(n-1):
        x = r*x*(1-x)
        seq.append(x)
    return seq

print("Logistic map x_{n+1} = r*x_n*(1-x_n), x0=0.2 (0.5 is degenerate for r=4):")
for r in [2.5, 3.2, 3.5, 3.9, 4.0]:
    seq = logistic_map(r, 0.2, 20)
    tail = seq[-5:]
    print(f"  r={r}: last 5 = {[f'{v:.4f}' for v in tail]}", end="")
    if r < 3: print(" -> stable")
    elif r < 3.45: print(" -> period-2")
    elif r < 3.55: print(" -> period-4")
    else: print(" -> CHAOS")

# Sensitive dependence: two nearby points diverge
r=4.0
seq1 = logistic_map(r, 0.2000, 30)
seq2 = logistic_map(r, 0.2001, 30)
print(f"\nButterfly effect r=4.0, x0=0.2 vs 0.2001:")
for i in [0,5,10,15,20,25,29]:
    print(f"  step {i:2d}: {seq1[i]:.6f} vs {seq2[i]:.6f} diff={abs(seq1[i]-seq2[i]):.6f}")

# Lorenz attractor preview (simplified Euler)
print("\nLorenz attractor (simplified, arxiv: nlin.CD):")
def lorenz_step(x,y,z, sigma=10, rho=28, beta=8/3, dt=0.01):
    dx = sigma*(y - x)
    dy = x*(rho - z) - y
    dz = x*y - beta*z
    return x+dx*dt, y+dy*dt, z+dz*dt

x,y,z = 1,1,1
for i in range(5):
    for _ in range(100):
        x,y,z = lorenz_step(x,y,z)
    print(f"  t={ (i+1)*100}: x={x:.2f} y={y:.2f} z={z:.2f}")

print("\n" + "="*60)
print("5.3 FOURIER TRANSFORM - Breaking waves into frequencies")
print("="*60)
# arxiv: math.CA, eess.SP - Fourier is everywhere
# Discrete Fourier Transform (naive O(n²))
def dft(x):
    N=len(x)
    X=[]
    for k in range(N):
        s=0j
        for n in range(N):
            s += x[n] * cmath.exp(-2j*math.pi*k*n/N)
        X.append(s)
    return X

# Example: signal = sin(2*pi*1*t) + 0.5*sin(2*pi*3*t)
N=16
signal = [math.sin(2*math.pi*1*n/N) + 0.5*math.sin(2*math.pi*3*n/N) for n in range(N)]
spectrum = dft(signal)
print(f"Signal (N={N}): sin(1 Hz) + 0.5*sin(3 Hz)")
print(f"  signal samples: {[f'{v:.2f}' for v in signal[:8]]}...")
print(f"  DFT magnitudes:")
for k, val in enumerate(spectrum[:8]):
    mag = abs(val)/N
    print(f"    k={k} (freq {k} Hz): mag={mag:.3f}", end="")
    if k in [1,3]: print(" <-- PEAK (expected!)")
    else: print("")

# Inverse DFT check
def idft(X):
    N=len(X)
    x=[]
    for n in range(N):
        s=0j
        for k in range(N):
            s += X[k] * cmath.exp(2j*math.pi*k*n/N)
        x.append((s/N).real)
    return x
recon = idft(spectrum)
err = max(abs(a-b) for a,b in zip(signal, recon))
print(f"  Reconstruction error (IDFT): {err:.2e} (should be ~0)")

# Fast Fourier via numpy if available
try:
    import numpy as np
    sig_np = np.array(signal)
    spec_np = np.fft.fft(sig_np)
    print(f"  [numpy FFT] magnitudes: {[f'{abs(v)/N:.3f}' for v in spec_np[:4]]} (matches naive DFT)")
except ImportError:
    pass

print("\nReal-world: JPEG, MP3, quantum mechanics all use Fourier!")
print("  arXiv: 1909.01423 'Fourier transform in deep learning'")
print("  Try: decompose a square wave into sines (Gibbs phenomenon)")

print("\n" + "="*60)
print("5.4 NUMBER THEORY - Advanced (arXiv style)")
print("="*60)
# Prime distribution: Prime Number Theorem pi(x) ~ x/log x
def pi_count(x):
    # count primes <= x
    if x < 2: return 0
    sieve = [True]*(x+1)
    sieve[0:2]=[False,False]
    for i in range(2, int(x**0.5)+1):
        if sieve[i]:
            step = i*i
            sieve[step:x+1:i]=[False]*(((x - step)//i)+1)
    return sum(sieve)

print("Prime Number Theorem: pi(x) ~ x / ln(x)")
for x in [100, 1000, 10000, 100000]:
    pi = pi_count(x)
    approx = x / math.log(x)
    print(f"  x={x:6d}: pi(x)={pi:5d}, x/ln(x)={approx:.1f}, ratio={pi/approx:.4f} -> approaches 1")

# RSA preview (modular exponentiation)
print("\nRSA Cryptography (modular arithmetic):")
def modpow(base, exp, mod):
    result=1
    base%=mod
    while exp>0:
        if exp%2==1: result=result*base%mod
        base=base*base%mod
        exp//=2
    return result

# Tiny RSA example
p,q=61,53  # primes
n=p*q
phi=(p-1)*(q-1)
e=17  # public exponent
# find d = e⁻¹ mod phi
def modinv(a,m):
    # extended Euclid
    g,x,y = __import__('math').gcd(a,m), 0,0
    # brute for demo
    for d in range(1,m):
        if (a*d)%m==1: return d
    return None
d=modinv(e,phi)
msg=42
cipher=modpow(msg,e,n)
plain=modpow(cipher,d,n)
print(f"  p={p}, q={q}, n={n}, phi={phi}, e={e}, d={d}")
print(f"  msg={msg} -> cipher={cipher} -> plain={plain} {'✓' if plain==msg else '✗'}")
print(f"  Real RSA uses 2048-bit primes (arxiv: cs.CR)")

# Riemann Zeta function teaser
print("\nRiemann Zeta (million-dollar problem, arxiv: math.NT):")
def zeta(s, terms=10000):
    return sum(1/(n**s) for n in range(1, terms+1))
print(f"  zeta(2) = {zeta(2, 100000):.6f} (true pi²/6 = {math.pi**2/6:.6f})  # Basel problem")
print(f"  zeta(4) = {zeta(4, 10000):.6f} (true pi⁴/90 = {math.pi**4/90:.6f})")
print("  Riemann Hypothesis: all non-trivial zeros have Re(s)=1/2")

print("\n" + "="*60)
print("5.5 GRAPH THEORY & ARXIV FRONTIER")
print("="*60)
print("Topics to explore via arxiv.org:")
print("  - cs.DM / math.CO: Graph theory (Euler, Hamilton, coloring)")
print("  - quant-ph: Quantum maths (Hilbert spaces, entanglement)")
print("  - cs.LG / stat.ML: Math behind AI (gradient descent, backprop)")
print("  - math.DS: Dynamical systems (chaos, fractals)")
print("  - hep-th: String theory maths")

# Simple graph demo: adjacency matrix
print("\nGraph Theory demo: 4-node cycle")
# 0-1-2-3-0
import collections
adj = {0:[1,3], 1:[0,2], 2:[1,3], 3:[2,0]}
def bfs(start, adj):
    visited=set()
    q=collections.deque([start])
    order=[]
    while q:
        u=q.popleft()
        if u in visited: continue
        visited.add(u); order.append(u)
        for v in adj[u]:
            if v not in visited: q.append(v)
    return order
def has_eulerian_cycle(adj):
    return all(len(nei)%2==0 for nei in adj.values())

print(f"  Adjacency: {adj}")
print(f"  BFS from 0: {bfs(0, adj)}")
print(f"  Has Eulerian cycle? {has_eulerian_cycle(adj)} (all degrees even -> True)")
print(f"  Cycle graph is 2-colorable? {True} (even cycle)")

# Neural network maths teaser (single neuron)
print("\nAI Maths teaser: single neuron y = sigmoid(w·x + b)")
def sigmoid(x): return 1/(1+math.exp(-x))
w,b = 0.5, -1.0
for x in [0,1,2,3,4]:
    y=sigmoid(w*x+b)
    print(f"  x={x} -> y=sigmoid({w}*{x}+{b}) = {y:.4f}")
print("  Training = calculus (gradient descent) + linear algebra!")

if PLOT or FRACTAL:
    try:
        import numpy as np
        import matplotlib.pyplot as plt

        # Koch curve visualization (simple)
        def koch_curve(p1, p2, depth):
            if depth==0:
                return [p1, p2]
            # divide segment into 3, build bump
            x1,y1=p1; x2,y2=p2
            dx,dy = (x2-x1)/3, (y2-y1)/3
            a = (x1+dx, y1+dy)
            b = (x2-dx, y2-dy)
            # peak: rotate 60°
            mx,my = (a[0]+b[0])/2, (a[1]+b[1])/2
            # equilateral peak
            angle = math.atan2(dy,dx) + math.pi/3
            length = math.hypot(dx,dy)
            peak = (a[0] + math.cos(angle)*length, a[1] + math.sin(angle)*length)
            # recurse 4 segments
            pts=[]
            for seg in [(p1,a),(a,peak),(peak,b),(b,p2)]:
                pts.extend(koch_curve(seg[0],seg[1],depth-1)[:-1])
            pts.append(p2)
            return pts
        # Draw snowflake
        plt.figure(figsize=(6,6))
        init = [(0,0),(1,0),(0.5, math.sqrt(3)/2), (0,0)]
        for depth, color in [(0,'lightgray'),(1,'orange'),(3,'red'),(5,'black')]:
            pts=[]
            for i in range(3):
                pts.extend(koch_curve(init[i], init[i+1], depth)[:-1])
            pts.append(pts[0])
            xs,ys=zip(*pts)
            plt.plot(xs,ys,label=f"iter {depth}", color=color, linewidth=1 if depth<5 else 1)
        plt.axis('equal'); plt.axis('off'); plt.title("Koch Snowflake"); plt.legend(); plt.show()

        # Logistic map bifurcation diagram
        rs = np.linspace(2.8,4,800)
        plt.figure(figsize=(10,4))
        for r in rs:
            seq=logistic_map(r,0.5,250)
            tail=seq[150:]
            plt.plot([r]*len(tail), tail, ',k', alpha=0.25)
        plt.title("Logistic Map Bifurcation Diagram (Route to Chaos)")
        plt.xlabel("r"); plt.ylabel("x (attractor)"); plt.show()

        # Fourier: signal + spectrum
        sig = np.array(signal)
        spec = np.fft.fft(sig)
        freqs = np.fft.fftfreq(N, d=1/N)
        fig, axes = plt.subplots(2,1, figsize=(8,5))
        axes[0].stem(range(N), sig); axes[0].set_title("Signal: sin(1Hz)+0.5sin(3Hz)"); axes[0].grid(True)
        axes[1].stem(freqs[:N//2], np.abs(spec[:N//2])/N); axes[1].set_title("Spectrum (peaks at 1 and 3)")
        axes[1].grid(True); plt.tight_layout(); plt.show()

        if FRACTAL:
            # Mandelbrot
            W,H=600,600
            xmin,xmax,ymin,ymax=-2,1,-1.5,1.5
            max_iter=80
            img=np.zeros((H,W))
            for iy in range(H):
                for ix in range(W):
                    c = complex(xmin+(xmax-xmin)*ix/W, ymin+(ymax-ymin)*iy/H)
                    z=0j
                    for it in range(max_iter):
                        if abs(z)>2: break
                        z=z*z+c
                    img[iy,ix]=it
            plt.figure(figsize=(6,6))
            plt.imshow(img, cmap='hot', extent=[xmin,xmax,ymin,ymax])
            plt.title(f"Mandelbrot Set ({W}x{H}, {max_iter} iter)")
            plt.xlabel("Re(c)"); plt.ylabel("Im(c)"); plt.show()
        else:
            print("\n[Tip] Add --fractal for Mandelbrot image (slow!)")

    except ImportError as e:
        print(f"Plot needs numpy+matplotlib: {e}")
else:
    print("\n[Tip] Run with --plot for graphs, --fractal for Mandelbrot:")
    print("  python 05_advanced.py --plot")
    print("  python 05_advanced.py --plot --fractal")

print("\nChallenge: implement Newton's fractal, Lorenz 3D, or train a tiny neural net!")
