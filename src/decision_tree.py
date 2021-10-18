import math
import random

class DecisionTree():
    
    def __init__(self, point_dict, min_size_to_split, is_random):
        
        self.point_dict = point_dict
        self.min_size_to_split = min_size_to_split
        self.is_random = is_random

        self.entropy = self.get_entropy()
        self.parent = None
        self.branches = []
        self.best_split = None
    
    def set_point_dict(self, point_dict):
        return self.point_dict if point_dict == None else point_dict

    def get_all_coords(self, point_dict=None):
        all_coords_nested = self.set_point_dict(point_dict).values()
        return [coord for type_coords in all_coords_nested for coord in type_coords]

    def get_entropy(self, point_dict=None):
        entropy = 0
        point_dict = self.set_point_dict(point_dict)
        for sign in point_dict:
            ratio = len(point_dict[sign]) / len(self.get_all_coords(point_dict))
            if ratio != 0:
                entropy += -1 * ratio * math.log(ratio)
        return entropy
    
    def remove_from_dict(self, input_dict, vals):
        return {k:[x for x in list(v) if x not in vals] for k, v in input_dict.items()}

    def get_midpoints(self, points):
        return [(points[i] + points[i+1]) / 2 for i in range(len(points) - 1)]

    def get_splits(self, point_dict=None):
        result = []
        all_coords = self.get_all_coords(point_dict)
        for i in range(len(all_coords[0])):
            unique = list(set([coord[i] for coord in all_coords]))
            result += [(i, midpoint) for midpoint in self.get_midpoints(unique)]
        return result
    
    def split(self, split_tuple, point_dict=None):
        
        check = point_dict == None
        point_dict = self.set_point_dict(point_dict)
        
        index, val = split_tuple
        
        greater = [coord for coord in self.get_all_coords(point_dict) if coord[index] >= val]
        lesser  = [coord for coord in self.get_all_coords(point_dict) if coord[index] <  val]
        
        greater_dict = self.remove_from_dict(point_dict,  lesser)
        lesser_dict  = self.remove_from_dict(point_dict, greater)
        
        if check:
            child_1 = DecisionTree(greater_dict, self.min_size_to_split, False)
            child_2 = DecisionTree( lesser_dict, self.min_size_to_split, False)
            child_1.parent = self
            child_2.parent = self
            self.branches = [child_1, child_2]
        
        return [greater_dict, lesser_dict]
    
    def weighted_entropy(self, point_dict_list):
        
        weighted_entropy = 0
        num_points = sum([len(self.get_all_coords(point_dict)) for point_dict in point_dict_list])
        
        for point_dict in point_dict_list:
            entropy = self.get_entropy(point_dict)
            num_point_ratio = len(self.get_all_coords(point_dict)) / num_points
            weighted_entropy += entropy * num_point_ratio
        
        return weighted_entropy
    
    def get_best_split(self, point_dict=None):
        
        check = point_dict == None
        point_dict = self.set_point_dict(point_dict)
        all_splits = self.get_splits(point_dict)

        if self.is_random:
            best_split = random.choice(all_splits)
        
        else:
            best_split = all_splits[0]
            best_entropy = self.weighted_entropy(self.split(best_split, point_dict))
            
            for split in all_splits:
            
                branches = self.split(split, point_dict)
                weighted_entropy = self.weighted_entropy(branches)
            
                if weighted_entropy < best_entropy:
                    best_split = split
                    best_entropy = weighted_entropy
        
        if check:
            self.best_split = best_split
        
        return best_split

    def fit_helper(self, decision_tree):
        decision_tree.get_best_split()
        decision_tree.split(decision_tree.best_split)
        return [b for b in decision_tree.branches if b.entropy != 0]

    def there_are_multiple_coords(self, decision_tree):
        return len(set(decision_tree.get_all_coords())) != 1

    def there_are_enough_coords(self, decision_tree):
        return len(decision_tree.get_all_coords()) > decision_tree.min_size_to_split

    def fit(self):

        if len(self.branches) != 0 or not self.there_are_enough_coords(self):
            return
        
        branches = self.fit_helper(self)
        next_branches = []
        
        while len(branches) != 0:
            
            for branch in branches:
                if self.there_are_multiple_coords(branch) and self.there_are_enough_coords(branch):
                    next_branches += self.fit_helper(branch)
        
            branches = next_branches
            next_branches = []

    def get_type(self, decision_tree=None):
        
        if decision_tree == None:
            decision_tree = self
        
        if decision_tree.entropy != 0:
        
            lengths = [(key, len(value)) for key, value in decision_tree.point_dict.items()]
            largest_len = max([pair[1] for pair in lengths])
            new_lengths = [pair[0] for pair in lengths if pair[1] == largest_len]   
        
            if len(new_lengths) > 1:
                return random.choice(new_lengths)
        
            return new_lengths[0]
        
        for key, value in decision_tree.point_dict.items():
            if len(value) != 0:
                return key

    def predict(self, point, decision_tree=None):
        
        if decision_tree == None:
            decision_tree = self
        
        decision_tree.fit()
        while decision_tree.entropy != 0 and self.there_are_enough_coords(decision_tree) and self.there_are_multiple_coords(decision_tree):
        
            i, val = decision_tree.best_split
            index = point[i] < val # 0 is False, 1 is True
            decision_tree = decision_tree.branches[index]
        
        return decision_tree.get_type()