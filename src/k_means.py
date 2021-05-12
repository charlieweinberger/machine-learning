import random

class KMeans():

    def __init__(self, initial_clusters, data):
        
        self.clusters = initial_clusters
        self.data = data
        
        self.centers = None

        self.keys = self.clusters.keys()
        self.k = len(self.keys)
        self.num_cols = len(self.data[0])
            
    def run(self):
        old_clusters = None
        while old_clusters != self.clusters:
            old_clusters = self.clusters.copy()
            self.update_clusters_once()
    
    def update_clusters_once(self):
        self.compute_centers()
        self.reassign_clusters()
    
    def compute_centers(self):
        
        self.centers = {key:{} for key in self.keys}

        for i in self.keys:
            for j in range(len(self.data)):
                if j in self.clusters[i]:
                    self.centers[i][j] = self.data[j]

        for key, value in self.centers.items():

            data_col_avgs = []
            for i in range(4):
                col = [row[i] for row in value.values()]
                avg = sum(col) / len(col)
                data_col_avgs.append(round(avg, 3))
            
            self.centers[key] = data_col_avgs

    def reassign_clusters(self):
        
        self.clusters = {key:[] for key in self.clusters.keys()}

        for i in range(len(self.data)):
            closest_center = self.find_closest_center(i)
            self.clusters[closest_center].append(i)

    def find_closest_center(self, i):
        distances = {key:self.euclidean_distance(value, self.data[i]) for key, value in self.centers.items()}
        return min(distances, key=distances.get)

    def euclidean_distance(self, a, b):
        radicand_list = [(a[i] - b[i]) ** 2 for i in range(len(a))]
        return sum(radicand_list) ** 0.5