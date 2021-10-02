import random
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

# make distribution more weighted toward the centers

farthest = 3

def get_coord(center):
    population = [round((center - farthest) + 0.1*x, 1) for x in range(0, 10 * (center + farthest) + 20)]
    left_weights  = [2 ** (x - center) for x in population[:len(population) // 2]]
    right_weights = [2 ** (center - x) for x in population[len(population) // 2:]]
    weights = [x / sum(left_weights + right_weights) for x in left_weights + right_weights]
    return random.choices(population, weights)

def avg(x): return sum(x) / len(x)

centers = [(1, 4), (4, 1), (1, 1), (4, 4)]
classes = [0, 0, 1, 1]
points = [[], [], [], []]
colors = ['#0000FF', '#00FF00', '#FF0000', '#800080']

for i in range(4):
    
    center = centers[i]
    for _ in range(50):
        x, y = get_coord(center[0]), get_coord(center[1])
        point = {'x': x[0], 'y': y[0], 'class': classes[i]}
        points[i].append(point)

    x_points = [point['x'] for point in points[i]]
    y_points = [point['y'] for point in points[i]]

    print('')
    print(center)
    print([avg(x_points), avg(y_points)])

    plt.scatter(x_points, y_points, c=colors[i])

plt.show()

'''
python datasets/semirandom_dataset.py
'''