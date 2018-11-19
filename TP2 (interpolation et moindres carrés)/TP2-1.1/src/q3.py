import q2
from math import sin, cos, atan, exp
import sys as s

def A(x):
    return [[sin(x), 2 * x], [x, exp(x)], [atan(x), x]]

def dA(x):
    return [[cos(x), 2], [1, exp(x)], [1/(1+x*x), 1]]

def b(x):
    return [[x], [x*x], [1/(1+x*x)]]

def db(x):
    return [[1], [2*x], [-2*x/((1+x*x)**2)]]

if __name__ == '__main__':
    """
    Methode "main", elle lancera la methode principale de q2 avec la valeur
    donnee en ligne de commande et les fonctions definies ci-dessus.
    """
    sol = q2.deriv(A, dA, b, db, float(s.argv[1]))
    for i in range(0, len(sol)):
        print("%.16g" % sol[i])