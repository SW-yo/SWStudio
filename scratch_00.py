import math

def scalar_multiply(c, v):
    #cは数値、vはベクトル
    return [c * v_i for v_i in v]

def vector_subtract(v, w):
    #対応する要素の差
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def dot(v, w):
    #v_i * w_i + ... + v_n * w_n
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    #v_1 * v_1 + ... + v_n * v_n
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v)) #math.sqrtは平方根を求める

def squared_distance(v, w):
    #(v_i - w_i) ** 2 + ... + (v_n - w_n) ** 2
    return sum_of_squares(vector_subtract(v, w))
"""
def distance(v, w):
    return math.sqrt(squared_distance(v, w))
"""

def distance(v, w):
    return magnitude(vector_subtract(v, w))
