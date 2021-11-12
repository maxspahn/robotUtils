import casadi as ca
import numpy as np
import os

import urdf2casadi.urdfparser as u2c

robot = u2c.URDFparser()
urdf_file = os.path.dirname(os.path.abspath(__file__)) + "/panda.urdf"
robot.from_file(urdf_file)

def pandaFk(q, n):
    link_names = ['panda_link' + str(i) for i in range(0, 10)]
    root = "panda_link0"
    tip = link_names[n]
    fk = robot.get_forward_kinematics(root, tip, q)["T_fk"][0:3, 3]
    return fk


if __name__ == "__main__":
    q = ca.SX.sym("q", 7)
    q_test = np.ones(7)
    for i in range(0, 10):
        print("---", i, "---")
        fk = pandaFk(q,  i)
        print(fk)
