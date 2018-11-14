import scipy.linalg.blas as s
import numpy as np
from q1 import solution_systeme as q1

def deriv(A, dA, B, dB, t):
    """
    Fonction deriv qui prend en paramètres les matrices A, B qui varient en
    fonction de t ainsi que leur dérivées respectives dA et dB.
    On évalue d'abord les 4 matrices au moment t ; on se ramène ensuite à
    calculer la solution premier système et finalement, après une série de
    manipulations, à calculer la solution d'un second système.
    """
    a = A(t)
    da = dA(t)
    b = B(t)
    db = dB(t)
    at = np.transpose(a)
    dat = np.transpose(da)

    m = s.sgemm(1, at, a)
    m1 = s.sgemm(1, at, b)

    x = q1(m, m1)

    m1 = s.sgemm(1, dat, a)
    m1 = s.sgemm(1, m1, x)
    m2 = s.sgemm(1, at, da)
    m2 = s.sgemm(1, m2, x)
    m1 = sum(1, m1, m2)

    m2 = s.sgemm(1, dat, b)
    m3 = s.sgemm(1, at, db)
    m2 = sum(1, m2, m3)

    m2 = sum(-1, m1, m2)
    return q1(m, m2)

def sum(alpha, A, B):
    """
    Calcule la somme de deux matrices A et B données en paramètres.
    """
    n = len(A)
    m = len(A[0])
    S = []
    for i in range(0, n):
        ligne = []
        for j in range(0,m):
            ligne.append(A[i][j] + alpha * B[i][j])
        S.append(ligne)
    return S