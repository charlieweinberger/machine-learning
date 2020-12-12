import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor

df = DataFrame.from_array(
    [[0, 0, 0.1],
     [1, 0, 0.2],
     [0, 2, 0.5],
     [4, 5, 0.6]],
    columns = ['scoops of chocolate', 'scoops of vanilla', 'taste rating']
)

regressor = LinearRegressor(df, dependent_variable = 'taste rating')

ans = {
          'constant': 0.19252336,
          'scoops of chocolate': -0.05981308,
          'scoops of vanilla': 0.13271028
      }
assert {key:round(value, 8) for (key, value) in regressor.coefficients.items()} == ans, {key:round(value, 8) for (key, value) in regressor.coefficients.items()} # these coefficients are rounded, you should only round in your assert statement

dict_problem = {
                    'scoops of chocolate': 2,
                    'scoops of vanilla': 3
               }
assert round(regressor.predict(dict_problem), 8) == 0.47102804, round(regressor.predict(dict_problem), 8)

print("passed all")