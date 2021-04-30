import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
plt.style.use('bmh')

df = pd.DataFrame(
    [['Shortbread', 0.14, 0.14, 0.28, 0.44],
     ['Shortbread', 0.10, 0.18, 0.28, 0.44],
     ['Shortbread', 0.12, 0.10, 0.33, 0.45],
     ['Shortbread', 0.10, 0.25, 0.25, 0.40],
     ['Sugar'     , 0.00, 0.10, 0.40, 0.50],
     ['Sugar'     , 0.00, 0.20, 0.40, 0.40],
     ['Sugar'     , 0.02, 0.08, 0.45, 0.45],
     ['Sugar'     , 0.10, 0.15, 0.35, 0.40],
     ['Sugar'     , 0.10, 0.08, 0.35, 0.47],
     ['Sugar'     , 0.00, 0.05, 0.30, 0.65],
     ['Fortune'   , 0.20, 0.00, 0.40, 0.40],
     ['Fortune'   , 0.25, 0.10, 0.30, 0.35],
     ['Fortune'   , 0.22, 0.15, 0.50, 0.13],
     ['Fortune'   , 0.15, 0.20, 0.35, 0.30],
     ['Fortune'   , 0.22, 0.00, 0.40, 0.38],
     ['Shortbread', 0.05, 0.12, 0.28, 0.55],
     ['Shortbread', 0.14, 0.27, 0.31, 0.28],
     ['Shortbread', 0.15, 0.23, 0.30, 0.32],
     ['Shortbread', 0.20, 0.10, 0.30, 0.40]],
     columns = ['Cookie Type', 'Portion Eggs', 'Portion Butter', 'Portion Sugar', 'Portion Flour']
    )

accuracies = []
k_values = range(1, 19)

def df_to_list(df):
    return df.to_numpy().tolist()

def row_prediction_is_correct(knn, i):

    x_df = df[[col for col in df.columns if col != 'Cookie Type']]
    y_df = df['Cookie Type']

    df_to_row = lambda a: df_to_list(a.iloc[[i]])[0]
    current_values =         df_to_row(x_df)
    current_classification = df_to_row(y_df)
    
    df_to_dataset = lambda a: df_to_list(a.drop([i]).reset_index(drop=True))
    train = df_to_dataset(x_df)
    test =  df_to_dataset(y_df)

    other_knn = knn.fit(train, test)
    other_classification = other_knn.predict([current_values])

    return current_classification == other_classification

for k in k_values:
    
    knn = KNeighborsClassifier(n_neighbors = k)
    
    num_total = len(df_to_list(df))
    num_correct = ['' for i in range(num_total) if row_prediction_is_correct(knn, i)]
    
    accuracy = len(num_correct) / num_total
    accuracies.append(accuracy)

plt.plot(k_values, accuracies)
plt.xlabel('k')
plt.ylabel('accuracy')
plt.xticks(k_values)
plt.title('Leave One Out Cross Validation')
plt.savefig('leave_one_out_accuracy.png')