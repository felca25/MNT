import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

PI = np.pi

def plot_cmap(leg, result):
    '''Helper function to plot temperature color maps based on specific points in time'''
    
    # Creating a Blue to Orange color map 
    
    top = cm.get_cmap('Blues', 128)
    bottom = cm.get_cmap('YlOrRd', 128)
    new_colors = np.vstack((top(np.linspace(1, 0, 128)), bottom(np.linspace(0, 1, 128))))
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

def finite_diff_bidimensional(Temp, time, dx, dy, dt):
    n = len(Temp) - 1
    m = len(Temp[0]) - 1
    time_len = len(time)
    t = 0.
    Temp_new = np.copy(Temp)
    result = np.zeros([time_len, n + 1, m + 1])
        
    
    if dt <= (dx ** 2) / 4.  and dt <= (dy ** 2) / 4.:
        while t < time[-1] - 0.1 * dt:
            for i in range(1, n):
                for j in range(1, m):
                    x_axis = (dt / (dx ** 2)) * (Temp[i + 1][j] - 2 * Temp[i][j] + Temp[i - 1][j])
                    y_axis = (dt / (dx ** 2)) * (Temp[i][j + 1] - 2 * Temp[i][j] + Temp[i][j - 1])
                    Temp_new[i][j] = Temp[i][j] + x_axis + y_axis
            for i in range(time_len):
                if t < time[i] + .1 * dt  and t > time[i] - .1 * dt:
                    result[i] = np.copy(Temp_new[::-1])
                    print(f'Result Saved | t = {t:.6f}')
                
            Temp = np.copy(Temp_new)
            t += dt
        result[i] = np.copy(Temp_new[::-1])
        print(f'Result Saved | t = {t:.6f}')
        return result


length_x = 1.
length_y = .2   

dx = 0.01
dy = 0.01
dt = (dx ** 2) / 4
t_final = .005

max_resolution = 1e-3

time = [dt,  t_final / 4, t_final / 2,  3 * t_final / 4, t_final]
time_len = len(time)

x_arr = np.arange(0., length_x, dx)
y_arr = np.arange(0., length_y, dy)

Temp_init_func = lambda x : np.abs(np.sin( 4 * (PI * x)))

m, n = len(x_arr), len(y_arr)

Temp = np.zeros([n, m], float)


for i in range(m):
    Temp[0][i] =  1.#Temp_init_func(x_arr[i])
    Temp[-1][i] = 0.

for j in range(n):
    Temp[j][0] = 0.
    Temp[j][-1] = 0.

print(Temp)


results = finite_diff_bidimensional(Temp, time, dx, dy, dt)

leg = []
for i in range(len(time)):
    leg.append(f'Temperature distribuition at time = {time[i]:.4f}\n')

plot_cmap(leg, results)
plt.show()


def refine_mesh(Temp):
    m, n = len(Temp), len(Temp[0])
    
    dx_arr = np.zeros(n)
    dy_arr = np.zeros(m)
    
    for i in range(0, m):
        pass
