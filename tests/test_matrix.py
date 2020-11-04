import sys
sys.path.append('src')
from matrix import Matrix

A = Matrix([[1, 1, 0],
            [2, -1, 0],
            [0, 0, 3]])
assert A.exponent(3).elements == [
                                  [3, 3, 0],
                                  [6, -3, 0],
                                  [0, 0, 27]
                                 ], A.exponent(3).elements

A = Matrix(
    [[1,0,2,0,3],
    [0,4,0,5,0],
    [6,0,7,0,8],
    [-1,-2,-3,-4,-5]])

A_t = A.transpose()
ans = [[1,  0,  6, -1], [0,  4,  0, -2], [2,  0,  7, -3], [0,  5,  0, -4], [3,  0,  8, -5]]
assert A_t.elements == ans, A_t.elements

B = A_t @ A
ans = [[38,  2, 47,  4, 56],
 [ 2, 20,  6, 28, 10],
 [47,  6, 62, 12, 77],
 [ 4, 28, 12, 41, 20],
 [56, 10, 77, 20, 98]]
assert B.elements == ans, B.elements

print("passed 1")

C =  B * 0.1
ans = [[3.8,  .2, 4.7,  .4, 5.6],
 [ .2, 2.0,  .6, 2.8, 1.0],
 [4.7,  .6, 6.2, 1.2, 7.7],
 [ .4, 2.8, 1.2, 4.1, 2.0],
 [5.6, 1.0, 7.7, 2.0, 9.8]]
assert C.elements == ans, C.elements

print("passed 2")

D = B - C
ans = [[34.2,  1.8, 42.3,  3.6, 50.4],
 [ 1.8, 18. ,  5.4, 25.2,  9. ],
 [42.3,  5.4, 55.8, 10.8, 69.3],
 [ 3.6, 25.2, 10.8, 36.9, 18. ],
 [50.4,  9. , 69.3, 18. , 88.2]]
assert D.elements == ans, D.elements

print("passed 3")

E = D + C
ans = [[38,  2, 47,  4, 56],
 [ 2, 20,  6, 28, 10],
 [47,  6, 62, 12, 77],
 [ 4, 28, 12, 41, 20],
 [56, 10, 77, 20, 98]]
assert E.elements == ans, E.elements

print("passed 4")

assert (E == B) == True, E == B

print("passed 5")

assert (E == C) == False, E == C

print("passed all")