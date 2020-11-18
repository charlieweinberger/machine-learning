import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor

df = DataFrame.from_array(
    [[1,0.2],
     [2,0.25],
     [3,0.5]],
    columns = ['hours worked', 'progress']
)

print(df.data_dict)

regressor = LinearRegressor(df, dependent_variable = 'progress')

assert regressor.coefficients == [0.01667, 0.15], regressor.coefficients
assert regressor.predict({'hours worked': 4}) == 0.61667, regressor.predict({'hours worked': 4})

print("passed all")