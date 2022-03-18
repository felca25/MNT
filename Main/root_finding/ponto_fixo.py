import numpy as np
from matplotlib import pyplot as plt

def g(x):
    return 2 * np.cosh(x/4) 

def g_lin(x):
    return 1/2 * np.sinh(x/4)

def fixed_point(x, atol, g):
    k = 0
    dif = 2. * atol

    while dif >= atol:
        x_new = g(x)
        dif = np.abs(x_new - x)
        x = x_new
        k += 1
        # print(f'Iteração k = {k}, o valor de x é {x}')
        
    print(f'Iterações:{k}')
    print(f'Raiz de f(x): {x:.6f}')
    return x

def plot_fixed_point(interval: list, x, g):
    
    x_values = np.linspace(interval[0], interval[1], interval[2])
    
    funcao_g = g(x_values)
    funcao_f = g(x_values) - x_values
    zero = 0.0 * x_values

    plt.figure()
    plt.plot(x_values,x_values)
    plt.plot(x_values, funcao_g)
    plt.scatter(x= x, y= x)
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.show()
    plt.plot(x_values, zero)
    plt.plot(x_values, funcao_f)
    plt.scatter(x= x, y = 0.)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    
def main():
    
    x = 1. #chute inicial
    atol = 1.e-8

    x = fixed_point(x, atol, g)
    x_2 = fixed_point(3., atol, g_lin)

    plot_fixed_point([-10., 10., 100], x, g)
    plot_fixed_point([-10., 10., 100], x_2, g_lin)
    
if __name__ == '__main__':
    main()