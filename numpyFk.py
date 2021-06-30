import numpy as np

def numpyFk(q, n, endlink=0):
    fk = np.array([0.0, 0.2, q[0]])
    for i in range(1, n+1):
        fk[0] += np.cos(fk[2]) * 1.0
        fk[1] += np.sin(fk[2]) * 1.0
        if i < len(q):
            fk[2] += q[i]
    fk[0] += np.cos(fk[2]) * endlink
    fk[1] += np.sin(fk[2]) * endlink
    return fk

def numpyMobileFk(q, heightBase, n):
    fk = np.array([q[0], 0.0, 0.0])
    if n >= 1:
        fk += np.array([0.0, heightBase, q[1]])
    for i in range(2, n+1):
        fk[0] += np.cos(fk[2]) * 1.0
        fk[1] += np.sin(fk[2]) * 1.0
        if i < (len(q)):
            fk[2] += q[i]
    return fk

if __name__ == "__main__":
    q = np.array([1.0, -np.pi/2.0, np.pi/2])
    heightBase = 1.5
    for i in range(4):
        print("---" , i , "---")
        print(numpyMobileFk(q,1.0,  i))
