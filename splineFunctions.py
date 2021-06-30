from scipy.optimize import minimize_scalar
import numpy as np


def dist2spline(x, spline, t):
    try:
        x_s = spline.evaluate_single(t)
        return np.linalg.norm(x - x_s)
    except Exception as e:
        print(e)


def project(x, spline):
    res = minimize_scalar(lambda t: dist2spline(x, spline, t), bounds=np.array([0, 1]), method='bounded')
    return res['x']
