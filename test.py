clusters = {
    "hi": 312,
    "hi2": 4311,
    "hi3": 3
}

print(min(clusters, key=clusters.get))
