import math
import sys
sys.path.append('src')
from linear_regressor import LinearRegressor

def ln(x):
    if x > 0:
        return math.log(x) / math.log(math.e)
    else:
        print("x is currently {}, but it cannt be less than zero".format(x))

class LogisticRegressor():
    
    def __init__(self, dataframe, dependent_variable, upper_bound):
        self.dataframe = dataframe
        self.dependent_variable = dependent_variable
        self.upper_bound = upper_bound
        self.coefficients = self.calculate_coefficients()

    def calculate_coefficients(self):

        y = self.dataframe.data_dict[self.dependent_variable]
        self.dataframe.data_dict[self.dependent_variable] = [ln((self.upper_bound / var_val) - 1) for var_val in y]

        logistic_regressor = LinearRegressor(self.dataframe, dependent_variable = self.dependent_variable)
        
        return logistic_regressor.coefficients

    def predict(self, this_dict):

        linear_regressor = LinearRegressor(self.dataframe, dependent_variable = self.dependent_variable)
        linear_prediction = linear_regressor.predict(this_dict)

        logistic_prediction = self.upper_bound / (1 + math.e ** linear_prediction)
        return logistic_prediction