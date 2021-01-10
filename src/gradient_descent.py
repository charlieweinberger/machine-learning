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