class GradientDescent():

    def __init__(self, f, initial_point):
        self.f = f
        self.point = initial_point
        self.num_vars = self.f.__code__.co_argcount

    def compute_gradient(self, delta):

        partials = []
        for i in range(self.num_vars):

            point_plus = []
            point_minus = []

            for j in range(len(self.point)):
                if j == i:
                    point_plus .append(self.point[j] + 0.5 * delta)
                    point_minus.append(self.point[j] - 0.5 * delta)
                else:
                    point_plus .append(self.point[j])
                    point_minus.append(self.point[j])
            
            partial = (self.f(*point_plus) - self.f(*point_minus)) / delta
            partials.append(partial)
            
        return partials
    
    def descend(self, alpha, delta, num_steps):

        for a in range(num_steps):
            for i in range(self.num_vars):
                self.point[i] -= alpha * self.compute_gradient(delta)[i]