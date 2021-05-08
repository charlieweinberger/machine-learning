import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
plt.style.use('bmh')

# python analysis/knn_normalized_data.py

df = pd.read_csv("datasets/knn_book_data.csv")
df['book type'] = df['book type'].apply(lambda x: 1 if x == "adult book" else 0)

df1 = df.copy()
df2 = df.copy()
df3 = df.copy()

for col in df1:
    if col != 'book type':
        df1[col] = df1[col] / df[col].max()

for col in df2:
    if col != 'book type':
        df2[col] = (df2[col] - df[col].min()) / (df[col].max() - df[col].min())

for col in df3:
    if col != 'book type':
        df3[col] = (df3[col] - df[col].mean()) / df[col].std()

df_list = [df, df1, df2, df3]
k_values = list(range(1, 100, 2))
accuracies_types = ['unnormalized', 'simple scaling', 'min-max', 'z-scoring']

def row_prediction_is_correct(knn, x, y, k, row_index):

    observation    = x[row_index]
    classification = y[row_index]

    x_leave_one_out = [x[i] for i in range(len(x)) if i != row_index]
    y_leave_one_out = [y[i] for i in range(len(y)) if i != row_index]

    prediction = knn.fit(x_leave_one_out, y_leave_one_out).predict([observation])[0]
    return int(classification == prediction)

def knn_accuracies(this_df):
    
    len_df_numpy = len(this_df.to_numpy())
    accuracies = []
    
    x = this_df[[col for col in this_df.columns if col != 'book type']].to_numpy().tolist()
    y = [elem[0] for elem in this_df[['book type']].to_numpy().tolist()]

    for k in k_values:
        
        knn = KNeighborsClassifier(n_neighbors = k)
        num_correct = [row_prediction_is_correct(knn, x, y, k, row_index) for row_index in range(len_df_numpy)]
        accuracy = sum(num_correct) / len_df_numpy
        accuracies.append(accuracy)
    
    return accuracies

for df_index in range(len(df_list)):
    
    this_df = df_list[df_index] 
    accuracies = knn_accuracies(this_df)
    plt.plot(k_values, accuracies, label=accuracies_types[df_index])

plt.legend()
plt.xlabel('k')
plt.ylabel('Accuracy')
plt.xticks([0, 20, 40, 60, 80, 100])
plt.title('Leave-One-Out Accuracy for Various Normalizations')
plt.savefig('leave_one_out_accuracy_for_various_normalizations.png')