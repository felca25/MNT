import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors 

def f(x):
    return 2. * np.cosh(x / 4) - x

def secant(x_0, x_1, atol, f):
    x_old = x_0
    x = x_1
    k = 1
    dif = 2. * atol
    x_values = [x]
     
    while dif >= atol:
        x_new = x - f(x) * (x - x_old) / (f(x) - f(x_old))
        dif = np.abs(x_new - x)
        x_old, x = x, x_new
        x_values.append(x)
        print(f'Iter: {k}, x = {x}')
        k += 1
        
    return x_values
        
root_1 = secant(0, 1, 1e-8, f)
root_2 = secant(10, 11, 1e-8, f)

print(root_1)
print(root_2)                                                                           