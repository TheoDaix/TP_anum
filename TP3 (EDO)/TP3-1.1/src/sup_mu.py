import time_p1 as tp
import trajectoire, sys
from math import pi

def sup_mu(m, a, t):
    mu = 0
    arret = True #inutile si on garde ça
    while (arret):
        res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                                   lambda x: tp.ddgamma(x, a),
                                   mu, m, t, 2, (0, 0))
        """
        while (res[1][0] < pi):
            t += 0.1
            res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                                       lambda x: tp.ddgamma(x, a),
                                       mu, m, t, 2, y0)
        while (res[1][0] > pi and res[1][0] < 2 * pi):
            t += 0.1
            res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                                       lambda x: tp.ddgamma(x, a),
                                       mu, m, t, 2, y0)
        """
        if (res[1][0] <= 2 * pi):
            arret = False
        else:
            mu += 0.01
    if (mu == 0):
        return "AUCUN"
    else:
        return recherche_mu_boucle(m, (0, 0), a, mu - 0.01, mu, t)

def recherche_mu(m, y0, a, mu0, mu, t):
    milieu = (mu0 + mu)/2
    res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                               lambda x: tp.ddgamma(x, a),
                               milieu, m, t, 2, y0)
    """
    while (res[1][0] < pi):
        t += 0.1
        res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                                   lambda x: tp.ddgamma(x, a),
                                   milieu, m, t, 2, y0)
    while (res[1][0] > pi and res[1][0] < 2 * pi):
        t += 0.1
        res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                                   lambda x: tp.ddgamma(x, a),
                                   milieu, m, t, 2, y0)
    """

    if (abs(mu - mu0)/abs(mu) < 1e-8):
        return milieu
    if (res[1][0] <= pi):
        return recherche_mu(m, y0, a, mu0, milieu, t)
    else:
        return recherche_mu(m, y0, a, milieu, mu, t)
def recherche_mu_boucle(m, y0, a, mu0, mu, t):
    while (abs(mu - mu0)/mu0 > 1e-8):
        milieu = (mu0 + mu)/2
        res = trajectoire.solution(lambda x: tp.dgamma(x, a),
                                   lambda x: tp.ddgamma(x, a),
                                   milieu, m, t, 2, y0)
        if (res[1][0] <= pi):
             mu = milieu
        else:
            mu0 = milieu
    return milieu
if __name__ == "__main__":
    m = float(sys.argv[1])
    a = float(sys.argv[2])
    t_max = 100
    print(sup_mu(m, a, t_max))
