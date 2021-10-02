import matplotlib.pyplot as plt
plt.style.use('bmh')
import pandas as pd
from sklearn.cluster import KMeans

# python kaggle/titanic/titanic_elbow_method.py

df = pd.read_csv("datasets/processed_dataset.csv")
features = ["Sex", "Pclass", "Fare", "Age", "SibSp"]
new_df = df[features]
result_df = df[features + ['Survived']]

for col in new_df:
    new_df[col] = (new_df[col] - new_df[col].min()) / (new_df[col].max() - new_df[col].min())

k_values = list(range(1, 26))
data = new_df.to_numpy()
sum_squared_error_list = [KMeans(n_clusters=k).fit(data).inertia_ for k in k_values]

plt.plot(k_values, sum_squared_error_list)
plt.xticks(k_values)
plt.xlabel('k')
plt.ylabel('sum squared distances from cluster centers')
plt.savefig('k_means_clustering_on_titanic_dataset.png')

kmeans = KMeans(n_clusters=4, random_state=0).fit(data)
labels = list(kmeans.labels_)

result_df['cluster'] = labels
result_df['count'] = result_df['cluster'].apply(lambda x: labels.count(x))
cluster_df = result_df.groupby(['cluster']).mean()

print("\n", cluster_df)