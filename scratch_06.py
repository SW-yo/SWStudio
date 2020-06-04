import math
import random
import matplotlib.pyplot as plt
import scratch_05 as sc5

def normal_approximation_to_binomal(n, p):
    "Binomal(n, p)に相当するμとσを計算する"
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

#変数が閾値を下回る確率はnormal_cdfで表せる
normal_probability_below = sc5.normal_cdf

#閾値を下回っていなければ閾値より上にある
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - sc5.normal_cdf(lo, mu, sigma)

#hiより小さくloより大きければ値はその間にある
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return sc5.normal_cdf(hi, mu, sigma) - sc5.normal_cdf(lo, mu, sigma)

#間になければ範囲外にある
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    "確率P(Z <= z)となるzを返す"
    return sc5.inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(prbability, mu=0, sigma=1):
    "確率P(Z >= z)となるzを返す"
    return sc5.inverse_normal_cdf(1 - prbability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    "指定された確率を包含する（平均値を中心に）対象な境界を返す"
    tial_probability = (1 - probability) / 2

    #上側の境界はテイル確率（tial_probability)分上に
    upper_bound = normal_lower_bound(tial_probability, mu, sigma)

    #下側の境界はテイル確率（tial_probability)分下に
    lower_bound = normal_upper_bound(tial_probability, mu, sigma)

    return lower_bound,upper_bound

mu_0, sigma_0 = normal_approximation_to_binomal(1000, 0.5)

#print(normal_two_sided_bounds(0.95, mu_0, sigma_0))

#pが0.5であると想定の元で95%の境界を確認する
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

#p=0.55であった場合のμとσを計算する
mu_1, sigma_1 = normal_approximation_to_binomal(1000, 0.55)

#第二種過誤とは帰無仮設を棄却しないという誤りがあり
#Xが当初想定の領域に入っている場合に生じる
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability
#print(power)

hi = normal_upper_bound(0.95, mu_0, sigma_0)
#print(hi)

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability
#print(power)


def  two_sided_p_value(x, mu=0, sigma=1):
    if x > mu:
        #xが平均より大きい場合、テイル確率はxより大きい分
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        #xが平均より小さい場合、テイル確率はより小さい分
        return 2 * normal_probability_below(x, mu, sigma)

#print(two_sided_p_value(529.5, mu_0, sigma_0))


extreme_value_count = 0
for _ in range(100000):
    num_heads = sum(1 if random.random() < 0.5 else 0   #1,000回のコイン投げを行い
    for _ in range(1000))                               #表が出る回数を数える。
    if num_heads >= 530 or num_heads <= 470:            #そのうち極端な回数はどれだけ
        extreme_value_count += 1                        #出方を数える。

#print(extreme_value_count / 100000)


#print(two_sided_p_value(531.5, mu_0, sigma_0))


upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

#print(upper_p_value(524.5, mu_0, sigma_0))
#print(upper_p_value(526.5, mu_0, sigma_0))

p_hat = 540 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) / 1000)

#print(normal_two_sided_bounds(0.95, mu, sigma))


def run_experiment():
    #歪みのないコインを1000回投げて、表が出たらTrue、裏はFalseとする
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):
    #5%の有意水準を用いる
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531

random.seed(0)

experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment
                    for experiment in experiments
                    if reject_fairness(experiment)])

#print(num_rejections)

def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma

def a_b_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B **2)

z = a_b_statistic(1000, 200, 1000, 150)
#print(z)

#print(two_sided_p_value(z))


def B(alpha, beta):
    #確率の総和が1となるように定数で正規化する
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x, alpha, beta):
    if x <0 or x > 1:       #[0, 1]の区間外では重みは0となる
        return 0
    return x ** (alpha - 1) * (1 - x) **(beta - 1) / B(alpha, beta)


xs = [x / 100 for x in range(0, 100)]
"""
plt.plot(xs, [beta_pdf(x, alpha=1, beta=1) for x in xs], '-', label='Beta(1,1)')
plt.plot(xs, [beta_pdf(x, alpha=10, beta=10) for x in xs], '-.', label='Beta(10,10)')
plt.plot(xs, [beta_pdf(x, alpha=4, beta=16) for x in xs], ':', label='Beta(4,16)')
plt.plot(xs, [beta_pdf(x, alpha=16, beta=4) for x in xs], '--', label='Beta(16,4)')
plt.legend(loc='upper center')
"""

plt.plot(xs, [beta_pdf(x, alpha=4, beta=8) for x in xs], '-', label='Beta(1,1)')
plt.plot(xs, [beta_pdf(x, alpha=23, beta=27) for x in xs], '-.', label='Beta(10,10)')
plt.plot(xs, [beta_pdf(x, alpha=33, beta=17) for x in xs], ':', label='Beta(4,16)')
plt.legend(loc='upper left')

plt.show()
