import sys
sys.path.append('src')
from k_means import *

columns = ['Portion Eggs',
            'Portion Butter',
            'Portion Sugar',
            'Portion Flour']

classes = ['Shortbread',
            'Fortune',
            'Shortbread',
            'Sugar',
            'Fortune',
            'Shortbread',
            'Sugar',
            'Shortbread',
            'Sugar',
            'Shortbread',
            'Sugar',
            'Fortune',
            'Shortbread',
            'Fortune',
            'Sugar',
            'Shortbread',
            'Sugar',
            'Fortune',
            'Shortbread']

"""

1. Initialize the clusters
   - Randomly divide the data into k parts. Each part represents an initial "cluster".
   - Compute the mean of each part. Each mean represents an initial cluster center.

2. Update the clusters
   - Re-assign each record to the cluster with the nearest center (using Euclidean distance).
   - Compute the new cluster centers by taking the mean of the records in each cluster.

3. Keep repeating step 2 until the clusters don't change after the update.

"""

data = [[0.14, 0.14, 0.28, 0.44],
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
        [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]]

initial_clusters = {
    1: [0,3,6,9,12,15,18],
    2: [1,4,7,10,13,16],
    3: [2,5,8,11,14,17]
}

kmeans = KMeans(initial_clusters, data)
kmeans.run()

assert kmeans.clusters == {
    1: [0, 2, 5, 7, 9, 12, 15, 18],
    2: [3, 6, 8, 10, 14, 16],
    3: [1, 4, 11, 13, 17]
}

print("passed")

"""

# Step-by-step instructions:

initial_clusters = {1: [0, 3, 6, 9, 12, 15, 18], 2: [1, 4, 7, 10, 13, 16], 3: [2, 5, 8, 11, 14, 17]}

kmeans = KMeans(initial_clusters, data)

print("passed 1.1")

### ITERATION 1
kmeans.update_clusters_once()

assert kmeans.clusters == {1: [0, 3, 6, 9, 12, 15, 18], 2: [1, 4, 7, 10, 13, 16], 3: [2, 5, 8, 11, 14, 17]}

assert kmeans.centers == {1: [0.113, 0.146, 0.324, 0.437], 2: [0.122, 0.115, 0.353, 0.427], 3: [0.117, 0.11, 0.352, 0.417]}

print("passed 1.5")

assert {n: [classes[i] for i in cluster_indices] \
    for cluster_number, cluster_indices in kmeans.clusters.items()} == {
    1: ['Shortbread', 'Sugar', 'Sugar', 'Shortbread', 'Shortbread', 'Shortbread', 'Shortbread'], 
    2: ['Fortune', 'Fortune', 'Shortbread', 'Sugar', 'Fortune', 'Sugar'], 
    3: ['Shortbread', 'Shortbread', 'Sugar', 'Fortune', 'Sugar', 'Fortune']
}

print("\niter 2\n")

### ITERATION 2
kmeans.update_clusters_once()

assert kmeans.clusters == {
    1: [0, 2, 5, 6, 7, 9, 10, 12, 15, 18],
    2: [14, 16],
    3: [1, 3, 4, 8, 11, 13, 17]
}

assert kmeans.centers == {
    1: [0.111, 0.158, 0.302, 0.448],
    2: [0.0, 0.115, 0.4, 0.495],
    3: [0.159, 0.08, 0.383, 0.379]
}

assert {n: [classes[i] for i in cluster_indices] \
    for cluster_number, cluster_indices in kmeans.clusters.items()} == {
    1: ['Shortbread', 'Shortbread', 'Shortbread', 'Sugar', 'Shortbread', 'Shortbread', 'Sugar', 'Shortbread', 'Shortbread', 'Shortbread'], 
    2: ['Sugar', 'Sugar'], 
    3: ['Fortune', 'Sugar', 'Fortune', 'Sugar', 'Fortune', 'Fortune', 'Fortune']
}

### ITERATION 3
kmeans.update_clusters_once()

assert kmeans.clusters == {
    0: [0, 2, 5, 7, 9, 12, 15, 18],
    1: [3, 6, 8, 10, 14, 16],
    2: [1, 4, 11, 13, 17]
}

assert kmeans.centers == {
    0: [0.133, 0.171, 0.291, 0.416],
    1: [0.018, 0.1, 0.378, 0.51],
    2: [0.21, 0.08, 0.38, 0.346]
}

assert {n: [classes[i] for i in cluster_indices] \
    for cluster_number, cluster_indices in kmeans.clusters.items()} == {
    0: ['Shortbread', 'Shortbread', 'Shortbread', 'Shortbread', 'Shortbread', 'Shortbread', 'Shortbread', 'Shortbread'],
    1: ['Sugar', 'Sugar', 'Sugar', 'Sugar', 'Sugar', 'Sugar'],
    2: ['Fortune', 'Fortune', 'Fortune', 'Fortune', 'Fortune']
}

print("passed 2")
"""