import random, math
import matplotlib.pyplot as plt
plt.style.use('bmh')

from sklearn.ensemble import RandomForestClassifier

# dataset
def get_dist(power, farthest):
    population = [round(x/100, 2) for x in range(int(100 * farthest))]
    weights = [power ** (-x) for x in population]
    weights = [x / sum(weights) for x in weights]
    return random.choices(population, weights)[0]

def semirandom_dataset(centers, classes, colors, farthest, power, total_num_points):
    
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
    
    return points

# code
def correct_classification(decision_tree, fold):
    total = 0
    correct = 0
    for key in ['x', 'o']:
        for point in fold[key]:
            if decision_tree.predict([point]) == key:
                correct += 1
            total += 1
    return correct / total

def get_folds_list(points, num_folds):
    folds_list = [{'x': [], 'o': []} for _ in range(num_folds)]
    for key in ['x', 'o']:
        for point in points[key]:
            i = random.randint(0, num_folds-1)
            folds_list[i][key].append(point)
    return folds_list

centers = [(-2, -2), (2, 2), (-2, 2), (2, -2)]
classes = ['x', 'x', 'o', 'o']
colors = {'x': 'red', 'o': 'blue'}
farthest = 4
power = 1.5
num_points = 200

dataset_points_dict = semirandom_dataset(centers, classes, colors, farthest, power, num_points)

num_folds = 2
num_trees = 100
min_size_to_split = 2 

training, testing = get_folds_list(dataset_points_dict, num_folds)
forest = RandomForestClassifier(n_estimators=num_trees)

x_and_y = [(elem, key) for key, value in training.items() for elem in value]
x = [list(elem[0]) for elem in x_and_y]
y = [elem[1] for elem in x_and_y]
forest.fit(x, y)

many_points = [[x/10, y/10] for x in range(-60, 60) for y in range(-60, 60)]
dataset_points = dataset_points_dict['x'] + dataset_points_dict['o']

for point in many_points:
    prediction = forest.predict([point])[0]
    plt.scatter(point[0], point[1], s=2, c=colors[prediction], alpha=0.5)

for point in dataset_points:
    prediction = forest.predict([point])[0]
    plt.scatter(point[0], point[1], s=50, c=colors[prediction])

plt.savefig('sklearn_random_forest_2.png')

print('done')