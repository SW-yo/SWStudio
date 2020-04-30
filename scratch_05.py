import random
import math
import matplotlib.pyplot as plt
from collections import Counter

def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older ==  "girl" or younger == "girl":
        either_girl += 1

#print("P(2人とも女の子|1人目が女の子)：", both_girls / older_girl)
#print("P(2人とも女の子|どちらか1人が女の子)", both_girls / either_girl)


def uniform_pdf(x):
    return 1 if x >= o and x < 1 else 0

def uniform_cdf(x):
    "returns the prbability that a uniform random variable is <= x"
    if x < 0 : return 0
    elif x < 1 : return x
    else : return 1


def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu) ** 2 / 2/ sigma ** 2) / (sqrt_two_pi * sigma))
"""
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()
"""

def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2
"""
xs = [x / 10.0 for x in range(-50 , 50)]
plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.legend(loc=4)
plt.title("Various Normal cdfs")
plt.show()
"""

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    "二分探索を用いて逆関数の近似値を計算する"

    #標準正規分布でない場合、標準正規分布からの差分を求める
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0     #normal_cdf(-10)は0(に近い値)である
    hi_z, hi_p = 10.0, 1        #normal_cdf(10)は1(に近い値)である
    while hi_z - loz > tolerance:
        mid_z = (low_z + hi_z) / 2  #中央の値および
        mid_p = normal_cdf(mid_z)   #その地点でのcdfの値
        if mid_p < p:
            #中央地はまだ小さいので、さらに上を使う
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            #中央値はまだ大きいので、さらに下を使う
            hi_z, hi_p = mid_z, mid_p
        else:
            break

    return mid_z


def bernoulli_trial(p):
    return 1 if random.random() < p else 0


def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))


def make_hist(p, n, num_points):

    data = [binomial(n, p) for _ in range(num_points)]

    #二項分布を棒グラフでプロットする
    histgram = Counter(data)
    plt.bar([x - 0.4 for x in histgram.keys()],
        [v / num_points for v in histgram.values()],
        0.8,
        color='0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1- p))

    #正規分布の近似を折線グラフでプロットする
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i -0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.title("binomial Distribution vs Normal Approximation")
    plt.show()

make_hist(0.75, 100, 10000)
