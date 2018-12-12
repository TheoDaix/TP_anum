from math import sin, exp, cos, pi
import trajectoire
import numpy as np
import matplotlib.pyplot as plt
import sys

def gamma(s, a):
    return (s, (1 + cos(s)) * exp(-a * s))

def dgamma(s, a):
    return (1, - exp(-a * s) * (sin(s) + a * (1 + cos(s))))

def ddgamma(s, a):
    return (0, a * exp(-a * s) * (sin(s) + a * (1 + cos(s))) - exp(-a * s) *
            (cos(s) - a * sin(s)))

def time_p1(m, a, mu):
    y0 = (0, 0)
    t = 0
    res = trajectoire.solution(lambda x : dgamma(x, a), lambda x : ddgamma(x,
     a), mu, m, t, 2, y0)
    while(res[1][0] < pi):
        t += 0.1
        res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x,
                                a), mu, m, t, 2, y0)
    val = res[1][0]
    ecart = t/2
    while(abs(val - pi)/pi > 0.000000001):
        ecart = ecart / 2
        if (val < pi):
            t = t + ecart
        else:
            t = t - ecart
        res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(
            x, a), mu, m, t, 2, y0)
        val = res[1][0]
    print(t)

    res = trajectoire.solution(lambda x : dgamma(x, a), lambda x : ddgamma(x,
     a), mu, m, t, 101, y0)
    t = np.linspace(0, t, 101)
    plt.plot(t, res[:, 0], 'b', label='S(t)')
    plt.plot(t, res[:, 1], 'g', label='dS(t)')
    for j in res:
        i = gamma(j[0], a)
        plt.plot(i[0], i[1], 'ro', label='gamma(S(t))')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    m = float(sys.argv[1])
    a = float(sys.argv[2])
    time_p1(m, a, 0.3)
