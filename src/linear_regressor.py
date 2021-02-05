import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame
 
class LinearRegressor():
  
    def __init__(self, dataframe, dependent_variable):
        self.dataframe = dataframe
        self.dependent_variable = dependent_variable
        self.coefficients = self.calculate_coefficients()
  
    def calculate_coefficients(self):
  
        self.dataframe.column_values = list(self.dataframe.data_dict.values())

        a_matrix = []
        for i in range(len(self.dataframe.column_values[0])):
            thing_to_add = [1]
          
            for j in range(len(self.dataframe.column_values)):
              
                j_values = self.dataframe.column_values[j]
                dependent_variable_values = self.dataframe.data_dict [self.dependent_variable]
              
                if j_values != dependent_variable_values:
                    thing_to_add.append(j_values[i])
          
            a_matrix.append(thing_to_add)
        
        a_matrix = Matrix(a_matrix)

        a_transpose = a_matrix.transpose()
        a_transpose_times_a_matrix = a_transpose.matrix_multiply(a_matrix)
        inverse_of_a_transpose_times_a_matrix = a_transpose_times_a_matrix.inverse()
        a_pseudoinverse = inverse_of_a_transpose_times_a_matrix.matrix_multiply(a_transpose)
        round_a_pseudoinverse = Matrix([[round(elem, 2) for elem in row] for row in a_pseudoinverse.elements])

        dependent_variable_values = self.dataframe.data_dict[self.dependent_variable]
        right_side_no_matrix = [[num] for num in dependent_variable_values]
        right_side = a_pseudoinverse.matrix_multiply(Matrix(right_side_no_matrix))
 
        coefficients_list = ['constant']
        for key in self.dataframe.columns:
            if key != self.dependent_variable:
                coefficients_list.append(key)
  
        coefficients_dict = {'constant': right_side.elements[0][0]}
        for i in range(len(right_side.elements)):
            key = coefficients_list[i]
            coefficients_dict[key] = right_side.elements[i][0]
  
        return coefficients_dict
  
    def predict(self, this_dict, zero_approximation=0):
        
        all_condiments = []
        for elem in self.dataframe.columns:
            total = list(this_dict.keys()) + all_condiments
            if ' * ' not in elem:
                if elem not in total:
                    all_condiments.append(elem)
            else:
                elem_split = elem.split(' * ')
                for mini_elem in elem_split:
                    if mini_elem not in total:
                        all_condiments.append(mini_elem)

        this_dict_better = {}
        for key, value in this_dict.items():
            if type(value) in (int, float):
                this_dict_better[key] = value
            elif type(value) == list:
                for elem in all_condiments:
                    this_dict_better[elem] = zero_approximation
                for elem in value:
                    this_dict_better[elem] = 1

        this_dict_better_keys = list(this_dict_better.keys())

        coefficients_keys = list(self.coefficients.keys())
        coefficient_values = list(self.coefficients.values())

        # print("\nthis_dict:", this_dict)
        # print("this_dict_better:", this_dict_better)
        # print("this_dict_better_keys:", this_dict_better_keys)

        # print("\ncoefficients_keys:", coefficients_keys)
        # print("\ncoefficient_values:", coefficient_values)

        ans = coefficient_values[0]
        for i in range(1, len(coefficient_values)):
            key = coefficients_keys[i]
            coefficient_value = coefficient_values[i]
            
            if ' * ' not in key:
                this_dict_value = this_dict_better[key]
            else:
                both_keys = key.split(' * ')
                this_dict_value = 1
                for one_key in both_keys:
                    this_dict_value *= this_dict_better[one_key]

            ans += coefficient_value * this_dict_value

        return ans