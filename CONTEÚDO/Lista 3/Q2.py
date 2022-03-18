import numpy  as np
from numpy import pi as PI
from matplotlib import pyplot as plt

def Temp_analitic(x, t):
    result = 0
    
    for i in range(10000):
        result += (4 / (((2 * i) - 1) * PI)) * np.sin(((2 * i) - 1) * PI * x) * np.exp(-(((2 * i) - 1) ** 2) * (PI ** 2) * t)
    
    return result

def apply_init_fin_dif(n, dx, corners, Temp_init_func):
    length = n * dx
    Temp = np.zeros(n + 1, float)
    x_arr = np.arange(0., length + dx, dx)

    Temp = Temp_init_func(Temp)
    Temp[0] = corners[0]; Temp[-1] = corners[-1]

    return [x_arr, Temp]

def fin_diff_method(n, dx, t_arr, Temp, println= False):
    t, t_final, dt = t_arr
    result = []
    result_points = np.linspace(0, t_final, 4)
    k = 0
    Temp_new = np.copy(Temp)
    conv_condition = (dx ** 2) / 4.
    
    if dt <= conv_condition:
        while t < t_final - .01 * dt:
            for i in range(1, n):
                Temp_new[i] = Temp[i] + (dt / (dx ** 2)) * (Temp[i + 1] - 2 * Temp[i] + Temp[i-1])
                
                if println:
                    print(f'Tempo {t:.2f}')
                    print(f'Temp no tempo {t:.2f} = {Temp}') 
            
            Temp = np.copy(Temp_new)
            
            if t in result_points:
                result.append(Temp)
                
            k += 1
            t = k * dt
    return result

def plotter(x_arr, results):
    
    plt.figure()
    for i in range(len(results) - 1):
        plt.plot(x_arr, results[i], 'ko')
    plt.plot(x_arr, results[-1])
    plt.show()
        
def main():
    dx = .01
    dt = .00001
    length = 1.

    t = 0.
    t_final = .5
    t_arr = [t, t_final, dt]

    n = int(length / dx)

    T_o = T_len = 0.
    corners = [T_o, T_len]

    Temp_init_func = lambda x : x + 1

    x_arr, Temp = apply_init_fin_dif(n, dx, corners, Temp_init_func)
    results = fin_diff_method(n, dx, t_arr, Temp)
    results.append(Temp_analitic(x_arr, t_final))
    plotter(x_arr, results)
    
if __name__ == '__main__':
    main()