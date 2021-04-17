import sys
sys.path.append('src')
from dataframe import DataFrame

class KNearestNeighborsClassifier():
    
    def __init__(self, k):
        self.k = k
        self.df = None
        self.dv = None
    
    def fit(self, df, dv):
        self.df, self.dv = df, dv

    def euclidean_distance_calculator(self, a_values, b_values):
        radicand = sum([(a_values[i] - b_values[i]) ** 2 for i in range(len(a_values))])
        return radicand ** 0.5

    def compute_distances(self, observation):

        observation_values = list(observation.values())
        ans = []

        for this_list in self.df.to_array():
            distance = self.euclidean_distance_calculator(observation_values, this_list[1:])
            ans.append([distance, this_list[0]])
        
        return ans
    
    def nearest_neighbors(self, observation):
        new_data_dict = self.compute_distances(observation)
        new_df = DataFrame.from_array(new_data_dict, columns=['distance', self.dv])
        return new_df.order_by('distance', ascending=True).to_array()
    
    def classify(self, observation):
        ordered_array = self.nearest_neighbors(observation)
        top_k = [ordered_array[i][1] for i in range(len(ordered_array)) if i < self.k]
        return max(set(top_k), key=top_k.count)