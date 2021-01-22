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
                dependent_variable_values = self.dataframe.data_dict[self.dependent_variable]
                
                if j_values != dependent_variable_values:
                    thing_to_add.append(j_values[i])
            
            a_matrix.append(thing_to_add)

        a_matrix = Matrix(a_matrix)

        a_transpose = a_matrix.transpose()
        a_transpose_times_a_matrix = a_transpose.matrix_multiply(a_matrix)
        inverse_of_a_transpose_times_a_matrix = a_transpose_times_a_matrix.inverse()
        a_pseudoinverse = inverse_of_a_transpose_times_a_matrix.matrix_multiply(a_transpose)

        dependent_variable_values = self.dataframe.data_dict[self.dependent_variable]
        right_side_no_matrix = [[num] for num in dependent_variable_values]
        right_side = a_pseudoinverse.matrix_multiply(Matrix(right_side_no_matrix))

        coefficients_list = ['constant']
        for key in self.dataframe.column_keys:
            if key != self.dependent_variable:
                coefficients_list.append(key)

        coefficients_dict = {'constant': right_side.elements[0][0]}
        for i in range(len(right_side.elements)):
            key = coefficients_list[i]
            coefficients_dict[key] = right_side.elements[i][0]

        return coefficients_dict
    
    def predict(self, this_dict):

        coefficients_keys = list(self.coefficients.keys())
        coefficients = list(self.coefficients.values())

        ans = coefficients[0]
        for i in range(1, len(coefficients)):
            key = coefficients_keys[i]
            if key != self.dependent_variable and '*' not in key:
                ans += self.coefficients[key] * this_dict[key]
        
        interaction_terms = [key for key in coefficients_keys if '*' in key]
        interaction_terms_list = [[term, term.split(' * ')] for term in interaction_terms]

        for term_list in interaction_terms_list:
            coefficient_key = term_list[0]
            coefficient = self.coefficients[coefficient_key]

            interaction_term_value = coefficient
            for term in term_list[1]:
                interaction_term_value *= this_dict[term]
            
            ans += interaction_term_value
        
        return ans