"""
12 - DISCRETE MATHEMATICS: Combinatorics, Graph Theory, Sequences
Sources:
  - https://mathworld.wolfram.com/topics/DiscreteMathematics.html
  - https://www.mathsisfun.com/combinatorics/combinations-permutations.html
  - https://www.mathsisfun.com/sets/graph-theory.html
  - arXiv: math.CO, cs.DM
Run: python 12_discrete_mathematics.py [--plot]
"""
import sys
try: sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
except: pass
import math, itertools, collections, random

PLOT="--plot" in sys.argv

print("="*60)
print("12.1 COMBINATORICS - Permutations & Combinations")
print("="*60)
# mathsisfun combinatorics

def perm(n,r): return math.perm(n,r) if hasattr(math,'perm') else math.factorial(n)//math.factorial(n-r)
def comb(n,r): return math.comb(n,r) if hasattr(math,'comb') else math.factorial(n)//(math.factorial(r)*math.factorial(n-r))

print(f"Factorial 5!={math.factorial(5)}, 10!={math.factorial(10)}")
print(f"Permutations P(10,3)={perm(10,3)} (order matters)")
print(f"Combinations C(10,3)={comb(10,3)} (order not, = P/r!)")
print(f"Stars and bars: distribute 10 identical balls into 4 boxes = C(13,3)={comb(13,3)}")

# Examples
print(f"\nExamples:")
print(f"  5 cards from 52: C(52,5)={comb(52,5)} poker hands")
print(f"  Arrange 3 of 10 books: P(10,3)={perm(10,3)}")
print(f"  Binomial coeff row 5: {[comb(5,k) for k in range(6)]} (Pascal)")
# With repetition
print(f"  Combinations with repetition C(n+r-1,r): choose 3 scoops from 5 flavors = C(7,3)={comb(7,3)}")

# Inclusion-exclusion (Wolfram)
print(f"\nInclusion-Exclusion: count numbers <=100 divisible by 2 or 3")
div2=len([n for n in range(1,101) if n%2==0])
div3=len([n for n in range(1,101) if n%3==0])
div6=len([n for n in range(1,101) if n%6==0])
print(f"  |A|=50, |B|=33, |A cap B|=16 => |A union B|={div2+div3-div6} vs brute {len([n for n in range(1,101) if n%2==0 or n%3==0])}")

# Pigeonhole (Wolfram)
print(f"\nPigeonhole: 367 people => at least 2 share birthday (366 possible inc leap)")

print("\n" + "="*60)
print("12.2 SEQUENCES & GENERATING FUNCTIONS")
print("="*60)
# Wolfram Sequences, GeneratingFunctions

def fibonacci(n):
    a,b=0,1
    seq=[]
    for _ in range(n): seq.append(a); a,b=b,a+b
    return seq
print(f"Fibonacci 10: {fibonacci(10)}")
# Recurrence: F(n)=F(n-1)+F(n-2)
# Generating function demo: 1/(1-x-x^2) expands to Fib
print(f"Generating function 1/(1-x-x^2) coefficients are Fib numbers")

# Catalan numbers (Wolfram)
def catalan(n): return comb(2*n,n)//(n+1)
print(f"Catalan numbers (trees, brackets): {[catalan(n) for n in range(8)]}")

# Binomial theorem: (x+y)^n = sum C(n,k) x^{n-k} y^k
def binomial_expand(n):
    terms=[]
    for k in range(n+1):
        terms.append(f"C({n},{k}) x^{n-k} y^{k}")
    return " + ".join(terms)
print(f"(x+y)^5 = {binomial_expand(5)}")
print(f"  Coeff: {[comb(5,k) for k in range(6)]}")

# Derangements !n = n! sum (-1)^k/k!
def derangements(n): return round(math.factorial(n)/math.e)  # approx
for n in range(1,7):
    exact=math.factorial(n)*sum((-1)**k/math.factorial(k) for k in range(n+1))
    print(f"  Derangements !{n}={round(exact)} (approx n!/e={derangements(n)})")

print("\n" + "="*60)
print("12.3 GRAPH THEORY (mathsisfun, Wolfram)")
print("="*60)

# Represent graph as adjacency list
graph={
    0:[1,2],
    1:[0,2,3],
    2:[0,1,3],
    3:[1,2,4],
    4:[3]
}
# Degree
for v in graph:
    print(f"  Vertex {v}: degree {len(graph[v])}, neighbors {graph[v]}")
print(f"  Sum degrees = {sum(len(graph[v]) for v in graph)} (=2*edges={sum(len(graph[v]) for v in graph)//2} edges, Handshaking Lemma)")

# BFS & DFS
def bfs(graph,start):
    visited=set(); q=collections.deque([start]); order=[]
    while q:
        v=q.popleft()
        if v in visited: continue
        visited.add(v); order.append(v)
        for nb in graph[v]:
            if nb not in visited: q.append(nb)
    return order
def dfs(graph,start, visited=None, order=None):
    if visited is None: visited=set(); order=[]
    visited.add(start); order.append(start)
    for nb in graph[start]:
        if nb not in visited: dfs(graph,nb,visited,order)
    return order

print(f"  BFS from 0: {bfs(graph,0)}")
print(f"  DFS from 0: {dfs(graph,0)}")
# Connected?
def is_connected(g):
    return len(bfs(g, next(iter(g))))==len(g)
print(f"  Is connected? {is_connected(graph)}")

# Eulerian trail: all vertices even degree -> circuit; 0 or 2 odd -> trail
def has_eulerian(graph):
    odds=sum(1 for v in graph if len(graph[v])%2==1)
    return odds==0 or odds==2
print(f"  Eulerian trail possible? {has_eulerian(graph)} (0 or 2 odd degrees) => {sum(1 for v in graph if len(graph[v])%2==1)} odds")

# Hamiltonian? NP-complete, brute for small
def has_hamiltonian_path(graph):
    nodes=list(graph)
    for perm in itertools.permutations(nodes):
        ok=all(perm[i+1] in graph[perm[i]] for i in range(len(perm)-1))
        if ok: return perm
    return None
print(f"  Hamiltonian path exists? {has_hamiltonian_path(graph)}")

# Coloring (Four Color Theorem Wolfram, mathsisfun coloring)
print(f"\nGraph coloring: bound chromatic number <= max degree +1 (Brook's)")
print(f"  This graph likely 3-colorable")

# Dijkstra shortest path
def dijkstra(graph_w, start):
    # graph_w: {u: [(v,w)]}
    import heapq
    dist={v: float('inf') for v in graph_w}
    dist[start]=0
    pq=[(0,start)]
    while pq:
        d,u=heapq.heappop(pq)
        if d!=dist[u]: continue
        for v,w in graph_w[u]:
            nd=d+w
            if nd<dist[v]:
                dist[v]=nd
                heapq.heappush(pq,(nd,v))
    return dist

wg={0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[(4,3)],4:[]}
print(f"  Weighted graph {wg}")
print(f"  Shortest from 0: {dijkstra(wg,0)}")

# Trees: V = E+1, no cycles
tree={0:[1,2],1:[0,3,4],2:[0],3:[1],4:[1]}
print(f"\nTree {tree}: V={len(tree)}, E={sum(len(v) for v in tree.values())//2}, V=E+1? {len(tree)==sum(len(v) for v in tree.values())//2+1}")

print("\n" + "="*60)
print("12.4 RECURSION & DYNAMIC PROGRAMMING")
print("="*60)

# Fibonacci via DP vs recursion
def fib_rec(n):
    if n<=1: return n
    return fib_rec(n-1)+fib_rec(n-2)
def fib_dp(n, memo={}):
    if n in memo: return memo[n]
    if n<=1: memo[n]=n
    else: memo[n]=fib_dp(n-1)+fib_dp(n-2)
    return memo[n]

print(f"  Fib rec(10)={fib_rec(10)}, dp(30)={fib_dp(30)} (dp avoids exponential)")

# Coin change: ways to make amount
def coin_change(amount, coins):
    dp=[0]*(amount+1); dp[0]=1
    for c in coins:
        for i in range(c, amount+1):
            dp[i]+=dp[i-c]
    return dp[amount]
print(f"  Coin change 10 with [1,2,5]: {coin_change(10,[1,2,5])} ways")

# Knapsack preview (0/1)
def knapsack(values, weights, W):
    n=len(values)
    dp=[[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(W+1):
            if weights[i-1]<=w:
                dp[i][w]=max(dp[i-1][w], dp[i-1][w-weights[i-1]]+values[i-1])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][W]
print(f"  Knapsack values [60,100,120] weights [10,20,30] W50 -> max {knapsack([60,100,120],[10,20,30],50)}")

print("\n" + "="*60)
print("12.5 BOOLEAN & CODING THEORY (Wolfram CodingTheory)")
print("="*60)
# Hamming distance, error detection
def hamming(s1,s2): return sum(c1!=c2 for c1,c2 in zip(s1,s2))
print(f"  Hamming('10101','10011')={hamming('10101','10011')}")
# Simple parity: add bit to make even weight
def parity_bit(s): return str(sum(int(c) for c in s)%2)
msg="1011"
print(f"  Message {msg} with even parity -> {msg+parity_bit(msg)}")
print(f"  Hamming(7,4) can correct 1-bit errors, detect 2 (Wolfram)")

if PLOT:
    try:
        import matplotlib.pyplot as plt, networkx as nx
        G=nx.Graph()
        for u in graph:
            for v in graph[u]:
                if u<v: G.add_edge(u,v)
        plt.figure()
        nx.draw(G, with_labels=True, node_color='lightblue', node_size=800)
        plt.title("Graph Visualization"); plt.show()

        # Pascal's triangle binomial coeffs heatmap
        import numpy as np
        n=16
        tri=np.zeros((n,n))
        for i in range(n):
            for j in range(i+1):
                tri[i,j]=comb(i,j)
        plt.figure()
        plt.imshow(tri, cmap='viridis')
        plt.title("Pascal's Triangle (binomial coeffs)"); plt.colorbar(); plt.show()

        # Catalan growth
        xs=list(range(10))
        plt.figure()
        plt.plot(xs, [catalan(x) for x in xs], 'o-')
        plt.title("Catalan Numbers"); plt.xlabel("n"); plt.ylabel("C(n)"); plt.grid(True); plt.show()
    except ImportError as e:
        # Fallback without networkx
        import matplotlib.pyplot as plt
        import numpy as np
        print(f"For graph plots install networkx: pip install networkx ; {e}")
        # Simple plot: degrees
        degrees=[len(graph[v]) for v in graph]
        plt.figure()
        plt.bar(list(graph.keys()), degrees)
        plt.title("Vertex Degrees"); plt.xlabel("vertex"); plt.ylabel("degree"); plt.show()
        n=16
        tri=np.zeros((n,n))
        for i in range(n):
            for j in range(i+1):
                tri[i,j]=comb(i,j)
        plt.figure()
        plt.imshow(tri, cmap='viridis')
        plt.title("Pascal Triangle"); plt.colorbar(); plt.show()
else:
    print("\n[Tip] --plot for graph & Pascal: python 12_discrete_mathematics.py --plot")

print("\nChallenge: implement Dijkstra from scratch, or find chromatic number via backtracking!")
