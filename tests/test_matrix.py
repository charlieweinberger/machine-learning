import sys
sys.path.append('src')
from matrix import Matrix

"""

print("\nAssignment 6-1\n")

print("Printing elements...")
A = Matrix([[1, 3], [2, 4]])
assert A.elements == [[1, 3], [2, 4]], A.elements
print("PASSED")

print("Testing method \"copy\"...")
B = A.copy()
A = 'resetting A to a string'
assert B.elements == [[1, 3], [2, 4]], B.elements
print("PASSED")

print("Testing method \"add\"...")
C = Matrix([[1, 0], [2, -1]])
D = B.add(C)
assert D.elements == [[2, 3], [4, 3]], D.elements
print("PASSED")

print("Testing method \"subtract\"...")
E = B.subtract(C)
assert E.elements == [[0,3], [0,5]], E.elements
print("PASSED")

print("Testing method \"scalar_multiply\"...")
F = B.scalar_multiply(2)
assert F.elements == [[2,6], [4,8]], F.elements
print("PASSED")


print("Testing method \"matrix_multiply\"...")
G = B.matrix_multiply(C)
assert G.elements == [[7,-3], [10,-4]], G.elements
print("PASSED")

print("\nAssignment 7-1\n")

print("Testing \"(num_rows, num_cols)\"...")
A = Matrix([[ 1, 0, 2, 0, 3],
            [ 0, 4, 0, 5, 0],
            [ 6, 0, 7, 0, 8],
            [-1,-2,-3,-4,-5]])
assert (A.num_rows, A.num_cols) == (4, 5), (A.num_rows, A.num_cols)
print("PASSED")

print("Testing method \"transpose\"...")
A_transpose = A.transpose()
assignment_7_1_answer_1 = [[ 1,  0,  6, -1],
                [ 0,  4,  0, -2],
                [ 2,  0,  7, -3],
                [ 0,  5,  0, -4],
                [ 3,  0,  8, -5]]
assert A_transpose.elements == assignment_7_1_answer_1, A_transpose.elements
print("PASSED")

print("Testing method \"matrix_multiply\"...")
B = A_transpose.matrix_multiply(A)
assignment_7_1_answer_2 = [[38,  2, 47,  4, 56],
                [ 2, 20,  6, 28, 10],
                [47,  6, 62, 12, 77],
                [ 4, 28, 12, 41, 20],
                [56, 10, 77, 20, 98]]
assert B.elements == assignment_7_1_answer_2, B.elements
print("PASSED")

print("Testing method \"scalar_multiply\"...")
C = B.scalar_multiply(0.1)
assignment_7_1_answer_3 = [[3.8,  .2, 4.7,  .4, 5.6],
                [ .2, 2.0,  .6, 2.8, 1.0],
                [4.7,  .6, 6.2, 1.2, 7.7],
                [ .4, 2.8, 1.2, 4.1, 2.0],
                [5.6, 1.0, 7.7, 2.0, 9.8]]
assert C.elements == assignment_7_1_answer_3, C.elements
print("PASSED")

print("Testing method \"subtract\"...")
D = B.subtract(C)
assignment_7_1_answer_4 = [[34.2, 1.8, 42.3, 3.6, 50.4],
                [ 1.8, 18. ,  5.4, 25.2,  9. ],
                [42.3,  5.4, 55.8, 10.8, 69.3],
                [ 3.6, 25.2, 10.8, 36.9, 18. ],
                [50.4,  9. , 69.3, 18. , 88.2]]
assert D.elements == assignment_7_1_answer_4, D.elements
print("PASSED")

print("Testing method \"add\"...")
E = D.add(C)
assignment_7_1_answer_5 = [[38,  2, 47,  4, 56],
                [ 2, 20,  6, 28, 10],
                [47,  6, 62, 12, 77],
                [ 4, 28, 12, 41, 20],
                [56, 10, 77, 20, 98]]
assert E.elements == assignment_7_1_answer_5, E.elements
print("PASSED")

print("Testing method \"is_equal\"...")
assert (E.is_equal(B), E.is_equal(C)) == (True, False), (E.is_equal(B), E.is_equal(C))
print("PASSED")

"""

print("\nAssignemnt 8-1\n")

print("Testing helper method \"get_pivot_row\" on input \"0\"...")
A = Matrix(elements = [[0, 1, 2],
                       [3, 6, 9],
                       [2, 6, 8]])
assert A.get_pivot_row(0) == 1, A.get_pivot_row(0)
print("PASSED")

print("Testing helper method \"swap_rows\" on inputs \"(0, 1)\"...")
A.swap_rows(0, 1)
assignment_8_1_answer_1 = [[3, 6, 9],
                           [0, 1, 2],
                           [2, 6, 8]]
assert A.elements == assignment_8_1_answer_1, A.elements
print("PASSED")

print("Testing helper method \"normalize_row\" on input \"0\"...")
A.normalize_row(0)
assignment_8_1_answer_2 = [[1, 2, 3],
                           [0, 1, 2],
                           [2, 6, 8]]
assert A.elements == assignment_8_1_answer_2, A.elements
print("PASSED")

print("Testing helper method \"clear_below\" on input \"0\"...")
A.clear_below(0)
assignment_8_1_answer_3 = [[1, 2, 3],
                           [0, 1, 2],
                           [0, 2, 2]]
assert A.elements == assignment_8_1_answer_3, A.elements
print("PASSED")

print("Testing helper method \"get_pivot_row\" on input \"1\"...")
assert A.get_pivot_row(1) == 1, A.get_pivot_row(1)
print("PASSED")

print("Testing helper method \"normalize_row\" on input \"1\"...")
A.normalize_row(1)
assignment_8_1_answer_4 = [[1, 2, 3],
                           [0, 1, 2],
                           [0, 2, 2]]
assert A.elements == assignment_8_1_answer_4, A.elements
print("PASSED")

print("Testing helper method \"clear_below\" on input \"1\"...")
A.clear_below(1)
assignment_8_1_answer_5 = [[1, 2, 3],
                           [0, 1, 2],
                           [0, 0, -2]]
assert A.elements == assignment_8_1_answer_5, A.elements
print("PASSED")

print("Testing helper method \"get_pivot_row\" on input \"2\"...")
assert A.get_pivot_row(2) == 2, A.get_pivot_row(2)
print("PASSED")

print("Testing helper method \"normalize_row\" on input \"2\"...")
A.normalize_row(2)
assignment_8_1_answer_6 = [[1, 2, 3],
                           [0, 1, 2],
                           [0, 0, 1]]
assert A.elements == assignment_8_1_answer_6, A.elements
print("PASSED")

print("Testing helper method \"clear_above\" on input \"2\"...")
A.clear_above(2)
assignment_8_1_answer_7 = [[1, 2, 0],
                           [0, 1, 0],
                           [0, 0, 1]]
assert A.elements == assignment_8_1_answer_7, A.elements
print("PASSED")


print("Testing helper method \"clear_above\" on input \"1\"...")
A.clear_above(1)
assignment_8_1_answer_8 = [[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]]
assert A.elements == assignment_8_1_answer_8, A.elements
print("PASSED")