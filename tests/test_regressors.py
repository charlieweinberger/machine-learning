import matplotlib.pyplot as plt
plt.style.use('bmh')
import sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor
from logistic_regressor import LogisticRegressor

arr = [
  [1,0],
  [2,0], 
  [3,0],
  [2,1],
  [3,1],
  [4,1]
]
df = DataFrame.from_array(arr, columns = ['x', 'y'])

'''
python tests/test_regressors.py
'''

reg = LogisticRegressor(df, dependent_variable='y', upper_bound=1)
reg.set_coefficients({'constant': 0.5, 'x': 0.5})

alpha = 0.01
delta = 0.01
num_steps = 20000
reg.gradient_descent(alpha, delta, num_steps)

print("\nreg.coefficients:", reg.coefficients) # should be {'constant': 2.7911, 'x': -1.1165}

x = [pair[0] for pair in arr]
y = [pair[1] for pair in arr]

lots_of_xs = [x/100 for x in range(100, 401)]
prediction = [reg.predict({'x':x}) for x in lots_of_xs]

plt.scatter(x, y, label="Actual", color="red")
plt.plot(lots_of_xs, prediction, label='Gradient descent')

plt.legend(loc='best')
plt.savefig('logistic_regressor_gradient_descent.png')

"""

x_points = [pair[0] for pair in arr]
y_points = [pair[1] for pair in arr]
plt.scatter(x_points, y_points, label="Actual", color="red")

def num_into_approximation(this_df, this_dv, zero_val):
    
    new_data_dict = {}
    for key, value in this_df.data_dict.items():
        
        if key == this_dv:
            value = [zero_val if elem == 0 else 1 - zero_val if elem == 1 else elem for elem in value]
        
        new_data_dict[key] = value
    
    return DataFrame(new_data_dict, this_df.columns)

zero_values = [0.1, 0.01, 0.001, 0.0001]
dfs = [num_into_approximation(df, 'y', zero_value) for zero_value in zero_values]
regressors = [LogisticRegressor(this_df, 'y', 1) for this_df in dfs]

lots_of_xs = [x/100 for x in range(100, 401)]
predictions = [[regressor.predict({'x':x}) for x in lots_of_xs] for regressor in regressors]

for i in range(len(predictions)):
    plt.plot(lots_of_xs, predictions[i], label = zero_values[i])

plt.legend()

plt.xlabel('x')
plt.ylabel('y')
plt.savefig('issue_with_LogisticRegressor.png')

"""