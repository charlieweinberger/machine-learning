# copy, add, subtract, scalar_multiply, matrix_multiply, transpose, is_equal, get_pivot_row, swap_rows, normalize_row, first_nonzero_entry_index, row_reduct, clear_below, clear_above

class Matrix():
    def __init__(self, elements):
        self.elements = elements
        self.num_rows = len(self.elements)
        self.num_cols = len(self.elements[0])

    def copy(self):
        return Matrix(self.elements)

    def add(self, matrix_to_add):
        ans = []
        
        for row_index in range(self.num_rows):
            ans.append([])
            for col_index in range(self.num_cols):
                ans[row_index].append(self.elements[row_index][col_index] + matrix_to_add.elements[row_index][col_index]) 

        return Matrix(ans)
    
    def subtract(self, matrix_to_subtract):
        ans = []
        
        for row_index in range(self.num_rows):
            ans.append([])
            for col_index in range(self.num_cols):
                ans[row_index].append(self.elements[row_index][col_index] - matrix_to_subtract.elements[row_index][col_index]) 

        return Matrix(ans)
    
    def scalar_multiply(self, scalar):
        ans = []
        
        for row_index in range(self.num_rows):
            ans.append([])
            for col_index in range(self.num_cols):
                ans[n].append(round(scalar * self.elements[row_index][col_index], 4)) 

        return Matrix(ans)
    
    def matrix_multiply(self, matrix_to_multiply):
        ans = []

        for num in range(self.num_rows):
            ans.append([])
            for num2 in range(self.num_rows):
                
                row = self.elements[num]
                horizontal_col = [thing[num2] for thing in matrix_to_multiply.elements]

                dot_product = 0
                for index in range(self.num_cols):
                        dot_product += row[index] * horizontal_col[index]
              
                ans[num].append(dot_product)

        return Matrix(ans)

    def transpose(self):
        return Matrix([[self.elements[row_index][col_index] for row_index in range(self.num_rows)] for col_index in range(self.num_cols)])

    def is_equal(self, matrix_to_compare):
        ans = True
        for col_index in range(self.num_cols):
            for row_index in range(self.num_rows):
                if self.elements[row_index][col_index] != matrix_to_compare.elements[row_index][col_index]:
                    ans = False
        return ans

    def get_pivot_row(self, col_index):
        for row in self.elements:
            if (row[col_index] != 0) and (all(row[elem] == 0 for elem in range(col_index)):
                return self.elements.index(row)
        return None
    
    def swap_rows(self, row_index1, row_index2):
        self.elements[row_index1], self.elements[row_index2] = self.elements[row_index2], self.elements[row_index1] 
        return self.elements
    
    def normalize_row(self, row_index): 
        row = self.elements[row_index]

        is_first_nonzero = True
        for num in range(len(row)):
            if row[num] != 0:
                for num2 in range(num):
                    if row[num2] != 0:
                        is_first_nonzero = False
                if is_first_nonzero:
                    dividing_num = row[num]

        self.elements[row_index] = [num / dividing_num for num in row]

        return self.elements
    
    def first_nonzero_entry_index(self, row_index):
        row = self.elements[row_index]
        first_nonzero_entry_index = 0
        for num in row:
            if num == 0:
                first_nonzero_entry_index += 1
            else:
                break
        return first_nonzero_entry_index

    def row_reduct(self, row2, row1, col_index): # makes row2[col_index] == 0
        multiplier = row2[col_index] / row1[col_index]
        return [row2[i] - multiplier * row1[i] for i in range(len(row1))]

    def clear_below(self, row_index):
        row = self.elements[row_index]
        j = self.first_nonzero_entry_index(row_index)

        for row_index_below in range(row_index + 1, len(self.elements)):
            row_below = self.elements[row_index_below]
            self.elements[row_index_below] = self.row_reduct(row_below, row, j)
        
        return self.elements

    def clear_above(self, row_index):
        row = self.elements[row_index]
        j = self.first_nonzero_entry_index(row_index)

        for row_index_below in range(row_index):
            row_below = self.elements[row_index_below]
            self.elements[row_index_below] = self.row_reduct(row_below, row, j)
        
        return self.elements