import random
from random import random

import sys
sys.path.append('src')
from matrix import Matrix

test_matrix_elements = [[round(40 * (random() - 0.5), 3) for i in range(10)] for j in range(10)]
test_matrix = Matrix(test_matrix_elements)

print(test_matrix.elements)

determinant = test_matrix.determinant()
print("\ndeterminant:", determinant)

cofactor_method_determinant = test_matrix.cofactor_method_determinant()
print("cofactor_method_determinant:", cofactor_method_determinant)

"""

The rref method of conputing a determinant is much faster than the cofacter method. The rref method took less than a second, while the cofactor method took over two minutes, according to my timer. I would guess that this is because of the recursion if the cofactor method. To compute a 10 by 10 matrix, it has to compute 10 9 by 9 matrices, which means it has to compute 90 8 by 8 matrices, and so on. In the end, it has to compute 10!/2 (which equals 1,814,400) 2 by 2 matrices.

"""