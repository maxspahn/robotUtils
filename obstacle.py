import numpy as np
import casadi as ca

class Obstacle(object):

    def __init__(self, x, r):
        self._x = x
        self._r = r

    def r(self):
        return self._r

    def x(self, t=None):
        return self._x

    def toArray(self):
        return np.array([self._x[0], self._x[1], self._r])

class Obstacle3D(Obstacle):

    def __init__(self, x, r):
        super(Obstacle3D, self).__init__(x, r)

    def toArray(self):
        return np.array([self._x[0], self._x[1], self._x[2], self._r])

class DynamicObstacle(Obstacle):

    def __init__(self, x_fun, r):
        super(DynamicObstacle, self).__init__(x_fun, r)
        self._x_fun = x_fun

    def x(self, t):
        t_np = np.array([t])
        a = self._x_fun(t_np)
        return np.array(self._x_fun(t))[:, 0]

