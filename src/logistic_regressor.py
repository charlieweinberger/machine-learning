import math
import sys
sys.path.append('src')
from linear_regressor import LinearRegressor

def ln(x):
    if x > 0:
        return math.log(x) / math.log(math.e)
    else:
        print("x is currently {}, but it can't be less than zero".format(x))
 
class LogisticRegressor():

    def __init__(self, dataframe, dependent_variable, upper_bound):
        self.dataframe = dataframe
        self.dependent_variable = dependent_variable
        self.upper_bound = upper_bound
        self.coefficients = self.calculate_coefficients()
 
    def calculate_coefficients(self):
        
        y = self.dataframe.data_dict[self.dependent_variable]
        self.dataframe.data_dict[self.dependent_variable] = [0.1 if elem == 0 else elem for elem in y]

        y = self.dataframe.data_dict[self.dependent_variable]
        self.dataframe.data_dict[self.dependent_variable] = [ln((self.upper_bound / var_val) - 1) for var_val in y]
 
        logistic_regressor = LinearRegressor(self.dataframe, dependent_variable = self.dependent_variable)
        return logistic_regressor.coefficients
 
    def predict(self, this_dict):

        linear_regressor = LinearRegressor(self.dataframe, dependent_variable = self.dependent_variable)

        new_dict = {}
        for key, value in this_dict.items():
            if value != 0:
                new_dict[key] = value
            else:
                new_dict[key] = 0.1

        linear_prediction = linear_regressor.predict(this_dict, zero_approximation = 0)
        logistic_prediction = self.upper_bound / (1 + (math.e ** linear_prediction))

        return logistic_prediction