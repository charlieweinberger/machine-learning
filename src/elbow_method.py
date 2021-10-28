import matplotlib.pyplot as plt
plt.style.use('bmh')
import sys
sys.path.append('src')
from k_means import *

class ElbowMethod():

    def __init__(self, data, k_list):
        self.data = data
        self.k_list = k_list
        self.sum_squared_error_list = []

    def run(self):

        for k in self.k_list:

            clusters = self.initial_clusters(k)
            kmeans = KMeans(clusters, self.data)
            kmeans.run()

            total_sum_squared_error = self.cal_total_sum_squared_error(kmeans)
            self.sum_squared_error_list.append(total_sum_squared_error)
        
        self.print_graph()

    def initial_clusters(self, k):
        clusters = {this_k:[] for this_k in range(k)}
        for i in range(len(self.data)):
            clusters[i % k].append(i)
        return clusters

    def cal_total_sum_squared_error(self, kmeans):
        total_squared_error = 0
        for i in range(len(self.data)):
            euclidean_distance = kmeans.euclidean_distance(self.data[i], self.get_center(kmeans, i))
            total_squared_error += euclidean_distance ** 2
        return total_squared_error
    
    def get_center(self, kmeans, i):
        for index, values in kmeans.clusters.items():
            if i in values:
                return kmeans.centers[index]

    def print_graph(self):
        plt.plot(self.k_list, self.sum_squared_error_list)
        plt.xlabel('k')
        plt.ylabel('sum squared error')
        plt.savefig('sum_squared_error_vs_k.png')

# test