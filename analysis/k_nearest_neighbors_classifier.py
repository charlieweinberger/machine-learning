import pandas as pd

class KNearestNeighborsClassifier():
    
    def __init__(self, k):
        self.k = k
    
    def fit(self, df, dv):
        self.df = df
        self.dv = dv
        self.dv_index = self.df.columns[0].index(self.dv)
        self.idvs = [elem for elem in self.df.columns if elem != self.dv]

    def get_data(self):
        return [list(elem) for elem in list(self.df.values)]

    def euclidean_distance_calculator(self, a_values, b_values):
        radicand_list = [(a_values[i] - b_values[i]) ** 2 for i in range(len(a_values))]
        return sum(radicand_list) ** 0.5

    def compute_distances(self, observation):

        observation_values = list(observation.values())
        data = []

        for this_list in self.get_data():
            this_dv = this_list[self.dv_index]
            this_list.remove(this_dv)
            distance = self.euclidean_distance_calculator(observation_values, this_list)
            data.append([distance, this_dv])

        return pd.DataFrame(data, columns=['Distance', self.dv])

    def nearest_neighbors(self, observation):
        new_df = self.compute_distances(observation)
        return new_df.sort_values(by=['Distance'])
    
    def classify(self, observation):
        ordered_df = self.nearest_neighbors(observation)
        ans = ordered_df[self.dv][:self.k].mode()
        str_ans = str(ans).split('\n')[0].split(' ')[4]
        return str_ans