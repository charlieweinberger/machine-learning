import sys
sys.path.append('datasets')
sys.path.append('src')
from semirandom_dataset import *
from decision_tree import *

def correct_classification(decision_tree, test_fold):
    total = 0
    correct = 0
    for key in ['x', 'o']:
        for point in test_fold[key]:
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

def plot_accuracy_vs_min_size_to_split(points, num_folds, min_size_to_split_list):
    
    x_points, o_points = list(points.values())
    random.shuffle(x_points)
    random.shuffle(o_points)
    points_copy = {'x': x_points, 'o': o_points}

    folds_list = get_folds_list(points_copy, num_folds)
    accuracy_list = []
        
    for min_size_to_split in min_size_to_split_list:
        
        num_correct_classifications = 0

        for test_fold in folds_list:

            testing_points = {'x': [], 'o': []}
            for key in ['x', 'o']:
                for point in points_copy[key]:
                    if point not in test_fold[key]:
                        testing_points[key].append(point)

            decision_tree = DecisionTree(testing_points, min_size_to_split, True)
            decision_tree.fit()
            num_correct_classifications += correct_classification(decision_tree, test_fold)

        accuracy = num_correct_classifications / num_folds
        accuracy_list.append(accuracy)

    plt.plot(min_size_to_split_list, accuracy_list)
    plt.xlabel('min size to split')
    plt.ylabel('5-fold cross-validation accuracy')
    plt.savefig('images/min_size_to_split_vs_accuracy.png')

centers = [(1, 4), (4, 1), (1, 1), (4, 4)]
classes = ['o', 'o', 'x', 'x']
colors = {'x': 'red', 'o': 'blue'}
farthest = 4
power = 1.5
num_points = 200

points = semirandom_dataset(centers, classes, colors, farthest, power, num_points)
min_size_to_split_list = [1, 2, 5, 10, 15, 20, 30, 50, 100]

plot_accuracy_vs_min_size_to_split(points, 5, min_size_to_split_list)
print('done')