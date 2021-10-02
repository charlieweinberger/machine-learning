import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
 
class LinearRegressor():
  
    def __init__(self, dataframe, dependent_variable):
        self.df = dataframe
        self.dv = dependent_variable
        self.independent_variables = [elem for elem in self.df.columns if elem != self.dv]
        self.coefficients = self.calculate_coefficients()
    
    def calculate_coefficients(self):
  
        data_dict = self.df.data_dict
        df_column_values = list(data_dict.values())
        dv_values = data_dict[self.dv]

        mat = []
        for i in range(len(df_column_values[0])):
            thing_to_add = [1] + [elem[i] for elem in df_column_values if elem != dv_values]
            mat.append(thing_to_add)
        
        mat = Matrix(mat)
        mat_transpose = mat.transpose()
        pseudoinv = (mat_transpose @ mat).inverse() @ mat_transpose

        right_side_no_matrix = [[num] for num in dv_values]
        right_side = (pseudoinv @ Matrix(right_side_no_matrix)).elements
 
        coefficients_keys = ['constant'] + self.independent_variables
        coefficients_dict = {coefficients_keys[i]:right_side[i][0] for i in range(len(right_side))}
  
        return coefficients_dict

    def predict(self, this_dict):

        ans = self.coefficients['constant']
        
        for key in self.coefficients:
            if key != 'constant':
                
                if ' * ' not in key:
                    this_dict_value = this_dict[key]
            
                else:
                    both_keys = key.split(' * ')
                    this_dict_value = 1
                    for one_key in both_keys:
                        this_dict_value *= this_dict[one_key]

                ans += self.coefficients[key] * this_dict_value

        return ans