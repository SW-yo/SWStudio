import matplotlib.pyplot as plt
import random, math
from functools import partial
from scratch_00 import distance

def sum_of_squares(v):
    #vの各要素の二乗を合計する
    return sum(v_i ** 2 for v_i in v)

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h

def square(x):
    return x * x

def derivative(x):
    return 2 * x

derivative_estimate = partial(difference_quotient, square, h=0.00001)


#図示する。基本的には両者は同じ値。
x = range(-10, 10)
plt.title("Actual Derivatives vs Estimates")
plt.plot(x, list(map(derivative, x)), 'rx', label='Actual')               #赤のx
plt.plot(x, list(map(derivative_estimate, x)), 'b+', label='Estimate')    #青の+
plt.legend(loc=9)
#plt.show()


def partial_differnce_quotient(f, v, i, h):
    #関数fと変数ベクトルvに対するi番目の差分商を計算する
    w = [v_j + (h if j == i else 0) #vのi番目の要素にhを加える
    for j, v_j, in enumerate(v)]

    return (f(w) - f(v)) / h

def estimate_gardient(f, v, h=0.00001):
    return [partial_differnce_quotient(f, v, i, h)
    for i, _ in enumerate(v)]


def step(v, direction, step_size):
    #vからdirection方向にstep_size移動する
    return [v_i + step_size * direction_i
    for v_i ,direction_i in zip(v, direction)]

def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]

#開始点を無作為に選択する
v = [random.randint(-10, 10) for i in range(3)]

tolerance = 0.0000001

while True:
    gradient = sum_of_squares_gradient(v)   #vにおける勾配を計算する
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v

#print(v)

step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

def safe(f):
    #fと等価であるが無効な入力に対する振る舞いとして
    #無限大を返すような新しい関数を返す
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')     #Pythonにおける無限大
    return safe_f

def minimize_batch(target, fn, gradient_fn, theta_0, tolerance=0.000001):
    #目的関数target_fnを最小化するthetaを勾配降下法を使って求める

    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

    theta = theta_0                 #thetaに初期値を設定
    target_fn = safe(target_fn)     #target_fnの安全版
    value = target_fn(theta)        #valueの値を最小化する

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size)
        for step_size in step_sizes]

        #誤差関数を最小化する値を選ぶ
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        #収束したなら終了する
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value

def negate(f):
    #あらゆる入力xに対する-f(x)に相当する関数を返す
    return lambda *args, **kwargs: -f(*args, **kwargs)

def negate_all(f):
    #fが数値リストを返す場合のnegate関数
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]

def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn), negate_all(gradient_fn), theta_0, tolerance)


def in_random_order(data):
    #データの要素を無作為な順序で使います
    indexes = [i for i, _ in enumerate(data)]       #インデックスのリストを作る
    random.shuffle(indexes)                         #無作為に並び替える
    for i in indexes:                               #データをその順番に返す
        yield data[i]

def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):

    data = xip(x, y)
    theta =theta_0                              #初期推定値
    alpha = alpha_0                             #初期ステップ量
    min_theta, min_value = None, float('inf')   #現時点での最小値
    iterations_with_no_improvement = 0

    #100回繰り返しても改善しなければストップする
    while iterations_with_no_improvement < 100:
        value = sum(target_fn(x_i, y_i) for x_i, y_i in data)

        if value < min_value:
            #新しい最小値が見つかれば、それを記憶して
            #最初のステップ量に戻す
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            #そこでなければ改善が見られないため
            #ステップ量を小さくする
            iterations_with_no_improvement += 1
            alpha *= 0.9

        #各データポイントに対して勾配ステップを適用する
        for x_i, y_I in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))

    return min_theta


def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_stochastic(negate(target_fn), negate_all(gradient_fn),
            x, y, theta_0,alpha_0)
