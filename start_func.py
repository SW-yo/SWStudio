import my_module
import importlib
importlib.reload(my_module)
n = my_module.func(5)
print(n)