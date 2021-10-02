class GradientDescent():

    def __init__(self, f, initial_point):
        self.f = f
        self.point = initial_point
        self.num_vars = self.f.__code__.co_argcount

    def compute_gradient(self, delta):

        partials = []
        for i in range(self.num_vars):

            point_plus  = [(self.point[elem_index] + 0.5 * delta) if elem_index == i else self.point[elem_index] for elem_index in range(len(self.point))]
            point_minus = [(self.point[elem_index] - 0.5 * delta) if elem_index == i else self.point[elem_index] for elem_index in range(len(self.point))]
            
            partial = (self.f(*point_plus) - self.f(*point_minus)) / delta
            partials.append(partial)
            
        return partials
    
    def descend(self, alpha, delta, num_steps):

        for a in range(num_steps):
            for i in range(self.num_vars):
                self.point[i] -= alpha * self.compute_gradient(delta)[i]

########################################################################################

"""

def single_variable_function(x):
    return (x - 1)**2

def y(x, a, b):
    return a * Math.sin(b * x)

minimizer = GradientDescent(f=single_variable_function, initial_point=[0])
assert minimizer.point == [0], minimizer.point
assert minimizer.compute_gradient(delta=0.01) == [-2.000], minimizer.compute_gradient(delta=0.01)

minimizer.descend(alpha=0.001, delta=0.01, num_steps=1)
assert minimizer.point == [0.002], minimizer.point

"""

########################################################################################

import matplotlib.pyplot as plt
plt.style.use('bmh')
import sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor
from logistic_regressor import LogisticRegressor

arr = [(0.5, 2), (0.9, 0.9), (1, 0.3)]
df = DataFrame.from_array(arr, columns = ['x', 'y'])

reg = LogisticRegressor(df, dependent_variable='y', upper_bound=1)
reg.set_coefficients({'constant': 0.5, 'x': 0.5})

alpha = 0.01
delta = 0.01
num_steps = 2000
reg.gradient_descent(alpha, delta, num_steps)

print("\nreg.coefficients:", reg.coefficients)

x = [pair[0] for pair in arr]
y = [pair[1] for pair in arr]

lots_of_xs = [x/100 for x in range(100, 401)]
prediction = [reg.predict({'x':x}) for x in lots_of_xs]

plt.scatter(x, y, label="Actual", color="red")
plt.plot(lots_of_xs, prediction, label='Gradient descent')

plt.legend(loc='best')
plt.savefig('logistic_regressor_gradient_descent.png')