import math


def arret_defaut(a, b, epsi=1e-8):
    return abs(a - b) <= epsi


def f(x):
    return x * x * x + 4 * x * x - 10


def f1(x):
    return 3 * x * x + 8 * x


def phi1(x):
    return math.sqrt((10 - x * x * x)/4)

def phi2(x):
    return 10/(x * x + 4 * x)


def phi3(x):
    return math.sqrt(10/(x + 4))


def bissection(f, a, b, arret=False, max_iter=50):
    """
        Implémentation de la bissection.

        Entrées
        -------
        f : fonction
            Fonction d'une variable réelle à valeur réelle.
            Elle est supposée continue
        a : nombre
            Une borne pour l'intervalle de recherche
            de racine.
        b : nombre
            Une seconde borne pour l'intervalle de recherche de racine.
        arret : fonction, optionnelle
            Fonction d'arrêt pour l'algorithme de bissection. Par défaut ...
        max_iter : nombre, optionnel
            Nombre maximal d'itérations lors d'un appel de la bissection.
            Par défaut, max_iter=50. Si max_iter est dépassé, une exception est
            levée.

        Sortie
        ------
        r : nombre
            Un nombre réel, solution de l'équation f(x)=0 dans l'intervalle [a,b].
    """
    if(f(a) * f(b) > 0):
        raise Exception("Le produit des bornes doit être negatif")
    else:
        if f(a) < 0:
            (a, b) = (b, a)
        X = (a + b) / 2
        N = 0
        f_X = f(X)
        while (N < max_iter and (not (arret) or (f_X >= 1e-8))):
            print(" * x" + str(N) + " = " + str(X))
            if (f_X > 0):
                a = X
            else:
                b = X
            X = (a + b) / 2
            N = N + 1
            f_X = f(X)
            arret = arret_defaut(a, b)
        if ((N == iter) and (not (arret))):
            raise Exception("Manque d'iterations")
        r = X
        return r


def bonne_approx(phi, X, epsi=1e-15):
    return abs(phi(X) - X) < epsi


def pt_fixe(phi, x_0, nbr_iter=50):
    print(" * x0 = " + str(x_0))
    X = phi(x_0)
    print(" * x1 = " + str(X))
    N = 0
    while (not (bonne_approx(phi, X)) and N < nbr_iter):
        X = phi(X)
        print(" * x" + str(N + 2) + " = " + str(X))
        N = N + 1
    if ((N == nbr_iter) and (not (bonne_approx(phi, X, 1e-8)))):
        return "Point repulsif ou manque d'iterations"
    else:
        return X

#print(bissection(f, -10, 0))
print(pt_fixe(phi2, 1))
