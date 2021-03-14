import math
import sys
sys.path.append('src')
from dataframe import *
from linear_regressor import *

dataset = [(0.0, 7.0), (0.2, 5.6), (0.4, 3.56), (0.6, 1.23), (0.8, -1.03), (1.0, -2.89), (1.2, -4.06), (1.4, -4.39), (1.6, -3.88), (1.8, -2.64), (2.0, -0.92), (2.2, 0.95), (2.4, 2.63), (2.6, 3.79), (2.8, 4.22), (3.0, 3.8), (3.2, 2.56), (3.4, 0.68), (3.6, -1.58), (3.8, -3.84), (4.0, -5.76), (4.2, -7.01), (4.4, -7.38), (4.6, -6.76), (4.8, -5.22)]

new_dataset = [(math.sin(x), math.cos(x), math.sin(2*x), math.cos(2*x), y) for x, y in dataset]
columns = ['sin(x)', 'cos(x)', 'sin(2x)', 'cos(2x)', 'y']
df = DataFrame.from_array(new_dataset, columns)

signal_regressor = LinearRegressor(df, 'y')
# print("\ncoefficients:", signal_regressor.coefficients)

print([elem for elem in list(signal_regressor.coefficients.values())])

import matplotlib.pyplot as plt
plt.clf()
plt.style.use('bmh')

actual_x = [pair[0] for pair in dataset]
actual_y = [pair[1] for pair in dataset]

x_values = [x/100 for x in range(500)]
predicted_y = []
for x in x_values:
    this_dict = {'sin(x)': math.sin(x), 'cos(x)': math.cos(x), 'sin(2x)': math.sin(2*x), 'cos(2x)': math.cos(2*x)}
    prediction = signal_regressor.predict(this_dict)
    predicted_y.append(prediction)

plt.plot(actual_x, actual_y, label='Actual Values')
plt.plot(x_values, predicted_y, label='Predicted Values')
plt.legend()

plt.xlabel('x') 
plt.ylabel('y')
plt.savefig('signal_separation.png')