import numpy as np
from numpy import pi as PI
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


def finite_diff_unidimensional(Temp, time, dx, dt):
    n = int(len(Temp) - 1)
    t = 0.
    time_len = len(time)
    Temp_new = np.copy(Temp)
    result = np.zeros([time_len, n + 1])
    
    if dt <= (dx ** 2) / 4.:
        while t < time[-1] - .1 * dt:
            for i in range(0, n):
                x_axis = (dt / (dx ** 2)) * (Temp[i + 1] - 2 * Temp[i] + Temp[i - 1])
                Temp_new[i] = Temp[i] + x_axis
            
                for i in range(time_len):
                    # print([time[i] - dt, t, time[i] + dt])
                    # print(t < time[i] + dt  and t > time[i] - dt)
                    if t < time[i] + dt  and t > time[i] - dt:
                        result[i] = np.copy(Temp_new)


            Temp = np.copy(Temp_new)
            t += dt
    
        return result
    else:
        print('something went wrong')

def finite_diff_bidimensional(Temp, time, dx, dy, dt):
    n = len(Temp) - 1
    m = len(Temp[0]) - 1
    time_len = len(time)
    t = 0.
    Temp_new = np.copy(Temp)
    result = np.zeros([time_len, n + 1, m + 1])
        
    
    if dt <= (dx ** 2) / 4.  and dt <= (dy ** 2) / 4.:
        while t < time[-1] - 0.1 * dt:
            # print(f'Time = {t:.3f}')
            for i in range(1, n):
                for j in range(1, m):
                    x_axis = (dt / (dx ** 2)) * (Temp[i + 1][j] - 2 * Temp[i][j] + Temp[i - 1][j])
                    y_axis = (dt / (dx ** 2)) * (Temp[i][j + 1] - 2 * Temp[i][j] + Temp[i][j - 1])
                    Temp_new[i][j] = Temp[i][j] + x_axis + y_axis
                    
            for i in range(time_len):
                # print([time[i] - dt, t, time[i] + dt])
                # print(t < time[i] + dt  and t > time[i] - dt)
                if t < time[i] + dt  and t > time[i] - dt:
                    result[i] = np.copy(Temp_new[::-1])
                    # print(result[i])
                
            Temp = np.copy(Temp_new)
            t += dt
        
        return result
    


def plot_cmap(leg, result):
    '''Helper function to plot temperature color maps based on specific points in time'''
    # Creating a Blue to Orange color map 
    top = cm.get_cmap('Blues', 128)
    bottom = cm.get_cmap('Oranges_r', 128)
    new_colors = np.vstack((top(np.linspace(1, 0, 128)), bottom(np.linspace(1, 0, 128))))
    newcmp = ListedColormap(new_colors, name='BlueOrange')
    colormaps = [newcmp]
    
    cmap_len = len(colormaps)

    # Plotting colormap
    for i in range(len(result)):
        fig, axs = plt.subplots(1, cmap_len, figsize= (cmap_len * 2 + 2, 3), constrained_layout= True, squeeze= False)
        plt.title(leg[i])
        for [ax, cmap] in zip(axs.flat, colormaps):
            psm = ax.pcolormesh(result[i], cmap= cmap, rasterized= True, vmin= 0, vmax= 1)
            fig.colorbar(psm, ax= ax)
            
def plot_uni(x_arr, result, an_result, title= 'Title', legend= None ):
    fig = plt.figure()
    plt.title(title)
    for i in range(len(result)):
        plt.plot(x_arr, result[i], 'o')
    for i in range(len(an_result)):
        plt.plot(x_arr, an_result[i], '-')

    plt.legend(legend)

def main_1():
    dx = .07
    dt = .001

    time = [0., .005, .5, 5.]

    x_arr = np.arange(0., 2., dx)

    n = len(x_arr)

    Temp = np.zeros(n, float)
    Temp_init_func = lambda x : np.sin((PI / 2) * x)

    Temp = Temp_init_func(x_arr)
    Temp[0] = Temp[-1] = 0.

    print(Temp)

    result = finite_diff_unidimensional(Temp, time, dx, dt)
    
    analitic_result = np.zeros([len(time), n])
    Temp_analitic = np.copy(Temp)
    Temp_analitic_func = lambda x, t : (np.exp((-(PI ** 2) * t) / 4) * 
                                        np.sin(0.5 * PI * x))
    for i in range(len(time)):
        for j in range(n):
            analitic_result[i][j] = Temp_analitic_func(x_arr[j], time[i])
    
    title = 'Unidimensional Temperature Distribuition'
    leg = []
    for i in range(len(time)):
        leg.append(f't = {time[i]:.4f}')
        
    for i in range(len(analitic_result)):
        leg.append(f'Analitical Solution')
        
    plot_uni(x_arr, result, analitic_result, title, leg)
    plt.show()
    
def main_6():
    dx = dy = .07
    dt = .001

    time = [0., 0.005, 0.5, 5.]

    x_arr = np.arange(0., 1., dx)
    y_arr = np.arange(0., 1., dy)

    n = len(x_arr)
    m = len(y_arr)

    Temp = np.zeros([m, n], float)
    Temp_init_func = lambda x : np.sin(PI * x)

    for i in range(m):
        Temp[-1][i] = Temp_init_func(x_arr[i])
        Temp[i][0] = 0. 
        Temp[i][-1] = 0. 
    Temp = Temp[::-1]

    result = finite_diff_bidimensional(Temp, time, dx, dy, dt)

    Temp_exact = np.copy(Temp)
    Temp_exact_func = lambda x, y : ((np.sinh(PI * y) * np.sin(PI * x)) / np.sinh(PI))

    for i in range(n):
        for j in range(m - 1):
            Temp_exact[i][j] = Temp_exact_func(x_arr[j], y_arr[i])
            
    exact_title = [f'Exact Solution for Temperature distribuition for permanent regime']

    leg = []
    for i in range(len(time)):
        leg.append(f'Temperature distribuition at time = {time[i]:.4f}\n')

    plot_cmap(leg, result)
    plot_cmap(exact_title, [Temp_exact])
    plt.show()

if __name__ == '__main__':
    main_1()