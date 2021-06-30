from robotSaver import SplineSaver, TimedSplineSaver

from geomdl import BSpline, utilities

crv = BSpline.Curve()
crv.degree = 2
crv.ctrlpts = [[3.1414, -1.79499], [0.0, 0.0], [3.1, 2.0]]
crv.ctrlpts = [[0.40443, -0.4163, 0.6897], [0.0, 0.0, 0.6], [0.55, 0.4, 0.5]]
crv.knotvector = utilities.generate_knot_vector(crv.degree, len(crv.ctrlpts))

T = 20

cv1 = TimedSplineSaver(crv, 'spline.csv', T)
cv1.save()





