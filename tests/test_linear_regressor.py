import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor

df = DataFrame.from_array(
    [[0, 0, 1], 
     [1, 0, 2],
     [2, 0, 4],
     [4, 0, 8],
     [6, 0, 9],
     [0, 2, 2],
     [0, 4, 5],
     [0, 6, 7],
     [0, 8, 6]],
    columns = ['Slices of Roast Beef', 'Tablespoons of Peanut Butter', 'Rating']
)
regressor = LinearRegressor(df, dependent_variable = 'Rating')

# part i
print("part i:", regressor.coefficients)

# part ii
ii_dict = {
                    'Slices of Roast Beef': 5,
                    'Tablespoons of Peanut Butter': 0
               }
print("part ii:", regressor.predict(ii_dict))

# part iii
iii_dict = {
                    'Slices of Roast Beef': 5,
                    'Tablespoons of Peanut Butter': 5
               }
print("part iii:", regressor.predict(iii_dict))