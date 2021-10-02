import matplotlib.pyplot as plt
plt.style.use('bmh')
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

df = pd.read_csv("flowerdata.csv")
df = df.sample(frac=1).reset_index(drop=True)
features = list(df.columns[1:-1])

print("\nsepal_lengths:", df['SepalLengthCm'].mean())
print("sepal_widths:"   , df['SepalWidthCm' ].mean())
print("pedal_lengths:"  , df['PetalLengthCm'].mean())
print("pedal_widths:"   , df['PetalWidthCm' ].mean(), '\n')

for col in features:
    df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

training_df = df[:75]
testing_df = df[75:]

data = df[features].to_numpy().tolist()

print(data)

k_list = [1, 2, 3, 4, 5, 6, 7]
sum_squared_error_list = [KMeans(n_clusters=k).fit(data).inertia_ for k in k_list]

plt.plot(k_list, sum_squared_error_list)
plt.savefig('pfinal2_k_graph.png')