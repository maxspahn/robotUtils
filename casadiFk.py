import casadi as ca
import numpy as np

def casadiFk(q, n, endlink=0.0):
    fk = np.array([0.0, 0.2, q[0]])
    for i in range(1, n+1):
        fk[0] += ca.cos(fk[2]) * 1.0
        fk[1] += ca.sin(fk[2]) * 1.0
        if i < q.size(1):
            fk[2] += q[i]
    fk[0] += ca.cos(fk[2]) * endlink
    fk[1] += ca.sin(fk[2]) * endlink
    return fk

def casadiMobileFk(q, heightBase, n):
    fk = ca.vertcat(q[0], 0, 0)
    if n >= 1:
        fk += np.array([0.0, heightBase, q[1]])
    for i in range(2, n+1):
        fk[0] += ca.cos(fk[2]) * 1.0
        fk[1] += ca.sin(fk[2]) * 1.0
        if i < q.size(1):
            fk[2] += q[i]
    return fk


if __name__ == "__main__":
    q = ca.SX.sym("q", 3)
    heightBase = 1.5
    for i in range(4):
        print("---" , i , "---")
        print(casadiMobileFk(q, 1.0,   i))
