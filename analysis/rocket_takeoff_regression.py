import sys
sys.path.append('src')
from dataframe import DataFrame
from polynomial_regressor import PolynomialRegressor

data = [(1, 3.1), (2, 10.17), (3, 20.93), (4, 38.71), (5, 60.91), (6, 98.87), (7, 113.92), (8, 146.95), (9, 190.09), (10, 232.65)]

columns = ['time', 'distance']
df = DataFrame.from_array(data, columns)

# Part A

print("\nquadratic_regressor")

quadratic_regressor = PolynomialRegressor(degree=2)
quadratic_regressor.fit(df, dependent_variable='distance')
quadratic_regressor.solve_coefficients()

n_list = [5, 10, 200]
for n in n_list:
    prediction = quadratic_regressor.predict({'time': n})
    print(n, "->", prediction)

# Part B

print("\ncubic_regressor")

cubic_regressor = PolynomialRegressor(degree=3)
cubic_regressor.fit(df, dependent_variable='distance')
cubic_regressor.solve_coefficients()

n_list = [5, 10, 200]
for n in n_list:
    prediction = cubic_regressor.predict({'time': n})
    print(n, "->", prediction)

# Part C

import matplotlib.pyplot as plt
plt.style.use('bmh')

times = [n for n in range(0, 201)]
quadratic_values = [quadratic_regressor.predict({'time': n}) for n in times]
cubic_values = [cubic_regressor.predict({'time': n}) for n in times]

plt.plot(times, quadratic_values, label="Quadratic Regressor")
plt.plot(times, cubic_values, label="Cubic Regressor")
plt.legend()

plt.xlabel('time')
plt.ylabel('predicted distance')
plt.savefig('rocket_takeoff_regression.png')