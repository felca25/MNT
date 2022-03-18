import numpy as np
from numpy import pi as PI
from matplotlib import pyplot as plt


def Temp_analitic_func(x, t):
    result = 0
    
    for i in range(1000000):
        result += ((4 / (((2 * i) - 1) * PI)) 
        * np.sin(((2 * i) - 1) * PI * x)
        * np.exp(-(((2 * i) - 1) ** 2) * (PI ** 2) * t))
    
    return result

Temp_init_func = lambda x : x + 1

dx = 0.05
dt = 0.0001
length = 1.
t_final = .5

println = False

n = int(length / dx)
nt = int(t_final / dt)
result_points = np.trunc(np.linspace(dt, nt, 4))
time = []

T_o = T_length = 0.
T_boundary = [(0, 0.), (-1, 0.)]

Temp = np.zeros(n + 1, float)
x_arr = np.arange(0., length + dx, dx)
Temp_by_time = []

Temp = Temp_init_func(Temp)
Temp[0] = Temp[-1] = 0.

print(result_points)
print(Temp_by_time)

t = 0.
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
        
        if k == 0:
            time.append(f't = {t:.4f}')
            Temp_by_time.append(Temp)
        
        if k in result_points[1:]:
            time.append(f't = {t:.4f}')
            Temp_by_time.append(Temp)
            
        k += 1
        t = k * dt
    Temp_by_time.append(Temp)
    Temp_by_time.append(Temp_analitic_func(x_arr, t_final))
    time.append(f't = {t:.4f}')
    time.append(f'solução analítica em t = {t:.4f}')

print(time)

plt.figure()
plt.title('Método de diferenças finitas aplicadas \npara as condições de contorno do exercício 2')
for i in range(4):
    plt.plot(x_arr, Temp_by_time[i], 'o')
plt.plot(x_arr, Temp_by_time[-1])
plt.legend(time)
plt.show(