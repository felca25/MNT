import numpy as np
from matplotlib import pyplot as plt

def func(x):
    return 2. * np.cosh(x / 4) - x
def d_func(x):
    return .5 * np.sinh(x / 4) - 1.

def newton_method(x_0, atol, func, d_func):
    x_values = []
    x = x_0
    k = 0
    dif = 2. * atol
    
    while dif >= atol:
        x_new = x - func(x) / d_func(x)
        dif = np.abs(x_new - x)
        x = x_new
        k += 1
        
        print(f'Iter: {k}, x = {x}')
        x_values.append(x)
        
    return x_values
if __name__ == '__main__':
    newton_method(8., 1e-8, func, d_func)