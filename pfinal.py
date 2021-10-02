import Math

'''

Write a python program that fits the function y = asin(bx) to the data points [(0.5,2), (0.9,0.9), (1,0.3)] by minimizing the residual sum squares using gradient descent, using the initial guess a=1, b=1. Have your program periodically print out the parameters and the residual sum squares. Choose the step size (in your gradient estimation) and learning rate (in your parameter updates) so that the parameters converge quickly.

'''

def y(x, a, b):
    return a * Math.sin(b * x)

data = [(0.5, 2), (0.9, 0.9), (1, 0.3)]