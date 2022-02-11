from matplotlib import pyplot as plt
import numpy as np
'''Definindo condições de contorno'''
t_o = 0.
t_final = 1.
y_o = 1.
dt =0.1

'''Definindo as arrays de tempo, y'''
t = np.arange(t_o, t_final + dt, dt)
y = np.zeros(len(t))
y[0] = y_o

''''definindo a função exata'''
y_bar = lambda t : np.exp(-t)

'''iteração para determinar os valores de y'''
def explicit_euler(t, y,y_bar, dt= 0.1):
    
    erro =np.zeros(len(t))
    
    for k in range(len(t) - 1):
        # iteração para y_k+1 = (1 - dt) * y_k
        y[k + 1] = (1. - dt) * y[k]
        # calculo do erro de truncamento erro = |y - y_bar|
        erro[k] = np.abs(y[k] - y_bar(t)[k])

        print(f'Tempo = {t[k+1]:.2f}, y = {y[k+1]:.5f}')
        print(f'Erro = {erro}')
    
    return [y, y_bar, erro]

def implicit_euler(t, y, y_bar, dt= 0.1):
    
    erro =np.zeros(len(t))
    
    for k in range(len(t) - 1):
        # iteração para y_k+1 = (1 - dt) * y_k
        y[k + 1] =  y[k] / (1. + dt)
        # calculo do erro de truncamento erro = |y - y_bar|
        erro[k] = np.abs(y[k] - y_bar(t)[k])

        print(f'Tempo = {t[k+1]:.2f}, y = {y[k+1]:.5f}')
        print(f'Erro = {erro}')
    
    return [y, y_bar, erro]

def plot_euler(t, y, y_bar, erro):
    fig1 = plt.figure()
    plt.plot(t, y, 'bo')
    plt.plot(t, y_bar(t), '--r')
    fig2 = plt.figure()
    plt.plot(t, erro, 'bo')
    
def plot_compare_euler(t, y_exp, y_imp, y_bar, erro_exp, erro_imp):
    fig1 = plt.figure()
    plt.plot(t, y_exp, 'bo')
    plt.plot(t, y_imp, 'rx')
    plt.plot(t, y_bar, '--b')
    fig2 = plt.figure()
    plt.plot(t, erro_exp, 'bo')
    plt.plot(t, erro_imp, 'rx')
y, y_bar, erro = explicit_euler(t, y, y_bar, dt)

y_imp, y_bar_imp, erro_imp = implicit_euler(t, y, y_bar, dt)

plot_compare_euler(t, y, y_imp, y_bar(t), erro, erro_imp)

plt.show()