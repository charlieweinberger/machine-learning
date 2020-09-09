import sys
sys.path.append('src')
from matrix import Matrix

print("Printing elements...")
A = Matrix([[1, 3], [2, 4]])
assert A.elements == [[1, 3], [2, 4]], "A.elements == \"{}\"".format(A.elements)
print("PASSED")

print("Testing method \"copy\"...")
B = A.copy()
A = 'resetting A to a string'
assert B.elements == [[1,3], [2,4]]
print("PASSED")

print("Testing method \"add\"...")
C = Matrix([[1,0], [2,-1]])
D = B.add(C)
assert D.elements == [[2,3], [4,3]]
print("PASSED")

print("Testing method \"subtract\"...")
E = B.subtract(C)
assert E.elements == [[0,3], [0,5]]
print("PASSED")

print("Testing method \"scalar_multiply\"...")
F = B.scalar_multiply(2)
assert F.elements == [[2,6], [4,8]]
print("PASSED")


print("Testing method \"matrix_multiply\"...")
G = B.matrix_multiply(C)
assert G.elements == [[7,-3], [10,-4]]
print("PASSED")