"""
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

g = doubler(f1)

print(g(3))
print(g(-1))
"""

def f2(x, y):
    return x + y

"""
g = doubler(f2)
#print(g(1, 2))
"""
"""
def magic(*args, **kwargs):
    print("引数なし:", args)
    print("キーワード引数：", kwargs)

magic(1, 2, key="word", key2="word2")


def other_way_magic(x, y, z):
    return x + y + z
x_y_list = [1, 2]
z_dict = {"z" : 3}
print(other_way_magic(*x_y_list, **z_dict))
"""

def doubler_correct(f):
    """fがどのような引数構成であってもうまく働く"""
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print(g(1, 2))
