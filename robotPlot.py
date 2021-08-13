import numpy as np
import casadi as ca
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from numpyFk import numpyFk

class RobotPlot(object):

    """Plotting robot trajectories for various robots
    types:  0 : point robot
            1 : planar robotic arm
            2 :
            3 :
            4 : point robot with orientation
    """

    def __init__(self, qs, fk, m, types, dt=0.01):
        self._dt = dt
        self._qs = qs
        self._fk = fk
        self._m = m
        self._nbSol = len(self._qs)
        self._ns = []
        self._dims = []
        self._types = types
        self._obsts = []
        self._obstacleAxes = []
        self._goals = []
        self._goalAxes = []
        for q in qs:
            self._ns.append(len(q))
            self._dims.append(len(q[0]))
        self.convert()

    def convert(self):
        self._fks = []
        for j in range(self._nbSol):
            fks = np.zeros((self._ns[j], self._m))
            for i in range(self._ns[j]):
                if self._types[j] == 3:
                    fk = np.array(self._fk(self._qs[j][i])).transpose()[0, :]
                elif self._types[j] == 1 or self._types[j] == 2:
                    fk = np.array(self._fk(self._qs[j][i], self._dims[j])[0:self._m])
                elif self._types[j] == 0:
                    fk = np.array(self._fk(self._qs[j][i]))
                elif self._types[j] == 4:
                    fk = np.array(self._fk(self._qs[j][i]))[:, 0]
                fks[i, :] = fk
            self._fks.append(fks)

    def addSolutions(self, nbAx, qs):
        for q in qs:
            n = len(q)
            m = len(q[0])
            fk = np.zeros((n, m))
            for i in range(len(q)):
                fk[i, :] = np.array(self._fk(q[i]))
            self._axs[nbAx].plot(fk[:, 0], fk[:, 1])

    def initFig(self, n, m, fig=None, lims=[(-5, 5), (-5, 5)], grid=False):
        if not fig:
            self._fig, axs = plt.subplots(n, m, figsize=(m*4, n*4))
        if (n == 1) and (m == 1):
            self._axs = [axs]
        else:
            self._axs = axs.flatten()
        for i in range(self._nbSol):
            self._axs[i].set_xlim([lims[0][0], lims[0][1]])
            self._axs[i].set_ylim([lims[1][0], lims[1][1]])
            if grid:
                minor_xticks = np.arange(lims[0][0], lims[0][1], 0.25)
                minor_yticks = np.arange(lims[1][0], lims[1][1], 0.25)
                self._axs[i].set_xticks(minor_xticks, minor=True)
                self._axs[i].set_yticks(minor_yticks, minor=True)
                self._axs[i].grid(which='major', alpha=0.8)
                self._axs[i].grid(which='minor', alpha=0.2)

    def getAx(self, i):
        return self._axs[i]

    def getAxs(self, indices):
        return self._axs[indices]

    def plot(self):
        for i in range(self._nbSol):
            self._axs[i].plot(self._fks[i][:, 0], self._fks[i][:, 1])

    def plotMulti(self, nbAx):
        for i in range(self._nbSol):
            self._axs[nbAx].plot(self._fks[i][:, 0], self._fks[i][:, 1])

    def animateEE(self, num):
        for i in range(len(self._lines)):
            maxNum = min(self._ns[i] - 1, num)
            start = max(0, maxNum - 100)
            self._lines[i].set_data(self._fks[i][start:maxNum, 0], self._fks[i][start:maxNum, 1])
            self._points[i].set_data(self._fks[i][maxNum, 0], self._fks[i][maxNum, 1])
        self.plotRobots(num)
        self.plotObstacles(num)
        self._goalLines = self.plotGoals(num)
        return self._lines + self._points + self._patches + self._goalLines

    def plotObstacles(self, num):
        t = num * self._dt
        for i in range(len(self._obstacleAxes)):
            for nbAx in self._obstacleAxes[i]:
                for obst in self._obsts[i]:
                    x = obst.x(t)
                    r = obst.r()
                    patch = plt.Circle(x, r, color='r')
                    self._patches.append(self._axs[nbAx].add_patch(patch))

    def plotGoals(self, num):
        t = num * self._dt
        goalLines = []
        goalPoints = []
        for i in range(len(self._goalAxes)):
            for nbAx in self._goalAxes[i]:
                goal = self._goals[i]
                if isinstance(goal, np.ndarray):
                    goalPoints.append(self._axs[nbAx].plot(goal[0], goal[1], 'g.')[0])
                    continue
                start = max(0, num - 100)
                steps = num-start
                xs = np.zeros((steps, 2))
                x = np.zeros(2)
                for j in range(steps):
                    t = (j+start) * self._dt
                    x = np.array(goal(t))[:, 0]
                    if len(x) == 1:
                        x = np.array([x[0], 0.3])
                    xs[j,:] = x
                goalLines.append(self._axs[nbAx].plot(xs[:, 0], xs[:, 1], 'g-')[0])
                goalPoints.append(self._axs[nbAx].plot(x[0], x[1], 'g.')[0])
                """
                goalRadius = 0.05
                if len(x) == 1:
                    patch = plt.Circle(np.array([x[0], 0.3]), radius=goalRadius, color='g')
                else:
                    patch = plt.Circle(np.array([x[0], x[1]]), radius=goalRadius, color='g')
                self._patches.append(self._axs[nbAx].add_patch(patch))
                """
        return goalLines + goalPoints

    def plotRobots(self, t):
        self._patches = []
        for j in range(self._nbSol):
            if self._types[j] == 0 or self._types[j] == 3:
                continue
            t = min(t, self._ns[j] - 1)
            if self._types[j] == 4:
                a = self._qs[j][t, 2]
                R = np.array([
                                [np.cos(a), -np.sin(a)],
                                [np.sin(a), np.cos(a)]
                            ])
                offset = np.array([-0.75, -0.30])
                offset_real = np.dot(R, offset)
                x = self._qs[j][t, 0:2]
                vehicle = plt.Rectangle(x + offset_real , 1.5, 0.6, angle=np.rad2deg(a))
                self._patches.append(self._axs[j].add_patch(vehicle))
                dx = np.dot(R, np.array([1.5, 0.0]))
                oriArrow1 = plt.Arrow(x[0], x[1], dx[0], dx[1], width=0.3)
                self._patches.append(self._axs[j].add_patch(oriArrow1))
                if len(self._qs[j][t, :]) == 3:
                    continue
                offset_arm_start = np.array([0.2, 0.0])
                offset_arm_start_real = np.dot(R, offset_arm_start)
                offset_arm = np.array([-0.0, -0.025])
                a_arm = a + self._qs[j][t, 3]
                R = np.array([
                                [np.cos(a_arm), -np.sin(a_arm)],
                                [np.sin(a_arm), np.cos(a_arm)]
                            ])
                offset_arm_real = np.dot(R, offset_arm)
                x = self._qs[j][t, 0:2]
                arm = plt.Rectangle(x + offset_arm_real + offset_arm_start_real , 1.0, 0.05, angle=np.rad2deg(a_arm), color='black')
                self._patches.append(self._axs[j].add_patch(arm))
                continue
            joints = []
            links = []
            offset = np.array([-0.00, -0.05])
            q = self._qs[j][t, :]
            armStartIndex = 0
            xi = []
            if self._types[j] == 1:
                baseLink = plt.Rectangle([-0.5, -0.4], 1.0, 0.6, fill='blue', alpha=0.3)
                self._patches.append(self._axs[j].add_patch(baseLink))
            if self._types[j] == 2:
                xi = self._fk(q, 0)
                baseLink = plt.Rectangle([xi[0]-0.5, xi[1]], 1.0, 1.0, fill='blue', alpha=0.3)
                armStartIndex = 1
                self._patches.append(self._axs[j].add_patch(baseLink))
            for i in range(armStartIndex, self._dims[j]):
                xi = self._fk(q, i)
                a = xi[2]
                R = np.array([
                                [np.cos(a), -np.sin(a)],
                                [np.sin(a), np.cos(a)]
                            ])
                offset_real = np.dot(R, offset)
                joint = plt.Circle(xi[0:2], radius=0.1)
                link = plt.Rectangle(xi[0:2] + offset_real, 1.0, 0.1, angle = np.rad2deg(xi[2]))
                self._patches.append(self._axs[j].add_patch(joint))
                self._patches.append(self._axs[j].add_patch(link))
            xee = self._fk(q, self._dims[j])
            eeJoint = plt.Circle(xee[0:2], radius=0.1)
            self._patches.append(self._axs[j].add_patch(eeJoint))
        return self._patches

    def addObstacle(self, nbAxs, obsts):
        self._obsts.append(obsts)
        self._obstacleAxes.append(nbAxs)
        """
        for nbAx in nbAxs:
            for obst in obsts:
                x = obst.x()
                r = obst.r()
                patch = plt.Circle(x, r, color='r')
                self._axs[nbAx].add_patch(patch)
        """

    def addGoal(self, nbAxs, goal):
        self._goals.append(goal)
        self._goalAxes.append(nbAxs)

    def addSpline(self, nbAxs, spline):
        pos = np.zeros((2, 100))
        points = np.array(spline.evalpts)
        for nbAx in nbAxs:
            self._axs[nbAx].plot(points[:, 0], points[:, 1])

    def makeAnimation(self, steps):
        self._lines = []
        self._points = []
        for j in range(self._nbSol):
            self._lines.append(self._axs[j].plot([], [], color='k')[0])
            self._points.append(self._axs[j].plot([], [], 'r.')[0])
        try:
            self._ani = animation.FuncAnimation(
                self._fig, self.animateEE, steps,
                interval=self._dt*100, blit=True
            )
        except TypeError as err:
            print("Type error in animation")
            print("Verify that steps is an integer")
            print("nsteps : ", steps , " of type : ", type(steps))

    def addTitles(self, is_ax, titles):
        for i, i_ax in enumerate(is_ax):
            self._axs[i_ax].set_title(titles[i])

    def show(self):
        plt.show()

    def saveFigure(self):
        print("Saving the figure can take several minutes")
        fileName = input("Filename or 'no' for abortion\n")
        if fileName != 'no':
            print("Saving the figure with animations")
            writerVideo = animation.FFMpegFileWriter(fps=60)
            self._ani.save(fileName, writer=writerVideo)

if __name__ == "__main__":

    n_steps = 1000
    t = np.arange(0, n_steps, 0.1)
    qs0 = np.array([0.1 * t, 0.1 * t]).transpose()
    qs1 = np.array([-0.1 * t[0:100], 0.1 * t[0:100]]).transpose()
    qs2 = np.array([0.1 * t, 0.2 * t, 0.1 * t]).transpose()
    qsall = [qs0, qs2, qs1]
    fk_fun = lambda q, n : numpyFk(q, n)
    """
    w = 0.1
    qs = np.array([1.1 * np.cos(w * t), 2.1 * np.sin(w * t)]).transpose()
    qsall = [qs]
    fk_fun = lambda q, n : np.array([q[0], q[1], 0.0])
    """
    m = 3
    robotPlot = RobotPlot(qsall, fk_fun, m, types=[1, 1, 1])
    robotPlot.initFig(2, 2)
    robotPlot.plot()
    #robotPlot.plotMulti(0)
    robotPlot.makeAnimation(n_steps)
    robotPlot.show()
