import math
import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
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

regressor = LogisticRegressor(df, dependent_variable = 'rating', upper_bound = 10)
logistic_coefficients = regressor.coefficients
logistic_coefficients_values = list(logistic_coefficients.values())
print("\nlogistic_coefficients_values:", logistic_coefficients_values)

test_1 = {
         'beef': 8,
         'pb': 0,
         'condiments': ['mayo']
        }
print("\n8 slices of beef + mayo:", regressor.predict(test_1)) # should be 9.718

test_2 = {
         'beef': 0,
         'pb': 4,
         'condiments': ['jelly']
        }
print("4 tbsp of pb + jelly:", regressor.predict(test_2)) # should be 8.2956

test_3 = {
         'beef': 0,
         'pb': 4,
         'condiments': ['mayo']
        }

print("4 tbsp of pb + mayo:", regressor.predict(test_3)) # should be 0.1803

test_4 = {
         'beef': 8,
         'pb': 4,
         'condiments': ['mayo']
        }
print("4 tbsp of pb + 8 slices of beef + mayo:", regressor.predict(test_4)) # should be 0.7674

test_5 = {
         'beef': 8,
         'pb': 0,
         'condiments': ['mayo', 'jelly']
        }
print("8 slices of beef + mayo + jelly:", regressor.predict(test_5)) # should be 0.7926