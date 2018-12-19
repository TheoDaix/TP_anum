import time_p1 as tp, scipy.optimize as spo
import trajectoire, sys
from math import pi

def f(m, a, t, mu, y0):
    """
    Fonction dont on va rechercher les racines (en fonction de mu) dependant
    de plusieurs parametres : m (la masse), a (le parametre de la fonction
    gamma), t (le temps) et y0 (le point de depart).
    La racine correspondra au frottement le plus grand tel que le mobile
    passe le sommet p2.
    """
    res = trajectoire.solution(lambda x: tp.dgamma(x, a), lambda x:
                               tp.ddgamma(x, a), mu, m, t, 2, y0)
    return res[1][0] - 2 * pi

def sup_mu(m, a):
    """
    Fonction principale pour rechercher le coefficient de frottements mu le
    plus eleve tel que le mobile passe le sommet p2. Cette methode depend des
    deux parametres m (la masse) et a (parametre de la fonction gamma).
    """
    mu = 0
    while (f(m, a, 60, mu, (0,0)) > 0):
        mu += 0.01
    if (mu == 0):
        return "AUCUN"
    else:
        return spo.brentq(lambda x: f(m, a, 60, x, (0, 0)), mu - 0.01, mu)

if __name__ == "__main__":
    """
    Methode "main", elle lancera la methode principale de sup_mu avec les
    valeurs donnees en ligne de commande.
    """
    m = float(sys.argv[1])
    a = float(sys.argv[2])
    print(sup_mu(m, a))
