import scipy.optimize as spo
from sys import argv as ldc
from math import sin, cos, pi
import time as t

def cbrt(x):
    """
    Redefinition de la racine cubique d'un nombre
    """
    if x >= 0:
        return x ** (1 / 3)
    else:
        return - cbrt(-x)

def f(a, x):
    """
    Fonction dans laquelle on recherche les racines dependant du parametre
    a entre en ligne de commande
    """
    return x + sin(x) ** 2 - a * abs(cbrt(x * sin(x)))

def sign(f, a, b):
    signe = f((b + a)/2)
    if signe >= 0:
        return 1
    else:
        return -1

def df(a, x, b_inf, b_sup):
    sin_x = sin(x)
    cos_x = cos(x)
    return cbrt((x * sin_x)**2) + 2  * (cbrt(x * sin_x)**2) * sin_x * \
    cos_x - sign(sin, b_inf, b_sup) * a / 3 * (sin_x + x * cos_x)

def intersections(a):
    """
    Methode qui calcule les intersection entre la courbe donnee par
    (x sin(x), x + sin(x) * sin(x)) et abs(sqrt3(x)) en fonction du
    parametre a entre en ligne de commande
    On recherche les minimums locaux de la fonction, pour ce faire, on
    recherche les racines de la derivee
    Une fois les minimums locaux calcules, si leur image par f est 
    negative, on recherche la racine entre le multiple de pi precedent
    et ce minimum et puis entre ce minimum et le multiple de pi suivant
    """
    intersections_fn = [(0, 0)]
    if a == 0:
        return intersections_fn
    elif a < 1e-10 or a > 1e5:
        raise Exception("La valeur de a rentree demande trop de precision")
    elif a < 0 :
        raise Exception("La valeur rentree doit etre positive")
    else:
        min_loc = pi
        while f(a, min_loc) >= 0:
            min_loc = min_loc / 2
        racine = spo.brentq(lambda x: f(a, x), min_loc, pi)
        sin_rac = sin(racine)
        intersections_fn.append((racine * sin_rac, racine + sin_rac ** 2))
        min_loc = spo.brentq(lambda x : df(a, x, pi, 2 * pi), pi, 2 * pi)
        k = 1
        while f(a, min_loc) <= 0:
            racine = spo.brentq(lambda x: f(a, x), k * pi, min_loc)
            sin_rac = sin(racine)
            intersections_fn.append((racine * sin_rac, racine + sin_rac ** 2))
            racine = spo.brentq(lambda x: f(a, x), min_loc, (k + 1) * pi)
            sin_rac = sin(racine)
            intersections_fn.append((racine * sin_rac, racine + sin_rac ** 2))
            k = k + 1
            min_loc = spo.brentq(lambda x: df(a, x, k * pi, (k + 1) * pi), \
            k * pi, (k + 1) * pi)
        return intersections_fn

if __name__ == '__main__':
    """
    Methode "main", elle lancera la methode principale avec la valeur donnee en
    ligne de commande
    """
    a = float(ldc[1])
    b = intersections(a)
    for i in b :
        print(str(i[0]) + " " + str(i[1]))