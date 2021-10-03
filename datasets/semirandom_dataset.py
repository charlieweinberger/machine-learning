import random
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

def get_coord(power, center):
    population = [round(0.1*x, 1) for x in range(10 * (center - farthest), 10 * (center + farthest + 1))]
    left_weights  = [power ** (x - center) for x in population[:len(population) // 2]]
    right_weights = [power ** (center - x) for x in population[len(population) // 2:]]
    weights = [x / sum(left_weights + right_weights) for x in left_weights + right_weights]
    return random.choices(population, weights)

def avg(x):
    return round(sum(x) / len(x), 3)

def semirandom_dataset(centers, classes, colors, farthest, total_num_points, power, show):

    num_sets = len(centers)
    points = [[] for _ in range(num_sets)]

    for i in range(num_sets):
        
        center = centers[i]
        for _ in range(total_num_points // num_sets):
            x, y = get_coord(power, center[0]), get_coord(power, center[1])
            point = {'x': x[0], 'y': y[0], 'class': classes[i]}
            points[i].append(point)

        x_points = [point['x'] for point in points[i]]
        y_points = [point['y'] for point in points[i]]

        print('\ncenter:    ', center)
        print('est_center:', (avg(x_points), avg(y_points)))

        if show:
            plt.scatter(x_points, y_points, c=colors[i])

    if show:
        plt.show()
    
    return points

centers = [(1, 4), (4, 1), (1, 1), (4, 4)]
classes = [0, 0, 1, 1]
colors = ['#0000FF', '#00FF00', '#FF0000', '#800080']
farthest = 3
total_num_points = 200
power = 5

points = semirandom_dataset(centers, classes, colors, farthest, total_num_points, power, show=True)

'''
python datasets/semirandom_dataset.py
'''