import random
import sys
sys.path.append('src')
from decision_tree import *

class RandomForest():
    
    def __init__(self, num_trees, point_dict, min_size_to_split, is_random, p=0.8):
        
        self.num_trees = num_trees
        self.point_dict = point_dict
        self.min_size_to_split = min_size_to_split
        self.is_random = is_random
        self.p = p
        self.trees = self.set_trees()
    
    def set_trees(self):
        trees = []
        for _ in range(self.num_trees):
            tree = DecisionTree(self.get_point_dict_subset(), self.min_size_to_split, self.is_random)
            tree.fit()
            trees.append(tree)
        return trees

    def get_point_dict_subset(self):
        
        if self.is_random: return self.point_dict

        all_points = [(key, point) for key, value in self.set_point_dict(point_dict).items() for point in value]
        used_points = []

        subset = {'x': [], 'o': []}
        for _ in range(round(len(all_points) * self.p)):
            available_points = list(set(all_points) - set(used_points))
            key, point = random.choice(available_points)
            subset[key].append(point)
            used_points.append((key, point))
        
        return subset

    def predict(self, point):

        predictions = {'x': 0, 'o': 0}
        for tree in self.trees:
            predictions[tree.predict(point)] += 1

        ties = [key for key, value in predictions.items() if value == max(predictions.values())]
        return random.choice(ties)