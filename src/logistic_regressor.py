import math
from linear_regressor import *

class LogisticRegressor():

    def __init__(self, df, dependent_variable, upper_bound):
        self.df = df
        self.dv = dependent_variable
        self.idvs = [elem for elem in self.df.columns if elem != self.dv]
        self.upper_bound = upper_bound

        try:
            self.coefficients = self.calculate_coefficients()
        except:
            self.coefficients = {element:None for element in ['constant'] + self.idvs}

    def copy(self):
        return LogisticRegressor(self.df, self.dv, self.upper_bound)

    def calculate_coefficients(self):
        
        data_dict = {key:value.copy() for key, value in self.df.data_dict.items()}
        data_dict[self.dv] = [math.log((self.upper_bound / elem) - 1) for elem in data_dict[self.dv]]
        
        
        new_df = DataFrame(data_dict, self.df.columns)
        linear_regressor = LinearRegressor(new_df, self.dv)
        return linear_regressor.coefficients

    def predict(self, input_dict):
        
        prediction = self.coefficients['constant']

        for key in self.idvs:
            
            to_multiply = 1
            should_be_in_input_dict = key.split(' * ') if ' * ' in key else [key]
            
            if all(elem in input_dict for elem in should_be_in_input_dict):
                for elem in should_be_in_input_dict:
                    to_multiply *= input_dict[elem]
            
            prediction += self.coefficients[key] * to_multiply

        return self.upper_bound / (1 + math.exp(prediction))

    def calc_rss(self):  
        
        dv_index = self.df.columns.index(self.dv)
        
        rss = 0
        for row in self.df.to_array():
            
            predict = {self.idvs[n]:row[n] for n in range(len(self.idvs))}
            rss += (self.predict(predict) - row[dv_index]) ** 2

        return rss

    def set_coefficients(self, coeffs):
        self.coefficients = coeffs

    def calc_gradient(self, delta):
        
        regressor1 = self.copy()
        regressor2 = self.copy()
        gradient = {}
        
        for key in self.coefficients:
            
            coefficients1 = self.coefficients.copy()
            coefficients2 = self.coefficients.copy()
            
            coefficients1[key] += delta / 2
            coefficients2[key] -= delta / 2
            
            regressor1.set_coefficients(coefficients1)
            regressor2.set_coefficients(coefficients2)
            
            gradient[key] = (regressor1.calc_rss() - regressor2.calc_rss()) / delta
        
        return gradient
    
    def gradient_descent(self, alpha, delta, num_steps, debug_mode=False):
      
        for i in range(num_steps):
            gradient = self.calc_gradient(delta)
            
            if debug_mode:
                print("Step #{}:".format(i))
                print("\tGradient:", gradient)
                print("\tCoefficients:", self.coefficients)
                print("\tRSS:", self.calc_rss())
            
            for key in gradient:
                self.coefficients[key] -= gradient[key] * alpha