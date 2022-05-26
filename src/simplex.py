class SimplexMethod():

    def __init__(self, matrix):
        self.matrix = matrix
        self.max = 0
        self.set_up_matrix()
    
    def set_up_matrix(self):
        base = [0] * (len(self.matrix) - 1)
        for i in range(len(self.matrix) - 1):
            copy = base.copy()
            copy[i] = 1
            self.matrix[i][-1:-1] = copy
        self.matrix[-1][-1:-1] = base.copy()

    def solve(self):
        while not self.check_if_solved():
            self.run_one_iteration()
        return -self.matrix[-1][-1]
    
    def run_one_iteration(self):
        col_to_change = self.get_col_to_change()
        row_to_change = self.get_row_to_change(col_to_change)
        self.reduce_row(col_to_change, row_to_change)
        self.reduce_other_rows(col_to_change, row_to_change)

    def get_col_to_change(self):
        return self.matrix[-1].index(max(self.matrix[-1]))

    def get_row_to_change(self, col_to_change):
        constraints = [self.matrix[i][-1] / self.matrix[i][col_to_change] for i in range(len(self.matrix) - 1)]
        return constraints.index(min(elem for elem in constraints if elem >= 0))

    def check_if_solved(self):
        for elem in self.matrix[-1]:
            if elem > 0:
                return False
        return True
    
    def reduce_row(self, col_to_change, row_to_change):
        const = self.matrix[row_to_change][col_to_change]
        for i in range(len(self.matrix[row_to_change])):
            self.matrix[row_to_change][i] /= const

    def reduce_other_rows(self, col_to_change, row_to_change):
        for i in range(len(self.matrix)):
            if i != row_to_change:
                const = self.matrix[i][col_to_change]
                for j in range(len(self.matrix[i])):
                    self.matrix[i][j] -= const * self.matrix[row_to_change][j]