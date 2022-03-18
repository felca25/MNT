import numpy as np 
from matplotlib import pyplot as plt

def bissec_c(a, b, tol, f):
    k_max = np.log((b - a) / (2 * tol))
    k = 0
    
    diff = np.abs(a - b)
    
    a_n = a
    b_n = b
    c_n = 0
    
    while k <= k_max + 1:
        print(f'Iter: k = {k} ------------')
        print(f'valor de c_n = {c_n}')
        print(f'valor de f(c_n) = {f(c_n)}')
        
        c_n = .5 * (b_n + a_n)
        
        if f(c_n) * f(a_n) < 0:
            b_n = c_n
            
        elif f(c_n) * f(a_n) > 0:
            a_n = c_n
        
        k += 1
        
    x = .5 * (b_n + a_n)
    diff = np.abs(a_n - b_n)

    print(f'------------ Result ------------')
    print(f'x* = {x}')
    print(f'diff = {diff}')
    
    return x
    
def plot_bissec(a, b, f):
    x = np.linspace(a, b, 100)
    y = f(x)
    zeros = 0.* x
    
    plt.figure()
    plt.plot(x, y)
    plt.plot(x, zeros, color='grey')
    plt.show()
    
    
def main():
    a, b, tol = 0., 10., 1.e-8

    def f(x):
        return 2 * np.cosh(x / 4) - x

    a = bissec_c(a, b, tol, f) + 1
    
    bissec_c(a, b, tol, f)
    plot_bissec(-10., 10, f)

if __name__ == '__main__':
    main()
