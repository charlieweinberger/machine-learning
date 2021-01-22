import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor

df = DataFrame.from_array(
    [[0, 0, 1, 0], 
    [1, 0, 2, 0], 
    [2, 0, 4, 0], 
    [4, 0, 8, 0], 
    [6, 0, 9, 0], 
    [0, 2, 2, 0], 
    [0, 4, 5, 0], 
    [0, 6, 7, 0], 
    [0, 8, 6, 0],
    [2, 2, 0, 4],
    [3, 4, 0, 12]],
    columns = ['beef', 'pb', 'rating', 'beef * pb']
)
regressor = LinearRegressor(df, dependent_variable = 'rating')
coefficients = regressor.coefficients
print(coefficients)

# part iii
iii_dict = {
                    'beef': 5,
                    'pb': 0
               }
print("part iii:", regressor.predict(iii_dict))

# part iV
iv_dict = {
                    'beef': 5,
                    'pb': 5
               }
print("part iv:", regressor.predict(iv_dict))