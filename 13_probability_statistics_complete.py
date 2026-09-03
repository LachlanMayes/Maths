"""
13 - PROBABILITY & STATISTICS COMPLETE
Sources:
  - https://www.mathsisfun.com/data/index.html (full Data chapter)
  - https://mathworld.wolfram.com/topics/ProbabilityandStatistics.html
  - arXiv: math.ST, stat.ML
Run: python 13_probability_statistics_complete.py [--plot]
"""
import sys
try: sys.stdout.reconfigure(encoding='utf-8'); sys.stderr.reconfigure(encoding='utf-8')
except: pass
import math, random, statistics

PLOT="--plot" in sys.argv
try: import numpy as np; HAS_NP=True
except: HAS_NP=False

print("="*60)
print("13.1 DATA DISPLAY & SAMPLING (mathsisfun data-index)")
print("="*60)

data=[2,4,4,4,5,5,7,9,9,10,12,14,15]
print(f"Data: {data} (n={len(data)})")
# Histograms concept
def histogram(data, bins):
    mn,mx=min(data),max(data)
    width=(mx-mn)/bins
    counts=[0]*bins
    for x in data:
        idx=min(int((x-mn)/width), bins-1)
        counts[idx]+=1
    return counts, mn, width
counts, mn, w=histogram(data,4)
print(f"  Histogram 4 bins width {w:.1f}: {counts}")

# Sampling demo
print(f"\nSampling: population mean vs sample mean")
random.seed(0)
pop=[random.gauss(50,10) for _ in range(1000)]
sample=random.sample(pop,30)
print(f"  Population mean {statistics.mean(pop):.2f}, sample (30) mean {statistics.mean(sample):.2f}")

print("\n" + "="*60)
print("13.2 MEASURES: Central, Spread, Shape")
print("="*60)

print(f"  Mean {statistics.mean(data):.2f}, Median {statistics.median(data):.2f}, Mode {statistics.mode(data)}")
print(f"  Range {max(data)-min(data)}, Quartiles Q1 {np.percentile(data,25) if HAS_NP else 'need numpy'}, Median, Q3")
if HAS_NP:
    print(f"    Q1={np.percentile(data,25):.1f}, Q2={np.percentile(data,50):.1f}, Q3={np.percentile(data,75):.1f}, IQR={np.percentile(data,75)-np.percentile(data,25):.1f}")
print(f"  Variance {statistics.variance(data):.2f}, StdDev {statistics.stdev(data):.2f}, PopStd {statistics.pstdev(data):.2f}")
print(f"  Mean deviation={(sum(abs(x-statistics.mean(data)) for x in data)/len(data)):.2f}")
# Weighted mean (mathsisfun)
vals=[90,80,70]; weights=[0.5,0.3,0.2]
wmean=sum(v*w for v,w in zip(vals,weights))/sum(weights)
print(f"\n  Weighted mean {vals} weights {weights} = {wmean:.1f}")
# Geometric & harmonic
def gmean(data): return math.exp(sum(math.log(x) for x in data)/len(data))
def hmean(data): return len(data)/sum(1/x for x in data)
print(f"  Geometric mean of {data[:4]}={gmean(data[:4]):.2f}, Harmonic={hmean(data[:4]):.2f}, Arth={statistics.mean(data[:4]):.2f} (AM>=GM>=HM)")

print("\nSkewness idea: tail direction")
print("  Symmetric: mean~median, Positive skew: mean>median (tail right)")

print("\n" + "="*60)
print("13.3 PROBABILITY FOUNDATIONS")
print("="*60)

# Basic: complement, independent, conditional, Bayes (already in 04, deeper)
print(f"Complement: P(not A)=1-P(A). Dice not 6 = {1-1/6:.4f}")
# Tree diagrams concept
print(f"Tree: two coins: P(HH)=0.25, P(at least one H)=0.75")
# Conditional
print(f"\nConditional: P(A|B)=P(A cap B)/P(B)")
print(f"  Cards: P(ace|red)=2/26={2/26:.4f}, P(red|ace)=2/4={2/4:.2f}")
# Bayes full
def bayes(p_b_given_a, p_a, p_b): return p_b_given_a*p_a/p_b
p_disease=0.01; p_pos_given_disease=0.95; p_pos_given_healthy=0.05
p_pos=p_pos_given_disease*p_disease + p_pos_given_healthy*(1-p_disease)
print(f"  Bayes disease example P(disease|pos)={bayes(p_pos_given_disease,p_disease,p_pos):.4f} (from 04)")

# Mutually exclusive vs independent
print(f"\nMutually exclusive (cannot both happen): P(A or B)=P(A)+P(B). e.g., dice 1 or 2 =1/6+1/6=1/3")
print(f"Independent (one doesn't affect other): P(A and B)=P(A)P(B). Two dice both 6=1/36")

print("\n" + "="*60)
print("13.4 DISTRIBUTIONS - Binomial, Normal, Chi-Square etc.")
print("="*60)

def binom_pmf(k,n,p): return math.comb(n,k)*p**k*(1-p)**(n-k)
print(f"Binomial n=10 p=0.5: P(3)={binom_pmf(3,10,0.5):.4f}, P(5)={binom_pmf(5,10,0.5):.4f}")
# Normal PDF
def normal_pdf(x, mu=0, sigma=1): return 1/(sigma*math.sqrt(2*math.pi))*math.exp(-0.5*((x-mu)/sigma)**2)
print(f"\nNormal(0,1) pdf at 0={normal_pdf(0):.4f}, at 1={normal_pdf(1):.4f}, at 2={normal_pdf(2):.4f}")
print(f"  68% within 1 sigma, 95% within 2, 99.7% within 3 (mathsisfun)")
# CDF via erf
def normal_cdf(x, mu=0, sigma=1): return 0.5*(1+math.erf((x-mu)/(sigma*math.sqrt(2))))
print(f"  CDF P(-1<Z<1)={normal_cdf(1)-normal_cdf(-1):.4f}, P(-2<Z<2)={normal_cdf(2)-normal_cdf(-2):.4f}")

# Binomial approx to normal when n large (De Moivre)
n,p=100,0.5
mu=n*p; sigma=math.sqrt(n*p*(1-p))
k=55
binom=sum(binom_pmf(i,n,p) for i in range(k, n+1))
normal_approx=1-normal_cdf(k-0.5,mu,sigma) # continuity correction
print(f"\nBinomial n100 P>=55 = {binom:.4f}, Normal approx {normal_approx:.4f}")

# Expected value, variance of random variable (mathsisfun random-variables-mean-variance)
print(f"\nRandom Variable X dice: E={sum(x*1/6 for x in range(1,7)):.2f}, Var={sum((x-3.5)**2*1/6 for x in range(1,7)):.2f}")
print(f"  Continuous: E = integral x f(x) dx, Var = E[X^2]-E[X]^2")

# Chi-square preview
print(f"\nChi-square: sum of squared normals, used for goodness-of-fit")
print(f"  Test: dice fair? observed vs expected")

# Outliers & correlation already in 04
print(f"\nCorrelation r: -1 to 1. Already in 04.")
# Central limit already demo

print("\n" + "="*60)
print("13.5 REGRESSION & FITTING (mathsisfun least-squares-regression)")
print("="*60)

# Least squares: y = a x + b, minimize sum (y - (a x+b))^2
def linear_regression(xs, ys):
    n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
    # slope a = sum (x-mx)(y-my)/ sum (x-mx)^2
    num=sum((x-mx)*(y-my) for x,y in zip(xs,ys))
    den=sum((x-mx)**2 for x in xs)
    a=num/den if den else 0
    b=my-a*mx
    # correlation & r^2
    ss_tot=sum((y-my)**2 for y in ys)
    ss_res=sum((y-(a*x+b))**2 for x,y in zip(xs,ys))
    r2=1-ss_res/ss_tot if ss_tot else 0
    return a,b,r2

xs=[1,2,3,4,5]; ys=[2.1,3.9,6.2,7.8,10.1]  # roughly y=2x
a,b,r2=linear_regression(xs,ys)
print(f"Data x={xs}, y={ys}")
print(f"  Fit y={a:.3f} x +{b:.3f}, R^2={r2:.4f} (1 is perfect)")
# Predict
print(f"  Predict x=6 => y={a*6+b:.2f}")

# Residuals
resids=[y-(a*x+b) for x,y in zip(xs,ys)]
print(f"  Residuals {[f'{r:.2f}' for r in resids]}, should be small random")

# Curve fitting: exponential via log transform
print(f"\nCurve fitting: if y = a e^{{bx}}, take ln y = ln a + b x then linear")

print("\n" + "="*60)
print("13.6 TESTING: Bayes, Confidence, t-test, Chi-square")
print("="*60)

# Confidence interval for mean: mean +/- z* sigma/sqrt(n)
def confidence_interval(data, confidence=0.95):
    m=statistics.mean(data)
    s=statistics.stdev(data) if len(data)>1 else 0
    # z for 95% approx 1.96
    z={0.90:1.645,0.95:1.96,0.99:2.576}[confidence]
    se=s/math.sqrt(len(data))
    return m - z*se, m+z*se

sample=[random.gauss(100,15) for _ in range(30)]
lo,hi=confidence_interval(sample,0.95)
print(f"Sample n30 mean {statistics.mean(sample):.1f} => 95% CI ({lo:.1f}, {hi:.1f}) (should contain true 100?) {lo<100<hi}")

# False positives (already in 13)
print(f"\nFalse positives: test 99% accurate, disease 1% => P(disease|pos) only ~50% (Bayes)")

# t-test idea
print(f"\nStudent's t-test: compare two means accounting for sample size (Wolfram)")
print(f"  t = (mean1-mean2)/ sqrt(s1^2/n1 + s2^2/n2) , df approximated")
g1=[random.gauss(100,10) for _ in range(20)]
g2=[random.gauss(110,10) for _ in range(20)]
def t_stat(a,b):
    m1,m2=statistics.mean(a),statistics.mean(b)
    s1,s2=statistics.pvariance(a),statistics.pvariance(b)
    se=math.sqrt(s1/len(a)+s2/len(b))
    return (m1-m2)/se if se else 0
print(f"  Group1 mean {statistics.mean(g1):.1f}, group2 {statistics.mean(g2):.1f}, t={t_stat(g1,g2):.2f} (large negative => different)")

# Chi-square goodness
observed=[20,30,25,25] # 4 categories, expected 25 each if uniform
expected=[25]*4
chi=sum((o-e)**2/e for o,e in zip(observed,expected))
print(f"\nChi-square test: observed {observed} expected {expected} => chi={chi:.2f}, df=3. Compare to critical 7.81 (95%)")

if PLOT:
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        # Histogram
        plt.figure(figsize=(10,4))
        plt.subplot(1,2,1)
        plt.hist(data, bins=6, edgecolor='black')
        plt.title("Histogram"); plt.grid(True, alpha=0.3)
        # Normal PDF
        plt.subplot(1,2,2)
        xs=np.linspace(-4,4,200); ys=[normal_pdf(x) for x in xs]
        plt.plot(xs,ys); plt.fill_between(xs,ys, alpha=0.2); plt.title("Standard Normal"); plt.grid(True)
        plt.tight_layout(); plt.show()

        # Scatter + regression
        plt.figure()
        plt.scatter(xs if 'xs' in locals() else [1,2,3,4,5], [2.1,3.9,6.2,7.8,10.1])
        reg_x=np.linspace(0,6,100)
        plt.plot(reg_x, a*reg_x+b, 'r-', label=f'y={a:.2f}x+{b:.2f} R2={r2:.2f}')
        plt.legend(); plt.grid(True); plt.title("Least Squares Regression"); plt.show()

        # Binomial vs Normal
        ks=list(range(0,21)); bms=[binom_pmf(k,20,0.5) for k in ks]
        plt.figure()
        plt.bar(ks,bms, alpha=0.5, label='Binomial n20')
        xs=np.linspace(0,20,200); ys=[normal_pdf(x,10, math.sqrt(5)) for x in xs]
        plt.plot(xs, ys*2, 'r--', label='Normal approx scaled')
        plt.legend(); plt.title("Binomial approx Normal"); plt.grid(True); plt.show()

        # Confidence intervals visualized
        means=[]; los=[]; his=[]
        for _ in range(20):
            s=[random.gauss(100,15) for _ in range(30)]
            lo,hi=confidence_interval(s)
            means.append(statistics.mean(s)); los.append(lo); his.append(hi)
        plt.figure()
        plt.errorbar(range(20), means, yerr=[np.array(means)-np.array(los), np.array(his)-np.array(means)], fmt='o', capsize=3)
        plt.axhline(100, color='red', linestyle='--', label='true 100')
        plt.title("20 95% CIs (expect 1 misses)"); plt.legend(); plt.grid(True); plt.show()
    except Exception as e:
        print(f"Plot error: {e}")
else:
    print("\n[Tip] --plot for histograms & regression: python 13_probability_statistics_complete.py --plot")

print("\nChallenge: implement Naive Bayes classifier, or bootstrap confidence intervals!")
