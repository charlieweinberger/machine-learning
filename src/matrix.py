# copy, add, and subtract, scalar_multiply, and matrix_multiply

class Matrix():
    def __init__(self, elements):   
        self.elements = elements

    def copy(self):
        return Matrix(self.elements)

    def add(self, matrix_to_add):
        ans = Matrix(self.elements)
        
        here_1 = self.elements[0][0] + matrix_to_add.elements[0][0]
        here_2 = self.elements[0][1] + matrix_to_add.elements[0][1]
        here_3 = self.elements[1][0] + matrix_to_add.elements[1][0]
        here_4 = self.elements[1][1] + matrix_to_add.elements[1][1]

        ans.elements = [[here_1, here_2],
                        [here_3, here_4]]

        return ans
    
    def subtract(self, matrix_to_subtract):
        ans = Matrix(self.elements)
        
        here_1 = self.elements[0][0] - matrix_to_subtract.elements[0][0]
        here_2 = self.elements[0][1] - matrix_to_subtract.elements[0][1]
        here_3 = self.elements[1][0] - matrix_to_subtract.elements[1][0]
        here_4 = self.elements[1][1] - matrix_to_subtract.elements[1][1]

        ans.elements = [[here_1, here_2],
                        [here_3, here_4]]

        return ans
    
    def scalar_multiply(self, scalar):
        ans = Matrix(self.elements)
        
        here_1 = scalar * self.elements[0][0]
        here_2 = scalar * self.elements[0][1]
        here_3 = scalar * self.elements[1][0]
        here_4 = scalar * self.elements[1][1]

        ans.elements = [[here_1, here_2],
                        [here_3, here_4]]
        
        return ans
    
    def matrix_multiply(self, matrix_to_multiply):
        ans = Matrix(self.elements)
        
        here_1 = self.elements[0][0] * matrix_to_multiply.elements[0][0] + self.elements[0][1] * matrix_to_multiply.elements[1][0]
        here_2 = self.elements[0][0] * matrix_to_multiply.elements[0][1] + self.elements[0][1] * matrix_to_multiply.elements[1][1]
        here_3 = self.elements[1][0] * matrix_to_multiply.elements[0][0] + self.elements[1][1] * matrix_to_multiply.elements[1][0]
        here_4 = self.elements[1][0] * matrix_to_multiply.elements[0][1] + self.elements[1][1] * matrix_to_multiply.elements[1][1]

        ans.elements = [[here_1, here_2],
                        [here_3, here_4]]
        
        return ans