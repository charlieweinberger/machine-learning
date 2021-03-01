import sys
sys.path.append('src')
from dataframe import DataFrame
from polynomial_regressor import PolynomialRegressor

df = DataFrame.from_array(
    [(0,1),
     (1,2), 
     (2,5), 
     (3,10), 
     (4,20), 
     (5,30)],
    columns = ['x', 'y']
)

def round_dict(this_dict, amount):
    new_dict = {}
    for key, value in this_dict.items():
        new_value = round(value, amount)
        new_dict[key] = new_value
    return new_dict

constant_regressor = PolynomialRegressor(degree=0)
constant_regressor.fit(df, dependent_variable='y')
constant_regressor.solve_coefficients()
assert round_dict(constant_regressor.coefficients, 4) == {'constant': 11.3333}, round_dict(constant_regressor.coefficients, 4)
assert round(constant_regressor.predict({'x': 2}), 4) == 11.3333

print("passed constant_regressor")

linear_regressor = PolynomialRegressor(degree=1)
linear_regressor.fit(df, dependent_variable='y')
linear_regressor.solve_coefficients()
assert round_dict(linear_regressor.coefficients, 4) == {'constant': -3.2381, 'x': 5.8286}
assert round(linear_regressor.predict({'x': 2}), 4) == 8.4190

print("passed linear_regressor")

quadratic_regressor = PolynomialRegressor(degree=2)
quadratic_regressor.fit(df, dependent_variable='y')
quadratic_regressor.solve_coefficients()
assert round_dict(quadratic_regressor.coefficients, 4) == {'constant': 1.1071, 'x': -0.6893, 'x^2': 1.3036}
assert round(quadratic_regressor.predict({'x': 2}), 4) == 4.9429

print("passed quadratic_regressor")

cubic_regressor = PolynomialRegressor(degree=3)
cubic_regressor.fit(df, dependent_variable='y')
cubic_regressor.solve_coefficients()
assert round_dict(cubic_regressor.coefficients, 4) == {'constant': 1.1349, 'x': -0.8161, 'x^2': 1.3730, 'x^3': -0.0093}
assert round(cubic_regressor.predict({'x': 2}), 4) == 4.9206

print("passed cubic_regressor")

quintic_regressor = PolynomialRegressor(degree=5)
quintic_regressor.fit(df, dependent_variable='y')
quintic_regressor.solve_coefficients()
assert round_dict(quintic_regressor.coefficients, 4) == {'constant': 1.0000, 'x': -2.9500, 'x^2': 6.9583, 'x^3': -3.9583, 'x^4': 1.0417, 'x^5': -0.0917}
assert round(quintic_regressor.predict({'x': 2}), 4) == 5.0000

print("passed quintic_regressr")