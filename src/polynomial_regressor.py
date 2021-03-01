import sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor

class PolynomialRegressor():

    def __init__(self, degree):
        self.degree = degree
        self.df = None
        self.first_variable = None
        self.dependent_variable = None
        self.coefficients = None
    
    def fit(self, dataframe, dependent_variable):
        
        self.first_variable = dataframe.columns[0]
        self.dependent_variable = dependent_variable

        if self.degree == 0:
            new_columns = [self.dependent_variable]
        elif self.degree == 1:
            new_columns = [self.first_variable, self.dependent_variable]
        else:
            new_columns = [self.first_variable]
            for i in range(2, self.degree + 1):
                new_term = self.first_variable + '^' + str(i)
                new_columns.append(new_term)
            new_columns.append(self.dependent_variable)

        new_dataset = []
        for pair in dataframe.to_array():
            new_values = []
            for i in range(1, self.degree + 1):  
                value = pair[0] ** i
                new_values.append(value)
            new_values.append(pair[1])
            new_dataset.append(new_values)

        self.df = DataFrame.from_array(new_dataset, new_columns)
    
    def solve_coefficients(self):
        
        linear_regressor = LinearRegressor(self.df, self.dependent_variable)
        self.coefficients = linear_regressor.coefficients
    
    def predict(self, this_dict):

        first_variable_value = this_dict[self.first_variable]

        for key in self.df.columns:
            if key not in (self.first_variable, self.dependent_variable):
                exponent = float(key.split('^')[1])
                value = first_variable_value ** exponent
                this_dict[key] = value

        linear_regressor = LinearRegressor(self.df, self.dependent_variable)
        return linear_regressor.predict(this_dict)