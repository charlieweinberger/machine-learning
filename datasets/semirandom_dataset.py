import random
import math
import matplotlib.pyplot as plt
plt.style.use('bmh')

def get_dist(power, farthest):
    population = [round(x/100, 2) for x in range(int(100 * farthest))]
    weights = [power ** (-x) for x in population]
    weights = [x / sum(weights) for x in weights]
    return random.choices(population, weights)[0]

def semirandom_dataset(centers, classes, colors, farthest, power, total_num_points, show=False):

    num_sets = len(centers)
    points = {'x': [], 'o': []}

    for i in range(num_sets):
        
        center = centers[i]
        for _ in range(total_num_points // num_sets):

            d = get_dist(power, farthest)
            theta = random.uniform(0, 2 * math.pi)

            x = center[0] + d * math.cos(theta)
            y = center[1] + d * math.sin(theta)

            points[classes[i]].append((x, y))

    if show:

        for key, value in points.items():
            for point in value:
                plt.plot(point[0], point[1], color=colors[key], marker=key)

        plt.savefig('images/semirandom_dataset.png')

    return points