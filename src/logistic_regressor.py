import math
import sys
sys.path.append('src')
from linear_regressor import LinearRegressor

def ln(x):
    return math.log(x) / math.log(math.e)

class LogisticRegressor():
    
    def __init__(self, dataframe, dependent_variable):
        self.dataframe = dataframe
        self.dependent_variable = dependent_variable
        self.coefficients = self.calculate_coefficients()

    def calculate_coefficients(self):

        y = self.dataframe.data_dict[self.dependent_variable]
        self.dataframe.data_dict[self.dependent_variable] = [ln((1 / var_val) - 1) for var_val in y]

        logistic_regressor = LinearRegressor(self.dataframe, dependent_variable = self.dependent_variable)
        
        return logistic_regressor.coefficients

    def predict(self, this_dict):
        
        coefficients_keys = list(self.coefficients.keys())
        coefficients = list(self.coefficients.values())

        linear_prediction = coefficients[0]

        for i in range(1, len(coefficients)):
            key = coefficients_keys[i]
            if key != self.dependent_variable:
                linear_prediction += self.coefficients[key] * this_dict[key]

        logistic_prediction = 1 / (1 + math.e ** linear_prediction)
        return logistic_prediction