import casadi as ca
import numpy as np

import os

import urdf2casadi.urdfparser as u2c

robot = u2c.URDFparser()
urdf_file = os.path.dirname(os.path.abspath(__file__)) + "/panda.urdf"
robot.from_file(urdf_file)

def pandaFk(q, n):
    relevantLinks = [0, 3, 4, 5, 6, 7, 8, 9]
    link_names = ['panda_link' + str(i) for i in relevantLinks]
    root = "panda_link0"
    tip = link_names[n]
    fk = robot.get_forward_kinematics(root, tip, q)["T_fk"][0:3, 3]
    return fk


q_ca = ca.SX.sym('q_ca', 7)
fks = []
for i in range(8):
    fks.append(pandaFk(q_ca, i))
fks_fun = ca.Function('fk', [q_ca], fks)

def pandaNumpyFk(q, n):
    return np.array(fks_fun(q)[n])[:, 0]


valid_types = ["pointMass", "planarArm", "panda"]


class InvalidRobotTypeError(Exception):
    pass


class ForwardKinematics(object):
    def __init__(self, robot_type="planarArm"):
        if robot_type not in valid_types:
            raise InvalidRobotTypeError(
                "No forward kinematics available for robot type %s" % robot_type
            )
        self._robot_type = robot_type

    def getFk(self, q, n, positionOnly=False):
        if isinstance(q, ca.SX):
            return self.casadiFk(q, n, positionOnly)
        elif isinstance(q, np.ndarray):
            return self.numpyFk(q, n, positionOnly)

    def casadiFk(self, q, n, positionOnly):
        if self._robot_type == "planarArm":
            if positionOnly:
                return casadiFk(q, n)[0:2]
            else:
                return casadiFk(q, n)
        elif self._robot_type == "pointMass":
            if n > 0:
                return q
            else:
                return np.zeros(2)
        elif self._robot_type == 'panda':
            if positionOnly:
                return pandaFk(q, n)[0:3]
            else:
                return pandaFk(q, n)

    def numpyFk(self, q, n, positionOnly):
        if self._robot_type == "planarArm":
            if positionOnly:
                return numpyFk(q, n)[0:2]
            else:
                return numpyFk(q, n)
        elif self._robot_type == "pointMass":
            if n > 0:
                return q
            else:
                return np.zeros(2)
        elif self._robot_type == 'panda':
            if positionOnly:
                return pandaNumpyFk(q, n)[0:3]
            else:
                return pandaNumpyFk(q, n)


def casadiFk(q, n, endlink=0.0):
    fk = ca.SX(np.array([0.0, 0.2, q[0]]))
    fk = ca.SX(np.array([0.0, 0.0, q[0]]))
    for i in range(1, n + 1):
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
    for i in range(2, n + 1):
        fk[0] += ca.cos(fk[2]) * 1.0
        fk[1] += ca.sin(fk[2]) * 1.0
        if i < q.size(1):
            fk[2] += q[i]
    return fk

def numpyFk(q, n, endlink=0):
    fk = np.array([0.0, 0.2, q[0]])
    fk = np.array([0.0, 0.0, q[0]])
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
    fk = ForwardKinematics(robot_type="panda")
    q_ca = ca.SX.sym('AAAAAA', 7)
    q = np.array([0.0, 0.0, 0.0, -1.501, 0.0, 1.8675, 0.0])
    q = np.array([-0.01026582, -0.28908, 0.00922652, -1.3468, -0.026000, 2.074019, 0.06062268])
    q2 = np.array([-0.01026582, -0.28908, 0.00922652, -1.3468, -0.026000, 2.574019, -0.06062268])
    #q = np.array([-0.0075, -0.178083, 0.0076, -1.4393, -0.0217, 1.9901, 0.0538])
    #q = np.array([0.0798, -0.1049, 0.1070, -1.2753, -0.0086, 2.0625, 0.0541])
    for i in range(8):
        fki = fk.getFk(q_ca, i, positionOnly=True)
        fki_np = fk.getFk(q, i, positionOnly=True)
        fki_np2 = fk.getFk(q2, i, positionOnly=True)
        # print(fki)
        print(fki_np)
        #print(fki_np2)
