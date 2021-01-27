import math
import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
from logistic_regressor import LogisticRegressor

sm = 0.0001

df = DataFrame.from_array(
    [[sm, sm, 1, sm], 
    [1, sm, 2, sm], 
    [2, sm, 4, sm], 
    [4, sm, 8, sm], 
    [6, sm, 9, sm], 
    [sm, 2, 2, sm], 
    [sm, 4, 5, sm], 
    [sm, 6, 7, sm], 
    [sm, 8, 6, sm],
    [2, 2, 0.1, 4],
    [3, 4, 0.1, 12]],
    columns = ['beef', 'pb', 'rating', 'beef * pb']
)

regressor = LogisticRegressor(df, dependent_variable = 'rating', upper_bound = 10)
coefficients = regressor.coefficients
print("\ncoefficients:", coefficients)

# part ii
ii_dict = {
                    'beef': 5,
                    'pb': 0
               }
print("part ii:", regressor.predict(ii_dict))

# part iii
iii_dict = {
                    'beef': 12,
                    'pb': 0
               }
print("part iii:", regressor.predict(iii_dict))

# part iv
iv_dict = {
                    'beef': 5,
                    'pb': 5
               }
print("part iv:", regressor.predict(iv_dict))