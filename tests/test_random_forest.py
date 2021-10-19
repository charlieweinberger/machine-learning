import sys
sys.path.append('datasets')
sys.path.append('src')
from semirandom_dataset import *
from random_forest import *

def correct_classification(decision_tree, fold):
    total = 0
    correct = 0
    for key in ['x', 'o']:
        for point in fold[key]:
            if decision_tree.predict(point) == key:
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

def get_point_dict(folds, leave_one_out_fold):
    result = {'x': [], 'o': []}
    for fold in folds:
        if fold != leave_one_out_fold:
            for key, value in fold.items():
                result[key] += value
    return result

centers = [(1, 4), (4, 1), (1, 1), (4, 4)]
classes = ['o', 'o', 'x', 'x']
colors = {'x': 'red', 'o': 'blue'}
farthest = 4
power = 1.5
num_points = 200

points = semirandom_dataset(centers, classes, colors, farthest, power, num_points)

folds = get_folds_list(points, 5)
# num_trees_list = [1, 5, 10]
num_trees_list = [1, 10, 20, 50, 100, 200]
min_size_to_split = 10

import time

starting_time = time.time()

accuracy_list = []
for num_trees in num_trees_list:
    
    print("\nnum_trees:", num_trees)

    accuracy = 0
    for leave_one_out_fold in folds:
        point_dict = get_point_dict(folds, leave_one_out_fold)
        forest = RandomForest(num_trees, point_dict, min_size_to_split, False, p=0.8)
        forest.set_trees()
        accuracy += correct_classification(forest, leave_one_out_fold)
    
    accuracy_list.append(accuracy / 5)

    t = time.time() - starting_time
    print("time:", f'{t} seconds' if t < 60 else f'{t/60} minutes')

# wednesday's graph took 38 mintues (about 10 minutes per 100 trees)
# weekend     graph took 49 minutes 

plt.plot(num_trees_list, accuracy_list, color='black', marker='o')
plt.xlabel('# of Decision Trees in RF')
plt.ylabel('5-fold cross-validation accuracy')
plt.savefig('images/random_forest_with_p.png')