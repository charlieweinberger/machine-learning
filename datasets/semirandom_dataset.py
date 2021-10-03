import random
import math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

def get_dist(power, farthest):
    population = [round(x/100, 2) for x in range(int(100 * farthest))]
    weights = [power ** (-x) for x in population]
    weights = [x / sum(weights) for x in weights]
    return random.choices(population, weights)[0]

def get_angle():
    return 2 * math.pi * random.random()

def avg(x):
    return round(sum(x) / len(x), 3)

def semirandom_dataset(centers, classes, colors, farthest, total_num_points, power, show):

    num_sets = len(centers)
    points = [[] for _ in range(num_sets)]

    for i in range(num_sets):
        
        center = centers[i]
        for _ in range(total_num_points // num_sets):

            d, theta = get_dist(power, farthest), get_angle()
            
            dx = d * math.cos(theta)
            dy = d * math.sin(theta)
            
            x = center[0] + dx
            y = center[1] + dy

            point = {'x': x, 'y': y, 'class': classes[i]}
            points[i].append(point)

        if show:

            x_points = [point['x'] for point in points[i]]
            y_points = [point['y'] for point in points[i]]

            print('\ncenter:    ', center)
            print('est_center:', (avg(x_points), avg(y_points)))

            plt.scatter(x_points, y_points, c=colors[i])

    if show:
        plt.show()
    
    return points

centers = [(1, 4), (4, 1), (1, 1), (4, 4)]
classes = [0, 0, 1, 1]
colors = ['#0000FF', '#0000FF', '#FF0000', '#FF0000']
total_num_points = 200

farthest = 2.1
power = 1.5

points = semirandom_dataset(centers, classes, colors, farthest, total_num_points, power, show=True)

# python datasets/semirandom_dataset.py