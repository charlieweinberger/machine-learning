import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

import time
start_time = time.time()

df1 = pd.read_csv("datasets/processed_dataset.csv")
features = ["Sex", "Pclass", "Fare", "Age","SibSp"]
df1 = df1[:100][["Survived"] + features]

df2 = df1.copy()
df3 = df1.copy()
df4 = df1.copy()

for col in features:
    df2[col] = df2[col] / df2[col].max()
    df3[col] = (df3[col] - df3[col].min()) / (df3[col].max() - df3[col].min())
    df4[col] = (df4[col] - df4[col].mean()) / df4[col].std()

y_df = df1['Survived'].to_numpy().tolist()

def leave_one_out_cross_validation(x_df, k):

    knn = KNeighborsClassifier(n_neighbors = k)
    num_correct = 0
    num_classifications = len(x_df)

    for i in range(num_classifications):
    
        x_copy = x_df.copy()
        y_copy = y_df.copy()

        observation    = x_copy[i]
        classification = y_copy[i]

        del x_copy[i]
        del y_copy[i]

        prediction = knn.fit(x_copy, y_copy).predict([observation])

        if type(prediction) == list:
            print('hi')

        if classification == prediction:
            num_correct += 1
    
    return num_correct / num_classifications

x_df1 = df1[[col for col in df1.columns if col != 'Survived']].to_numpy().tolist()
x_df2 = df2[[col for col in df1.columns if col != 'Survived']].to_numpy().tolist()
x_df3 = df3[[col for col in df1.columns if col != 'Survived']].to_numpy().tolist()
x_df4 = df4[[col for col in df1.columns if col != 'Survived']].to_numpy().tolist()

k_values = [2*n + 1 for n in range(50)]

df1_accuracies = []
df2_accuracies = []
df3_accuracies = []
df4_accuracies = []

for k in k_values:
    df1_accuracies.append(leave_one_out_cross_validation(x_df1, k))
    df2_accuracies.append(leave_one_out_cross_validation(x_df2, k))
    df3_accuracies.append(leave_one_out_cross_validation(x_df3, k))
    df4_accuracies.append(leave_one_out_cross_validation(x_df4, k))

plt.style.use('bmh')
plt.plot(k_values, df1_accuracies, label='unnormalized')
plt.plot(k_values, df2_accuracies, label='simple scaling')
plt.plot(k_values, df3_accuracies, label='min-max')
plt.plot(k_values, df4_accuracies, label='z-scoring')

plt.legend(loc='best')
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.xticks([0, 20, 40, 60, 80, 100])
plt.title('Leave-One-Out Accuracy for Various Normalizations')
plt.savefig('leave_one_out_accuracy_for_various_normalizations.png')

end_time = time.time()
print('\ntime taken:', end_time - start_time)

# python kaggle/titanic/tittanic_knn-normalized_data.py

# multiplier = 0.2693
# relative speed = 0.2693 / 0.15 = 1.8
# target time = 1.8 * 45 = 81