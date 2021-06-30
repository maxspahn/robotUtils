import csv
import numpy as np

class TrajectorySaver(object):

    def __init__(self, fileName):
        self._fileName = fileName

    def save(self, n_steps, qs, dt):
        with open(self._fileName, mode='w') as file:
            csv_writer = csv.writer(file, delimiter=';')
            for i in range(n_steps):
                qs_i = [i * dt]
                for q in qs:
                    for q_j in q[i]:
                        qs_i.append(q_j)
                csv_writer.writerow(qs_i)

class SolverTimesSaver(object):

    def __init__(self, fileName):
        self._fileName = fileName

    def save(self, n_steps, sts, dt):
        with open(self._fileName, mode='w') as file:
            csv_writer = csv.writer(file, delimiter=';')
            for i in range(n_steps):
                data_i = [i * dt]
                for st in sts:
                    data_i.append(st[i])
                csv_writer.writerow(data_i)

class CircleSaver(object):
    def __init__(self, x0, y0, r, fileName):
        self._fileName = fileName
        theta = np.arange(-np.pi, np.pi + np.pi/100, np.pi/100)
        self._x = x0 + r * np.cos(theta)
        self._y = y0 + r * np.sin(theta)

    def save(self):
        with open(self._fileName, mode='w') as file:
            csv_writer = csv.writer(file, delimiter=';')
            for i in range(len(self._x)):
                csv_writer.writerow([self._x[i], self._y[i]])

class SplineSaver(object):
    def __init__(self, spline, fileName):
        self._fileName = fileName
        points = np.array(spline.evalpts)
        self._x = points[:, 0]
        self._y = points[:, 1]

    def save(self):
        with open(self._fileName, mode='w') as file:
            csv_writer = csv.writer(file, delimiter=';')
            for i in range(len(self._x)):
                csv_writer.writerow([self._x[i], self._y[i]])

class TimedSplineSaver(object):
    def __init__(self, spline, fileName, T):
        self._fileName = fileName
        points = np.array(spline.evalpts)
        n = len(points)
        self._dt = T/n
        self._x = points[:, 0]
        self._y = points[:, 1]
        self._z = points[:, 2]

    def save(self):
        with open(self._fileName, mode='w') as file:
            csv_writer = csv.writer(file, delimiter=';')
            for i in range(len(self._x)):
                csv_writer.writerow([self._dt * i, self._x[i], self._y[i], self._z[i]])
