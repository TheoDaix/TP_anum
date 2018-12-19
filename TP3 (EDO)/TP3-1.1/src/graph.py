import time_p1 as tp, matplotlib.pyplot as plt, numpy as np
import trajectoire
from math import pi

def graph(m, a):
    """
    Methode permettant d'afficher les graphiques de S(t) en fonction des
    parametres m (la masse) et a (parametre de la fonction gamma) rentres.
    """
    subd = np.linspace(0.2, 0.4, 20)
    t = np.linspace(0, 30, 100001)
    for i in subd:
        res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                                   lambda x: tp.ddgamma(x, a),
                                   i, m, 30, 100001, (0, 0))
        if(res[100000][0] > 3*pi/2):
            plt.plot(t, res[:, 0], 'b', label='$S(t) > p_2$', linewidth=0.2)
        else:
            plt.plot(t, res[:, 0], 'r', label='$S(t) < p_2$', linewidth=0.2)
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.savefig("Graphe.pdf", quality=95)
    plt.show()

graph(1, 0.1)