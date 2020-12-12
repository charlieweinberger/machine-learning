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
        
        a_matrix = []
        for i in range(len(self.dataframe.column_values[0])):
            thing_to_add = [1]
            for j in range(len(self.dataframe.column_values) - 1):
                thing_to_add.append(self.dataframe.column_values[j][i])
            a_matrix.append(thing_to_add)
        a_matrix = Matrix(a_matrix)

        a_transpose = a_matrix.transpose()
        a_transpose_times_a_matrix = a_transpose.matrix_multiply(a_matrix)
        inverse_of_a_transpose_times_a_matrix = a_transpose_times_a_matrix.inverse()
        a_pseudoinverse = inverse_of_a_transpose_times_a_matrix.matrix_multiply(a_transpose)

        right_side_no_matrix = [[num] for num in self.dataframe.data_dict[self.dependent_variable]]
        right_side = a_pseudoinverse.matrix_multiply(Matrix(right_side_no_matrix))

        coefficients_dict = {}
        for i in range(len(right_side.elements)):
            if i == 0:
                key = 'constant'
            else:
                key = self.dataframe.column_keys[i - 1]
            coefficients_dict[key] = [row[0] for row in right_side.elements][i]
        
        return coefficients_dict
    
    def predict(self, this_dict):

        x_list = list(this_dict.values())
        coefficients = list(self.coefficients.values())
        
        ans = coefficients[0]
        for i in range(len(coefficients) - 1):
            ans += x_list[i] * coefficients[i + 1]

        return ans