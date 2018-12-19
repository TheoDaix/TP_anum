from math import sin, exp, cos, pi
import sys, trajectoire

def gamma(s, a):
    """
    Fonction gamma(s) dependant d'un parametre a.
    """
    return (s, (1 + cos(s)) * exp(-a * s))

def dgamma(s, a):
    """
    Derivee de la fonction gamma(s).
    """
    return (1, - exp(-a * s) * (sin(s) + a * (1 + cos(s))))

def ddgamma(s, a):
    """
    Derivee seconde de la fonction gamma(s).
    """
    return (0, a * exp(-a * s) * (sin(s) + a * (1 + cos(s))) - exp(-a * s) *
            (cos(s) - a * sin(s)))

def f(m, a, t, mu, y0):
    """
    Fonction dont on va rechercher les racines (en fonction du temps) dependant
    de plusieurs parametres : m (la masse), a (le parametre de la fonction
    gamma), mu (le coefficient de frottements) et y0 (le point de depart).
    La racine correspondra au moment ou le mobile passe par le point p1.
    """
    res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x, a),
                               mu, m, t, 2, y0)
    return res[1][0] - pi

def time_p1(m, a, mu):
    """
    Fonction principale afin de rechercher le moment ou le mobile passe par
    le point p1 dependant de plusieurs parametres : m (la masse) et a
    (parametre de la fonction a).
    """
    y0 = (0, 0)
    t = 60 + 1/(2 * m * a)
    res = trajectoire.solution(lambda x: dgamma(x, a), lambda x: ddgamma(x, a),
                               mu, m, t, 10001, y0)
    n = 1
    while (n < 10001 and res[n][0] < pi):
        n += 1
    t0 = (t / 10000) * (n - 1)
    t = (t / 10000) * n
    x = (t0 + t) / 2
    while (t - t0 > 1e-8 and abs(f(m, a, x, mu, y0)) > 1e-100):
        if (f(m, a, x, mu, y0) > 0):
            t = x
        else:
            t0 = x
        x = (t0 + t) / 2
    return x

if __name__ == "__main__":
    """
    Methode "main", elle lancera la methode principale de time_p1 avec les
    valeurs donnees en ligne de commande.
    """
    m = float(sys.argv[1])
    a = float(sys.argv[2])
    t1 = time_p1(m, a, 0.3)
    print(t1)