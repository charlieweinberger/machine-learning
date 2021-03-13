import sys
sys.path.append('src')
from dataframe import *
from polynomial_regressor import *

dataset = [(-4, 11.0), (-2, 5.0), (0, 3.0), (2, 5.0), (4, 11.1), (6, 21.1), (8, 35.1), (10, 52.8), (12, 74.8), (14, 101.2)]

training_data = [dataset[i] for i in range(len(dataset)) if i % 2 == 0]
testing_data = [dataset[i] for i in range(len(dataset)) if i % 2 == 1]

training_df = DataFrame.from_array(training_data, columns=['x', 'y'])

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(training_df, 'y')

quadratic_regressor = PolynomialRegressor(degree=2)
quadratic_regressor.fit(training_df, 'y')

cubic_regressor = PolynomialRegressor(degree=3)
cubic_regressor.fit(training_df, 'y')

quartic_regressor = PolynomialRegressor(degree=4)
quartic_regressor.fit(training_df, 'y')

# calculating RSS values
def calc_rss(regressor, dataset):
    rss_value = 0
    for point in dataset:
        y = point[1]
        f_x = regressor.predict({'x': point[0]})
        rss_value += (y - f_x) ** 2
    return rss_value

print("\ncalc_rss(linear_regressor, training_data):   ", calc_rss(linear_regressor, training_data))
print("calc_rss(linear_regressor, testing_data):    ", calc_rss(linear_regressor, testing_data))

print("\ncalc_rss(quadratic_regressor, training_data):", calc_rss(quadratic_regressor, training_data))
print("calc_rss(quadratic_regressor, testing_data): ", calc_rss(quadratic_regressor, testing_data))

print("\ncalc_rss(cubic_regressor, training_data):    ", calc_rss(cubic_regressor, training_data))
print("calc_rss(cubic_regressor, testing_data):     ", calc_rss(cubic_regressor, testing_data))

print("\ncalc_rss(quartic_regressor, training_data):  ", calc_rss(quartic_regressor, training_data))
print("calc_rss(quartic_regressor, testing_data):   ", calc_rss(quartic_regressor, testing_data))

# plotting all models
import matplotlib.pyplot as plt
plt.style.use('bmh')

x = [pair[0] for pair in dataset]
y = [pair[1] for pair in dataset]

plt.plot(x, y, label='Actual Values')

training_x = [dataset[pair_index][0] for pair_index in range(len(dataset)) if pair_index % 2 == 0]
testing_x = [dataset[pair_index][0] for pair_index in range(len(dataset)) if pair_index % 2 == 1]

linear_training_values = [linear_regressor.predict({'x': pair[0]}) for pair in training_data]
linear_testing_values = [linear_regressor.predict({'x': pair[0]}) for pair in testing_data]

plt.plot(training_x, linear_training_values, label = "Linear Training values")
plt.plot(testing_x, linear_testing_values, label = "Linear Testing values")

quadratic_training_values = [quadratic_regressor.predict({'x': pair[0]}) for pair in training_data]
quadratic_testing_values = [quadratic_regressor.predict({'x': pair[0]}) for pair in testing_data]

plt.plot(training_x, quadratic_training_values, label = "Quadratic Training values")
plt.plot(testing_x, quadratic_testing_values, label = "Quadratic Testing values")

cubic_training_values = [cubic_regressor.predict({'x': pair[0]}) for pair in training_data]
cubic_testing_values = [cubic_regressor.predict({'x': pair[0]}) for pair in testing_data]

plt.plot(training_x, cubic_training_values, label = "Cubic Training values")
plt.plot(testing_x, cubic_testing_values, label = "Cubic Testing values")

quartic_training_values = [quartic_regressor.predict({'x': pair[0]}) for pair in training_data]
quartic_testing_values = [quartic_regressor.predict({'x': pair[0]}) for pair in testing_data]

plt.plot(training_x, quartic_training_values, label = "Quartic Training values")
plt.plot(testing_x, quartic_testing_values, label = "Quartic Testing values")

plt.legend()

plt.xlabel('x') 
plt.ylabel('y')
plt.savefig('training_and_testing_sets.png')

# calculating the differences in RSS
def rss_difference_calc(regressor):
    return abs(calc_rss(regressor, training_data) - calc_rss(regressor, testing_data))

print("\nrss_difference_calc(linear_regressor):   ", rss_difference_calc(linear_regressor))
print("rss_difference_calc(quadratic_regressor):", rss_difference_calc(quadratic_regressor))
print("rss_difference_calc(cubic_regressor):    ", rss_difference_calc(cubic_regressor))
print("rss_difference_calc(quartic_regressor):  ", rss_difference_calc(quartic_regressor))