import numpy as np
from matplotlib import pyplot as plt



analitical = lambda x, t : np.exp((-(np.pi ** 2) * t) / 4) * np.sin(((np.pi * x) / 2))
Initial_func = lambda x : np.sin((np.pi / 2) * x_arr) 

# -------------------
# INICIALIZANDO O PROBLEMA
# -------------------


dx = .1 # passo de espaço entre os pontos
dt = .0001
length = 2. # comprimento da barra 
 # passo de tempo

N = 20 # número de pontos do domínio
t = 0.
t_final = .5

T_o = T_length = 0.
# -------------------
# DEFINIÇÃO DOS VETORES E APLICANDO AS CONDIÇÕES DE CONTORNO
# -------------------
Temp = np.zeros(N + 1, float) # vetor de temperaturas discretas 
x_arr = np.arange(0., length + dx, dx) # vetor de posições discretas

Temp = Initial_func(x_arr)
Temp[0] = T_o; Temp[-1] = T_length

Temp_new = np.copy(Temp) # vetor utilizado para manipulações
Temp_analitic = analitical(x_arr, t_final)
# -------------------
# APLICANDO O MÉTODO DAS DIFERNÇAS FINITAS PARA A RESOLUÇÃO
# -------------------
k = 0
conv_condition = (dx ** 2) / 4.
if dt <= conv_condition:
    while t < t_final - .01 * dt:
        for i in range(1, N):
            Temp_new[i] = Temp[i] + (dt / (dx ** 2)) * (Temp[i + 1] - 2 * Temp[i] + Temp[i-1])
        
        Temp = np.copy(Temp_new)
        k += 1
        t = k * dt
    # print(f'Tempo {t:.2f}')
    # print(f'Temp no tempo {t:.2f} = {Temp}')
# -------------------
# PLOTANDO O GRÁFICO
# -------------------
plt.figure()
plt.title(f'Temperatura para $t = {t:.3f}$, $\Delta t = {dt:.3f}$')
plt.plot(x_arr, Temp, 'ko')
plt.plot(x_arr, Temp_analitic, 'k')
plt.show()