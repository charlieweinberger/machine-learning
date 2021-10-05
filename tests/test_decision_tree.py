import sys
sys.path.append('datasets')
sys.path.append('src')
from semirandom_dataset import *
from decision_tree import *

import matplotlib.pyplot as plt
plt.style.use('bmh')

# class 0 means 'o' and class 1 means 'x'

centers = [(1, 4), (4, 1), (1, 1), (4, 4)]
classes = [0, 0, 1, 1]
colors = ['#0000FF', '#0000FF', '#FF0000', '#FF0000']
total_num_points = 200
farthest = 4
power = 1.5
points_og = semirandom_dataset(centers, classes, colors, farthest, total_num_points, power, show=False)

points = points_og.copy()
random.shuffle(points)

folds_list = [points[i:i + 40] for i in range(0, 200, 40)]
min_size_to_split_list = [1, 2, 5, 10, 15, 20, 30, 50, 100]
accuracy_list = []

for min_size_to_split in min_size_to_split_list:
    
    num_classifications = 0
    num_correct_classifications = 0

    for test_fold in folds_list:

        testing_points = [point for fold in folds_list for point in fold if fold != test_fold]
        decision_tree = DecisionTree(testing_points, min_size_to_split)
        decision_tree.fit()
        num_classifications += 1
        num_correct_classifications += correct_classification(decision_tree, test_fold)

    accuracy = num_correct_classifications / num_classifications
    accuracy_list.append(accuracy)

def correct_classification(decision_tree, test_fold):
    correct = 0
    for point in test_fold:
        if decision_tree.predict(point) == point['class']:
            correct += 1
    return correct / len(test_fold)

plt.plot(min_size_to_split_list, accuracy_list)
plt.xlabel('min_size_to_split')
plt.ylabel('5-fold cross-validation accuracy')
plt.savefig('min_size_to_split_vs_accuracy.png')

# makes some error in the decision_tree, but idk what

'''

def draw_points(points):
    print('\ny=9  ' + map_to[(1, 9)] + '   ' + map_to[(2, 9)] + '   ' + map_to[(3, 9)] + '   ' + map_to[(4, 9)] + '   ' + map_to[(5, 9)] + '   ' + map_to[(6, 9)] + '   ' + map_to[(7, 9)] + '   ' + map_to[(8, 9)] + '   ' + map_to[(9, 9)])
    print('y=8  ' + map_to[(1, 8)] + '   ' + map_to[(2, 8)] + '   ' + map_to[(3, 8)] + '   ' + map_to[(4, 8)] + '   ' + map_to[(5, 8)] + '   ' + map_to[(6, 8)] + '   ' + map_to[(7, 8)] + '   ' + map_to[(8, 8)] + '   ' + map_to[(9, 8)])
    print('y=7  ' + map_to[(1, 7)] + '   ' + map_to[(2, 7)] + '   ' + map_to[(3, 7)] + '   ' + map_to[(4, 7)] + '   ' + map_to[(5, 7)] + '   ' + map_to[(6, 7)] + '   ' + map_to[(7, 7)] + '   ' + map_to[(8, 7)] + '   ' + map_to[(9, 7)])
    print('y=6  ' + map_to[(1, 6)] + '   ' + map_to[(2, 6)] + '   ' + map_to[(3, 6)] + '   ' + map_to[(4, 6)] + '   ' + map_to[(5, 6)] + '   ' + map_to[(6, 6)] + '   ' + map_to[(7, 6)] + '   ' + map_to[(8, 6)] + '   ' + map_to[(9, 6)])
    print('y=5  ' + map_to[(1, 5)] + '   ' + map_to[(2, 5)] + '   ' + map_to[(3, 5)] + '   ' + map_to[(4, 5)] + '   ' + map_to[(5, 5)] + '   ' + map_to[(6, 5)] + '   ' + map_to[(7, 5)] + '   ' + map_to[(8, 5)] + '   ' + map_to[(9, 5)])
    print('y=4  ' + map_to[(1, 4)] + '   ' + map_to[(2, 4)] + '   ' + map_to[(3, 4)] + '   ' + map_to[(4, 4)] + '   ' + map_to[(5, 4)] + '   ' + map_to[(6, 4)] + '   ' + map_to[(7, 4)] + '   ' + map_to[(8, 4)] + '   ' + map_to[(9, 4)])
    print('y=3  ' + map_to[(1, 3)] + '   ' + map_to[(2, 3)] + '   ' + map_to[(3, 3)] + '   ' + map_to[(4, 3)] + '   ' + map_to[(5, 3)] + '   ' + map_to[(6, 3)] + '   ' + map_to[(7, 3)] + '   ' + map_to[(8, 3)] + '   ' + map_to[(9, 3)])
    print('y=2  ' + map_to[(1, 2)] + '   ' + map_to[(2, 2)] + '   ' + map_to[(3, 2)] + '   ' + map_to[(4, 2)] + '   ' + map_to[(5, 2)] + '   ' + map_to[(6, 2)] + '   ' + map_to[(7, 2)] + '   ' + map_to[(8, 2)] + '   ' + map_to[(9, 2)])
    print('y=1  ' + map_to[(1, 1)] + '   ' + map_to[(2, 1)] + '   ' + map_to[(3, 1)] + '   ' + map_to[(4, 1)] + '   ' + map_to[(5, 1)] + '   ' + map_to[(6, 1)] + '   ' + map_to[(7, 1)] + '   ' + map_to[(8, 1)] + '   ' + map_to[(9, 1)])
    print('    x=1 x=2 x=3 x=4 x=5 x=6 x=7 x=8 x=9\n')

def tree_structure(input_node, min_size_to_split, num=''):
    
    print("structure of tree after iteration {}\n".format(num))
    draw_points(input_node.points)
    
    if not input_node.is_pure_enough(min_size_to_split):
    
        for split in input_node.splits:
            print('split at ' + str(split.dim) + '=' + str(split.midpoint) + ':', '\n')
            for node in split.children[::-1]:
                draw_points(node.points)
    
    else:
        print("node is pure\n")

def best_split(input_node, num=''):
    print("\nbest split after iteration {}".format(num))
    split = input_node.find_best_split()
    print(str(split.dim) + '=' + str(split.midpoint), '\n')

'''