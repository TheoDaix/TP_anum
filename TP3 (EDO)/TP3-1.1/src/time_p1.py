from math import sin, exp, cos, pi
import numpy as np, scipy.optimize as spo, matplotlib.pyplot as plt
import sys, trajectoire

def gamma(s, a):
    return (s, (1 + cos(s)) * exp(-a * s))

def dgamma(s, a):
    return (1, - exp(-a * s) * (sin(s) + a * (1 + cos(s))))

def ddgamma(s, a):
    return (0, a * exp(-a * s) * (sin(s) + a * (1 + cos(s))) - exp(-a * s) *
            (cos(s) - a * sin(s)))

def f(a, t, mu, y0):
    res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x, a),
                               mu, m, t, 2, y0)
    return res[1][0] - pi

def time_p1(m, a, mu):
    y0 = (0, 0)
    t = 0
    res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x, a),
                               mu, m, t, 2, y0)
    while (res[1][0] < pi):
        t += 0.1
        res = trajectoire.solution(lambda x: dgamma(x, a),
                                   lambda x: ddgamma(x, a),
                                   mu, m, t, 2, y0)
    res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x, a),
                               mu, m, t, 1001, y0)
    n = 0
    arret = True
    while (n < len(res) and arret):
        if (res[n][0] > pi):
            arret = False
        n += 1
    t = (t/1000) * (n - 1)
    t = spo.brentq(lambda x: f(a, x, mu, y0), 0, t)
    return t

def graphe(m, mu, t, y0, a):
    res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x, a),
                               mu, m, t, 101, y0)
    t = np.linspace(0, t, 101)
    plt.plot(t, res[:, 0], 'b', label='S(t)')
    plt.plot(t, res[:, 1], 'g', label='dS(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

    gamma_S_0 = []
    gamma_S_1 = []
    for j in res:
        i = gamma(j[0], a)
        gamma_S_0.append(i[0])
        gamma_S_1.append(i[1])
    x = np.array(gamma_S_0)
    y = np.array(gamma_S_1)
    plt.plot(x, y, 'r', label='gamma(S(t))')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    m = float(sys.argv[1])
    a = float(sys.argv[2])
    t1 = time_p1(m, a, 0.3)
    print(t1)
    graphe(m, 0.3, t1, (0, 0), a)