from functools import reduce

def vector_add(v, w):
    #対応する要素の和
    return [v_i + w_i for v_i, w_i in zip(v, w)]

x = [1, 2]
y = [2, 1]

z = vector_add(x, y)
print(z)

def vector_sum(vectors):
    return reduce(vector_add, vectors)

v = [x, y]
w = vector_sum(v)
print(w)

A =[[1, 2, 3],
[4, 5, 6]]

B = [[1, 2],
[3, 4],
[5, 6]]

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 #最初の行の要素数
    return num_rows, num_cols

print(shape(A))


def make_matrix(num_rows, num_cols, entry_fn):
    #num_rows ×　num_colsの行列を返す
    #(i, j)の要素はentry_fn(i, j)が与える
    return [[entry_fn(i, j)             #与えられたiからリスト
            for j in range(num_cols)]   #[entry_fn(i, 0), …]を作る
            for i in range(num_rows)]   #各iに対して、リストを作る

def is_diagonal(i, j):
    #対角要素は1、それ以外は0
    return 1 if i == j else 0

identity_matrix = make_matrix(5, 5, is_diagonal)
print(identity_matrix)
