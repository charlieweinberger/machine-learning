import math

def calc_entropy(points):

    num_class_0 = sum([point['class'] == 0 for point in points])
    num_class_1 = sum([point['class'] == 1 for point in points])
    
    if num_class_0 == 0 or num_class_1 == 0: return 0
    
    p0 = num_class_0 / len(points)
    p1 = num_class_1 / len(points)
    
    return - p0 * math.log(p0) - p1 * math.log(p1)

class Split:
    def __init__(self, dim, points, midpoint):
        self.dim = dim
        self.points = points
        self.midpoint = midpoint
        self.children = self.set_children()

    def set_children(self):

        divided_points = [[], []]

        for point in self.points:
            point_index = point[self.dim] > self.midpoint # False = 0, True = 1
            divided_points[point_index].append(point)
        
        return [Node(points) for points in divided_points]

    def get_weighted_avg(self):
        less_than_points, greater_than_points = [node.points for node in self.children]
        less_than_weight    = len(less_than_points)    * calc_entropy(less_than_points)
        greater_than_weight = len(greater_than_points) * calc_entropy(greater_than_points)
        return (less_than_weight + greater_than_weight) / len(self.points)

class Node:
    def __init__(self, points):
        self.points = points
        self.splits = self.set_splits()
    
    def set_splits(self):

        splits = []

        for key in self.points[0].keys():
            if key != 'class':

                values = list(set([point[key] for point in self.points]))
                for i in range(len(values) - 1):
                    midpoint = (values[i] + values[i + 1]) / 2
                    split = Split(key, self.points, midpoint)
                    splits.append(split)
        
        return splits

    def find_best_split(self):
        weighted_avgs = [split.get_weighted_avg() for split in self.splits]
        return self.splits[weighted_avgs.index(min(weighted_avgs))]
    
    def is_pure_enough(self, min_size_to_split):
        all_the_same = len(set([(point['x'], point['y']) for point in self.points])) == 1
        return calc_entropy(self.points) == 0 or len(self.points) < min_size_to_split or all_the_same

class DecisionTree:
    def __init__(self, min_size_to_split=1):
        self.root = None
        self.min_size_to_split = min_size_to_split
        
    def fit(self, points):

        self.root = Node(points)
        current_node = self.root
        nodes_to_do = [current_node]

        while len(nodes_to_do) > 0:

            current_node = nodes_to_do[0]
            nodes_to_do.remove(current_node)

            for i in [0, 1]:
                temp_node = current_node.find_best_split().children[i]
                if not temp_node.is_pure_enough(self.min_size_to_split):
                    nodes_to_do.insert(i, temp_node)
    
    def predict(self, point):
        
        current_node = self.root
        while not current_node.is_pure_enough(self.min_size_to_split):
            best_split = current_node.find_best_split()
            child_index = point[best_split.dim] > best_split.midpoint # False = 0, True = 1
            current_node = best_split.children[child_index]
        
        classes = [point['class'] for point in current_node.points]
        # if len([i == 0 for i in classes]) == len([i == 1 or i in classes]):
        #     return random.randint(0, 1)
        return max(set(classes), key = classes.count)