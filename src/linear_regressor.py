import sys
sys.path.append('src')
from matrix import Matrix
from dataframe import DataFrame

class LinearRegressor():
    
    def __init__(self, dataframe, dependent_variable):
        self.dataframe = dataframe
        self.dependent_variable = dependent_variable
        self.coefficients = self.calculate_coefficients()
        self.function = lambda x : round(self.coefficients[0] + x * self.coefficients[1], 5)
    
    def copy(self):
        return LinearRegressor(self.dataframe, self.dependent_variable)
    
    def calculate_coefficients(self):

        print(self.dataframe.column_values[0])
        a_matrix = Matrix([[1, num] for num in self.dataframe.column_values[0]])
        a_transpose = a_matrix.transpose()
        a_transpose_times_a_matrix = a_transpose.matrix_multiply(a_matrix)
        inverse_of_a_transpose_times_a_matrix = a_transpose_times_a_matrix.inverse()
        a_pseudoinverse = inverse_of_a_transpose_times_a_matrix.matrix_multiply(a_transpose)

        right_side_no_matrix = [[num] for num in self.dataframe.data_dict[self.dependent_variable]]
        right_side = a_pseudoinverse.matrix_multiply(Matrix(right_side_no_matrix))

        ans = [[round(num, 5) for num in row][0] for row in right_side.elements]
        return ans
    
    def predict(self, hours_dict):
        c = self.copy()
        num_hours = list(hours_dict.values())[0]
        return c.function(num_hours)
        return self.coefficients[0] + num_hours * self.coefficients[1]