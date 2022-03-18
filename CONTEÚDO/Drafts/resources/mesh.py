import numpy as np
from matplotlib import pyplot as plt

# Lets begin by creating a constant resolution grid, this means that the step between two points is a fixed value
# !_!_!_!_!_!_!
# !_!_!_!_!_!_!
# !_!_!_!_!_!_!
# !_!_!_!_!_!_!
# !_!_!_!_!_!_!
def generateGrid():
    step = 0.1
    cavity_sides = [1., 1.]

    grid = [[],[]]

    x_grid = np.arange(0, cavity_sides[0], step)
    y_grid = np.arange(0, cavity_sides[1], step)

    points = []
    for i in range(0, len(x_grid)):
        for j in range(0, len(y_grid)):
            point = [x_grid[i], y_grid[j]]
            print(point)
            points.append(point)

    plt.figure()
    for point in points:
        print(point)
        plt.scatter(point[0], point[1])
    plt.show()