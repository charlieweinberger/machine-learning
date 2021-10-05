import random
import math
import matplotlib.pyplot as plt
plt.style.use('bmh')

def get_dist(power, farthest):
    population = [round(x/100, 2) for x in range(int(100 * farthest))]
    weights = [power ** (-x) for x in population]
    weights = [x / sum(weights) for x in weights]
    return random.choices(population, weights)[0]

def semirandom_dataset(centers, classes, colors, farthest, total_num_points, power, show):

    num_sets = len(centers)
    points = [[] for _ in range(num_sets)]

    for i in range(num_sets):
        
        center = centers[i]
        for _ in range(total_num_points // num_sets):

            d = get_dist(power, farthest)
            theta = random.uniform(0, 2 * math.pi)

            x = center[0] + d * math.cos(theta)
            y = center[1] + d * math.sin(theta)

            point = {'x': x, 'y': y, 'class': classes[i]}
            points[i].append(point)

        if show:

            x_points = [point['x'] for point in points[i]]
            y_points = [point['y'] for point in points[i]]

            print('\ncenter:    ', center)
            print('est_center:', (round(sum(x_points) / len(x_points), 3), round(sum(y_points) / len(y_points), 3)))

            plt.scatter(x_points, y_points, c=colors[i])

    if show:
        plt.savefig('images/semirandom_dataset.png')
    
    return [point for center_points in points for point in center_points]

# python datasets/semirandom_dataset.py