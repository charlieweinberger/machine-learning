import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
from linear_regressor import LinearRegressor
 
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
 
regressor = LinearRegressor(df, dependent_variable = 'rating')
linear_coefficients = regressor.coefficients
linear_coefficients_values = list(linear_coefficients.values())
print("\nlinear_coefficients_values:", linear_coefficients_values)

test_1 = {
         'beef': 8,
         'pb': 0,
         'condiments': ['mayo']
        }
print("\n8 slices of beef + mayo:", regressor.predict(test_1))

test_2 = {
         'beef': 0,
         'pb': 4,
         'condiments': ['jelly']
        }
print("4 tbsp of pb + jelly:", regressor.predict(test_2))
 
test_3 = {
         'beef': 0,
         'pb': 4,
         'condiments': ['mayo']
        }
print("4 tbsp of pb + mayo:", regressor.predict(test_3))
 
test_4 = {
         'beef': 8,
         'pb': 4,
         'condiments': ['mayo']
        }
print("4 tbsp of pb + 8 slices of beef + mayo:", regressor.predict(test_4))
 
test_5 = {
         'beef': 8,
         'pb': 0,
         'condiments': ['mayo', 'jelly']
        }
print("8 slices of beef + mayo + jelly:", regressor.predict(test_5))