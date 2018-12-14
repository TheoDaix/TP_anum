import time_p1 as tp, matplotlib.pyplot as plt
import trajectoire
import numpy as np
from math import pi

def graph(m, a, t1):
    subd = np.linspace(0.2, 0.4, 20)
    t = np.linspace(0, t1, 100001)
    for i in subd:
        res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                                   lambda x: tp.ddgamma(x, a),
                                   i, m, t1, 100001, (0,0))
        if(res[100000][0] > 3*pi/2):
            plt.plot(t, res[:, 0], 'b', label='$S(t) > p_2$',
                     linewidth=0.2)
        else:
            plt.plot(t, res[:, 0], 'r', label='$S(t) < p_2$', linewidth=0.2)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.savefig("Graphe.pdf", quality=95)
    plt.show()

graph(1, 0.1, 30)

def graph_2(m, a, t1):
    subd = np.linspace(0.2, 0.4, 20)
    cpt=0
    for i in subd:
        res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                                   lambda x: tp.ddgamma(x, a),
                                   i, m, t1, 100001, (0,0))
        gamma_S_0 = []
        gamma_S_1 = []
        for j in res:
            k = tp.gamma(j[0], a)
            gamma_S_0.append(k[0])
            gamma_S_1.append(k[1])
        x = np.array(gamma_S_0)
        y = np.array(gamma_S_1)
        plt.plot(x, y, 'r', label='gamma(S(t))')
        plt.annotate(r'$\gamma(S(t))_{\mu = '+ str(i) +'}$',
                 xy=(gamma_S_0[100000], gamma_S_1[100000]), xycoords='data',
                 xytext=(+10, +((-1)**cpt)*30), textcoords='offset points',
                     fontsize=16,
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3,rad=.2"))
        plt.plot(gamma_S_0[100000], gamma_S_1[100000], 'co')
        plt.legend(loc='best')
        plt.xlabel('t')
        plt.grid()
        cpt += 1
    plt.show()

graph_2(1, 0.1, 30)
