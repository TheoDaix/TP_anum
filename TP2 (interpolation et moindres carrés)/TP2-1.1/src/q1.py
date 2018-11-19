import scipy.linalg.lapack as sll
import numpy as np
from sys import argv as ldc

def solution_systeme(A, B):
    """
    Permet de resoudre un système Ax = B ou A est une matrice carree
    """
    sol = sll.dgesv(A, B)
    if sol[3] == 0:
        return sol[2]
    elif sol[3] > 0:
        raise Exception("Le systeme comporte une infinite de solutions ou est"
        " impossible.")
    else:
        raise Exception("Un des arguments n'est pas valide.")

def formMat(args):
    """
    Permet de former les matrices a partir des arguments entres en ligne de
    commande. Retourne le tuple (M, N, A, B) ou A est une matrice M * N et B
    une matrice M * 1.
    """
    M = int(args[0])
    N = int(args[1])
    compteur = 2
    A = []
    B = []
    nbargs = 2 + M * N + M
    if len(args) == nbargs:
        for i in range(0, M):
            ligne = []
            for j in range(0, N):
                ligne.append(float(args[compteur]))
                compteur += 1
            A.append(ligne)
        for i in range(0, M):
            B.append([float(args[compteur])])
            compteur += 1
        return (M, N, A, B)
    else:
        raise Exception("Le nombre d'argument(s) rentre(s) est incorrect.")

if __name__ == '__main__':
    """
    Methode "main", elle lancera la methode principale avec les valeurs
    donnees en ligne de commande.
    """
    (M, N, A, b) = formMat(ldc[1:])
    At = np.transpose(A)
    At_A = np.dot(At, A)
    At_b = np.dot(At, b)
    sol = solution_systeme(At_A, At_b)
    for i in range(0, N):
        print("%.16g" % sol[i])