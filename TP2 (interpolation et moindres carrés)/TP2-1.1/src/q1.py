import scipy.linalg.lapack as sll
from sys import argv as ldc

def solution_systeme(A, B):
    sol = sll.dgesv(A, B)
    if sol[3] == 0 :
        X = []
        for i in sol[2]:
            for j in i:
                X.append([j])
        return X
    elif sol[3] > 0:
        raise Exception("Le système comporte une infinité de solutions ou est impossible.")
    else:
        raise Exception("Un des arguments n'est pas valide.")

def formMat(args):
    M = int(args[0])
    N = int(args[1])
    compteur = 2
    A = []
    B = []
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

def transpose(A):
    X = []
    for i in range(0, len(A[0])):
        list = []
        for j in range(0, len(A)):
            list.append(A[j][i])
        X.append(list)
    return X

def multMat(A, B):
    prod = []
    M = len(A)
    N = len(B)
    L = len(B[0])
    for i in range(0, M):
        list = []
        for j in range(0, L):
            som = 0
            for k in range(0, N):
                som += A[i][k] * B[k][j]
            list.append(som)
        prod.append(list)
    return prod

if __name__ == '__main__':
    """
    Methode "main", elle lancera la methode principale avec la valeur donnee en
    ligne de commande.
    """
    (M, N, A, B) = formMat(ldc[1:])
    At = transpose(A)
    prod = multMat(At, A)
    prod1 = multMat(At, B)
    sol = solution_systeme(prod, prod1)
    for i in range(0, N):
        print("%.16g" % sol[i][0])
