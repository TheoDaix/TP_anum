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

def S(a, t, mu, y0):
    res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x, a),
                               mu, m, t, 2, y0)
    return res[1][0] - pi

def time_p1(m, a, mu):
    y0 = (0, 0)
    t = 0
    res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x, a),
                               mu, m, t, 2, y0)
    while(res[1][0] < pi):
        t += 0.1
        res = trajectoire.solution(lambda x: dgamma(x, a),
                                   lambda x: ddgamma(x, a),
                                   mu, m, t, 2, y0)
    val = res[1][0]
    ecart = t/2
    while(abs(val - pi)/pi >= 1e-8):
        ecart = ecart / 2
        if (val < pi):
            t = t + ecart
        else:
            t = t - ecart
        res = trajectoire.solution(lambda x: dgamma(x, a),
                                   lambda x: ddgamma(x, a),
                                   mu, m, t, 2, y0)
        val = res[1][0]
    return t

def time_p1_elegant(m, a, mu):
    y0 = (0, 0)
    t = 0
    res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x, a),
                               mu, m, t, 2, y0)
    while (res[1][0] < pi):
        t += 0.1
        res = trajectoire.solution(lambda x: dgamma(x, a),
                                   lambda x: ddgamma(x, a),
                                   mu, m, t, 2, y0)
    t = spo.brentq(lambda x: S(a, x, mu, y0), 0, t)
    return t

def graphe(m, mu, t, y0, a):
    res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x, a),
                               mu, m, t, 101, y0)
    t = np.linspace(0, t, 101)
    plt.plot(t, res[:, 0], 'b', label='S(t)')
    plt.plot(t, res[:, 1], 'g', label='dS(t)')
    for j in res:
        i = gamma(j[0], a)
        plt.plot(i[0], i[1], 'ro')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    m = float(sys.argv[1])
    a = float(sys.argv[2])
    #t1 = time_p1(m, a, 0.3)
    t2 = time_p1_elegant(m, a, 0.3)
    print(t2)
    #print(abs(t1 - t2) < 1e-8)
    graphe(m, 0.3, t2, (0, 0), a)
