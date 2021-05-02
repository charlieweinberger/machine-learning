import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
plt.style.use('bmh')

def df_to_list(df):
    return df.to_numpy().tolist()

def row_prediction_is_correct(knn, i, dv):

    x_df = df[[col for col in df.columns if col != dv]]
    y_df = df[dv]

    df_to_row = lambda a: df_to_list(a.iloc[[i]])[0]
    current_values =         df_to_row(x_df)
    current_classification = df_to_row(y_df)
    
    df_to_dataset = lambda a: df_to_list(a.drop([i]).reset_index(drop=True))
    train = df_to_dataset(x_df)
    test =  df_to_dataset(y_df)

    other_knn = knn.fit(train, test)
    other_classification = other_knn.predict([current_values])

    return current_classification == other_classification

def knn_accuracies(df, k_values, dv):

    accuracies = []

    for k in k_values:
        
        knn = KNeighborsClassifier(n_neighbors = k)
        
        num_total = len(df_to_list(df))
        num_correct = [row_prediction_is_correct(knn, i, dv) for i in range(num_total)]
        
        accuracy = sum(num_correct) / num_total
        accuracies.append(accuracy)
    
    return accuracies

df = pd.read_csv("kaggle/data/processes_dataset.csv")
features_to_keep = ["Survived", "Sex", "Pclass", "Fare", "Age", "SibSp"]
df = df[:100][features_to_keep]

print("\ndf:", df)

k_values = [1, 3, 5, 10, 15, 20, 30, 40, 50, 75]
accuracies = knn_accuracies(df, k_values, 'Survived')

# python kaggle/titanic/knn_titanic_survival_modeling.py

plt.plot(k_values, accuracies)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.xticks(k_values)
plt.title('Leave-One-Out Accuracy vs k')
plt.savefig('leave_one_out_accuracy_vs_k.png')