# copy, add, subtract, scalar_multiply, matrix_multiply, transpose, is_equal, row_reduct, get_pivot_row, swap_rows, normalize_row, first_nonzero_entry_index, clear_below, clear_above, rref, augment, get_rows, get_cols, inverse, make_int, determinant, cofactor_method_determinant, exponent, overloads (matrix addition, matrix subtraction, scalar multiplication, matrix multiplication, equality, scalar multiplication w/ the scalar on the left, and exponents for matrices)

class Matrix():
    def __init__(self, elements):
        self.elements = elements
        self.num_rows = len(self.elements)
        self.num_cols = len(self.elements[0])

    def copy(self):
        return Matrix([[entry for entry in row] for row in self.elements])

    def add(self, matrix_to_add):
        c = self.copy()
        ans = []
        
        for row_index in range(c.num_rows):
            ans.append([])
            for col_index in range(c.num_cols):
                c_elems = c.elements[row_index][col_index]
                matrix_to_add_elems = matrix_to_add.elements[row_index][col_index]
                ans[row_index].append(c_elems + matrix_to_add_elems) 

        return Matrix(ans)

    def subtract(self, matrix_to_subtract):
        c = self.copy()
        ans = []
        
        for row_index in range(c.num_rows):
            ans.append([])
            for col_index in range(c.num_cols):
                c_elems = c.elements[row_index][col_index]
                matrix_to_subtract_elems = matrix_to_subtract.elements[row_index][col_index]
                ans[row_index].append(c_elems - matrix_to_subtract_elems)

        return Matrix(ans)

    def scalar_multiply(self, scalar):
        c = self.copy()
        ans = []
        
        for row_index in range(c.num_rows):
            ans.append([])
            for col_index in range(c.num_cols):
                c_elems = c.elements[row_index][col_index]
                rounded = round(scalar * c_elems, 4)
                ans[row_index].append(rounded) 

        return Matrix(ans)

    def matrix_multiply(self, matrix_to_multiply):
        c = self.copy()
        c2 = matrix_to_multiply.copy()
        ans = []

        for num in range(c.num_rows):
            ans.append([])
            for num2 in range(c2.num_cols):
                
                row = c.elements[num]
                horizontal_col = [thing[num2] for thing in c2.elements]

                dot_product = 0
                for index in range(c.num_cols):
                    dot_product += row[index] * horizontal_col[index]
              
                ans[num].append(dot_product)

        return Matrix(ans)
    
    def transpose(self):
        c = self.copy()
        return Matrix([[c.elements[row_index][col_index] for row_index in range(c.num_rows)] for col_index in range(c.num_cols)])

    def is_equal(self, matrix_to_compare):
        ans = True
        for col_index in range(self.num_cols):
            for row_index in range(self.num_rows):
                if self.elements[row_index][col_index] != matrix_to_compare.elements[row_index][col_index]:
                    ans = False
        return ans
    
    def row_reduct(self, row1, row2, col_index): # makes row2[col_index] == 0
        multiplier = row2[col_index] / row1[col_index]
        return [row2[i] - multiplier * row1[i] for i in range(len(row1))]

    def get_pivot_row(self, col_index):
        for row in self.elements:
            if (row[col_index] != 0) and all(row[elem] == 0 for elem in range(col_index)):
                return self.elements.index(row)
        return None
    
    def swap_rows(self, row_index1, row_index2):
        c = self.copy()
        c.elements[row_index1], c.elements[row_index2] = c.elements[row_index2], c.elements[row_index1] 
        return c
    
    def normalize_row(self, row_index): 
        c = self.copy()
        row = c.elements[row_index]

        is_first_nonzero = True
        for num in range(len(row)):
            if row[num] != 0:
                for num2 in range(num):
                    if row[num2] != 0:
                        is_first_nonzero = False
                if is_first_nonzero:
                    dividing_num = row[num]

        c.elements[row_index] = [num / dividing_num for num in row]

        return c
    
    def first_nonzero_entry_index(self, row_index):
        row = self.elements[row_index]
        first_nonzero_entry_index = 0
        for num in row:
            if num == 0:
                first_nonzero_entry_index += 1
            else:
                break
        return first_nonzero_entry_index

    def clear_below(self, row_index):
        c = self.copy()
        row = c.elements[row_index]
        j = c.first_nonzero_entry_index(row_index)

        for row_index_below in range(row_index + 1, c.num_rows):
            c.elements[row_index_below] = c.row_reduct(row, c.elements[row_index_below], j)
        
        return c

    def clear_above(self, row_index):
        c = self.copy()
        row = c.elements[row_index]
        j = c.first_nonzero_entry_index(row_index)

        for row_index_below in range(row_index):
            row_below = c.elements[row_index_below]
            c.elements[row_index_below] = c.row_reduct(row, row_below, j)
        
        return c
    
    def rref(self):
        c = self.copy()
        row_index = 0
        for col_index in range(c.num_cols):
            
            pivot_row = c.get_pivot_row(col_index)
            if pivot_row != None:
                
                if pivot_row != row_index:
                    c = c.swap_rows(pivot_row, row_index)

                c = c.normalize_row(row_index)
                c = c.clear_below(row_index)
                c = c.clear_above(row_index)

                row_index += 1

        return c
    
    def get_rows(self, row_nums):
        c = self.copy()
        ans = [[c.elements[row_index] for row_index in range(c.num_rows) if row_num == row_index][0] for row_num in row_nums]
        return Matrix(ans)
    
    def get_columns(self, col_nums):
        c = self.copy()
        final_ans = []
        for row_index in range(c.num_rows):
            ans_set = []
            for num_index in range(c.num_cols):
                for col_num in col_nums:
                    if col_num == num_index:
                        ans_set.append(c.elements[row_index][num_index])
            final_ans.append(ans_set)
        return Matrix(final_ans)
    
    def augment(self, other_matrix):
        c = self.copy()
        co = other_matrix

        for row_index in range(c.num_rows):
            c.elements[row_index] += co[row_index]
        return c
    
    def inverse(self):
        
        c = self.copy()

        if c.num_rows != c.num_cols:
            return "Error: cannot invert a non-square matrix"

        identity_matrix = Matrix([[1 if num == num2 else 0 for num2 in range(c.num_cols)] for num in range(c.num_rows)])

        c_augmented = c.augment(identity_matrix.elements)
        c_rref_augmented = c_augmented.rref()

        inverse_ans = [[c_rref_augmented.elements[row_index][col_index] for col_index in range(self.num_cols, c_rref_augmented.num_cols)] for row_index in range(c_rref_augmented.num_rows)]

        should_be_identity_matrix = [[int(c_rref_augmented.elements[row_index][col_index]) for col_index in range(self.num_cols)] for row_index in range(c_rref_augmented.num_rows)]

        if should_be_identity_matrix != identity_matrix.elements:
            return "Error: cannot invert a singular matrix"

        return Matrix(inverse_ans)

    def make_int(self, num):
        if type(num) == float and int(str(num).split(".")[1]) == 0:
            return int(str(num).split(".")[0])
        else:
            return num

    def determinant(self):
        c = self.copy()
        identity_matrix = Matrix([[1 if num == num2 else 0 for num2 in range(c.num_cols)] for num in range(c.num_rows)])
        
        if c.num_rows != c.num_cols:
            return "Error: cannot take determinant of a non-square matrix"

        num_to_multiply_by = 1
        num_row_swaps = 0

        # rref
        row_index = 0
        for col_index in range(c.num_cols):

            pivot_row = c.get_pivot_row(col_index)
            if pivot_row != None:
                
                if pivot_row != row_index:
                    c = c.swap_rows(pivot_row, row_index)
                    num_row_swaps += 1

                # normalize_row
                row = c.elements[row_index]
                is_first_nonzero = True

                for num in range(len(row)):
                    if row[num] != 0:
                        for num2 in range(num):
                            if row[num2] != 0:
                                is_first_nonzero = False
                        if is_first_nonzero:
                            dividing_num = row[num]

                num_to_multiply_by *= dividing_num
                c.elements[row_index] = [num / dividing_num for num in row]

                c = c.clear_below(row_index)
                c = c.clear_above(row_index)

                row_index += 1

        # make numbers integers
        for row_index in range(c.num_rows):
            for num_index in range(c.num_cols):                
                c.elements[row_index][num_index] = c.make_int(c.elements[row_index][num_index])
        
        determinant = c.make_int(num_to_multiply_by) * ((-1) ** num_row_swaps)

        if c.elements != identity_matrix.elements:
            return 0
        else:
            return determinant
    
    def big_to_small_matrix(self, bad_row_index, bad_col_index):
        c = self.copy()

        small = []
        for row_index in range(c.num_rows):
            row = []
            for col_index in range(c.num_cols):
                if row_index != bad_row_index and col_index != bad_col_index:
                    row.append(c.elements[row_index][col_index])
            small.append(row)
        
        ans = [row for row in small if len(row) != 0]

        return Matrix(ans)

    def cofactor_method_determinant(self):
        c = self.copy()
        
        if c.num_rows != c.num_cols:
            return "Error: cannot take cofactor_method_determinant of a non-square matrix"

        if c.num_rows == 2:
            return (c.elements[0][0] * c.elements[1][1]) - (c.elements[0][1] * c.elements[1][0])
        else:
            ans = 0
            for col_index in range(c.num_cols):
                ans += (-1 ** col_index) * c.elements[0][col_index] * c.big_to_small_matrix(0, col_index).cofactor_method_determinant()
            return ans
    
    def exponent(self, num):
        c = self.copy()
        for i in range(num - 1):
            c = c.matrix_multiply(c)
        return c
    
    def __add__(self, matrix_to_add):
        return self.add(matrix_to_add)

    def __sub__(self, matrix_to_subtract):
        return self.subtract(matrix_to_subtract)

    def __mul__(self, scalar):
        return self.scalar_multiply(scalar)
    
    def __rmul__(self, scalar):
        return self.scalar_multiply(scalar)

    def __matmul__(self, matrix_to_multiply):
        return self.matrix_multiply(matrix_to_multiply)

    def __eq__(self, matrix_to_compare):
        return self.is_equal(matrix_to_compare)
    
    def __pow__(self, num):
        return self.exponent(num)