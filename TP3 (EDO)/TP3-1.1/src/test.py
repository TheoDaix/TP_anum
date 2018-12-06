import trajectoire
from math import atan, cos, sin, sqrt
import matplotlib.pyplot as plt
import numpy as np

def gamma(h, l, t):
    return (l*t, h*(1-t))

def dgamma(h, l, t):
    return (l, -h)

def ddgamma(h, l, t):
    return (0, 0)

def test(mu, m, h, l):
    theta = atan(h/l)
    t = sqrt(22/(9.81*cos(theta)*sin(theta)))
    res = trajectoire.solution(lambda x: dgamma(h, l, x), lambda x: ddgamma(
        h, l, x), mu, m, t)
    for i in res:
        print(gamma(h, l, i[0]))
    """
    t = np.linspace(0, t, 101)
    plt.plot(t, res[:, 0], 'b', label='S(t)')
    plt.plot(t, res[:, 1], 'g', label='dS(t)')
    for j in res:
        i = gamma(h, l, j[0])
        plt.plot(i[0], i[1], 'go')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()
    """
test(0, 450, 3, 11)