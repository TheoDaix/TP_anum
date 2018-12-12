from scipy.integrate import odeint as edo
import numpy as np

def solution(dgamma, ddgamma, mu, m, t1, n, y0):
    t = np.linspace(0, t1, n)
    return edo(f, y0, t, args=(m, mu, dgamma, ddgamma))

def f(y, t, m, mu, dgamma, ddgamma):
    s, ds = y
    dgamma_s = dgamma(s)
    ddgamma_s = ddgamma(s)
    a = prod(dgamma_s, ddgamma_s) * ds**2
    b = 9.81 * dgamma_s[1]
    c = (mu / m) * ds
    d = prod(dgamma_s, dgamma_s)
    res = ((-a - b)/d) - c
    dydt = [ds, res]
    return dydt

def prod(u, v):
    return u[0] * v[0] + u[1] * v[1]


