import time_p1 as tp, matplotlib.pyplot as plt
import trajectoire
import numpy as np
from math import pi

def graph(m, a, t1):
    subd = np.linspace(1, 1.01, 20)
    t = np.linspace(0, t1, 100001)
    for i in subd:
        res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                                   lambda x: tp.ddgamma(x, a),
                                   i, m, t1, 100001, (0,0))
        if(res[100000][0] > 3*pi/2):
            plt.plot(t, res[:, 0], 'b', label='S(t) > p2', linewidth=0.2)
        else:
            plt.plot(t, res[:, 0], 'r', label='S(t) < p2', linewidth=0.2)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

graph(1, 0.4, 30)