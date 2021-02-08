import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
from logistic_regressor import LogisticRegressor

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0],
    [5, 5, [],                0],
    [5, 5, ['mayo'],          0],
    [5, 5, ['jelly'],         0],
    [5, 5, ['mayo', 'jelly'], 0]],
    columns = ['beef', 'pb', 'condiments', 'rating']
)
 
df = df.create_dummy_variables('condiments')
df = df.create_interaction_terms(dependent_variable = 'rating')

linear_regressor = LinearRegressor(df, dependent_variable = 'rating')
logistic_regressor = LogisticRegressor(df, dependent_variable = 'rating', upper_bound = 10)

# test 8 slices of beef + mayo
observation = {'beef': 8, 'mayo': 1}
assert round(linear_regressor.predict(observation), 2) == 11.34
assert round(logistic_regressor.predict(observation), 2) == 9.72

# test 4 tbsp of pb + 8 slices of beef + mayo
observation = {
                'beef': 8, 
                'pb': 4, 
                'mayo': 1
              }
assert round(linear_regressor.predict(observation), 2) == 3.62
assert round(logistic_regressor.predict(observation), 2) == 0.77

# test 8 slices of beef + mayo + jelly
observation = {
                'beef': 8, 
                'mayo': 1, 
                'jelly': 1
              }
assert round(linear_regressor.predict(observation), 2) == 2.79
assert round(logistic_regressor.predict(observation), 2) == 0.79

print("passed all")