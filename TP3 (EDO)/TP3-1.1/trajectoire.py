from scipy.integrate import odeint as edo
from scipy.constants import g
import numpy as np

def trajectoire(gamma, dgamma, ddgamma, mu, m):
    y0 = gamma(0)
    t = np.linspace(0, 2.97, 11)
    return edo(f, y0, t, args=(m, mu, dgamma, ddgamma))

def f(y, t, m, mu, dgamma, ddgamma):
    s, ds = y
    dgamma_s = dgamma(s)
    ddgamma_s = ddgamma(s)
    a = prod(dgamma_s, ddgamma_s) * ds**2
    b = g * dgamma_s[1]
    c = mu * prod(dgamma_s, dgamma_s) / m
    d = prod(dgamma_s, dgamma_s)
    res = (-a - b - c)/d
    dydt = [ds, res]
    return dydt

def prod(u, v):
    return u[0] * v[0] + u[1] * v[1]

def gamma(t):
    return (11*t, 3-3*t)

def dgamma(t):
    return (11, -3)

def ddgamma(t):
    return (0, 0)

print(trajectoire(gamma, dgamma, ddgamma, 0, 450))