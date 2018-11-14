import scipy.linalg.blas as slb
import numpy as np
import q1

def deriv(A, dA, B, dB, t):
    """
    Fonction deriv qui prend en parametres les fonctions A et B, ainsi que leur
    derivee respective dA et dB.
    On evalue d'abord les 4 fonctions en t. On se ramene ensuite a
    calculer la solution d'un premier systeme, et finalement, apres une serie
    de manipulations, a calculer la solution d'un second systeme.
    """
    a = A(t)
    da = dA(t)
    b = B(t)
    db = dB(t)
    at = np.transpose(a)
    dat = np.transpose(da)

    m = slb.sgemm(1, at, a)
    m1 = slb.sgemm(1, at, b)

    x = q1.solution_systeme(m, m1)

    m1 = slb.sgemm(1, dat, a)
    m1 = slb.sgemm(1, m1, x)
    m2 = slb.sgemm(1, at, da)
    m2 = slb.sgemm(1, m2, x)
    m1 = slb.saxpy(m1, m2)

    m2 = slb.sgemm(1, dat, b)
    m3 = slb.sgemm(1, at, db)
    m2 = slb.saxpy(m2, m3)

    m1 = slb.sscal(-1, m1)
    m2 = slb.saxpy(m1, m2)
    return q1.solution_systeme(m, m2)
