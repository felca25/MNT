import numpy as np
from matplotlib import pyplot as plt
import math

class ODE:
    def __init__ (self, y_prime, t_arr, y_o, methods_used, analitical=None, implicit=None):
        '''
        A classe contém soluções numericas para edo's dada uma edo y_prime e um intervalo de tempo t_arr
        
        Parameters
        ----------
        y_prime: function
            isolar y_prime na edo e definir uma função(t,y) para ser resolvida
        
        t_arr: list
            t_arr = [t_inicial, t_final, step]
        
        '''
        self.methods = methods_used
        self.y_prime = y_prime
        
        self.t_initial = t_arr[0]
        self.t_final = t_arr[1]
        self.t_step = t_arr[2]
        
        self.y_o = y_o
        
        self.y_bar = analitical
        self.implicit = implicit
        
        self.t = np.arange(self.t_initial, self.t_final, self.t_step)
        self.y = np.zeros(len(self.t))
        self.y[0] = self.y_o
        
        self.errors = []
        
        self.results = []
        
    def reset(self):
        self.y = np.zeros(len(self.t))
        
        
    def euler_explicit(self):
        
        erro =np.zeros(len(self.t))
    
        for n in range(len(self.t) - 1):

            self.y[n + 1] = self.y[n] + (self.t_step * self.y_prime(self.t[n], self.y[n]))
            # calculo do erro de truncamento erro = |y - y_bar|
            erro[n] = np.abs(self.y[n] - self.y_bar(self.t)[n])

            print(f'Tempo = {self.t[n+1]:.2f}, y = {self.y[n+1]:.5f}')
            print(f'Erro = {erro}')
            
        self.results.append(self.y)
        self.errors.append(erro)
        self.reset()
        
    def euler_implicit(self):
        
        erro =np.zeros(len(self.t))
    
        for n in range(len(self.t) - 1):

            self.y[n + 1] = self.implicit(self.t[n], self.y[n])
            # calculo do erro de truncamento erro = |y - y_bar|
            erro[n] = np.abs(self.y[n] - self.y_bar(self.t)[n])

            print(f'Tempo = {self.t[n+1]:.2f}, y = {self.y[n+1]:.5f}')
            print(f'Erro = {erro}')
            
        self.results.append(self.y)
        self.errors.append(erro)
        self.reset()
    
    def runge_kutta_2(self):
        
        erro =np.zeros(len(self.t))
    
        for n in range(len(self.t) - 1):

            k1 = self.t_step * self.y_prime(self.t[n], self.y[n])
            k2 = self.t_step * self.y_prime(self.t[n + 1], (self.y[n] + k1))
            self.y[n + 1] = self.y[n] + 0.5 * (k1 + k2)
            # calculo do erro de truncamento erro = |y - y_bar|
            erro[n] = np.abs(self.y[n] - self.y_bar(self.t)[n])

            print(f'Tempo = {self.t[n+1]:.2f}, y = {self.y[n+1]:.5f}')
            print(f'Erro = {erro}')
            
        self.results.append(self.y)
        self.errors.append(erro)
        self.reset()
        
    def runge_kutta_4(self):
        
        erro =np.zeros(len(self.t))
    
        for n in range(len(self.t) - 1):

            k1 = self.t_step * self.y_prime(self.t[n], self.y[n])
            k2 = self.t_step * self.y_prime((self.t[n] + (0.5 * self.t_step)), (self.y[n] + (0.5 * k1)))
            k3 = self.t_step * self.y_prime((self.t[n] + (0.5 * self.t_step)), (self.y[n] + (0.5 * k2)))
            k4 = self.t_step * self.y_prime(self.t[n + 1], (self.y[n] + k3))
            self.y[n + 1] = self.y[n] + (1 / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
            # calculo do erro de truncamento erro = |y - y_bar|
            erro[n] = np.abs(self.y[n] - self.y_bar(self.t)[n])

            print(f'Tempo = {self.t[n+1]:.2f}, y = {self.y[n+1]:.5f}')
            print(f'Erro = {erro}')
            
        self.results.append(self.y)
        self.errors.append(erro)
        self.reset()
        
    def analitical(self):
        y_values = np.zeros(len(self.t))
        
        for time in self.t:
            y_values.append(self.y_bar(time))
            
        self.results.append(self.y)
        self.reset()
        
    def run(self):
        
        for method in self.methods:
            if method.lower() == 'euler explícito':
                self.explicit_euler()
                
            elif method.lower() == 'euler implícito':
                self.implicit_euler()
                
            elif method.lower() == 'runge kutta 2ª ordem':
                self.runge_kutta_2()
                
            elif method.lower() == 'runge kutta 4ª ordem':
                self.runge_kutta_4()
                
        pass      
        
    