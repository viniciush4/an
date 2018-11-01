import math
import numpy as np
import gauss
import seidel


# Exibe o erro existente no vetor
# solução x, considerando que a so-
# lução correta é o vetor [1, 1, ... 1]
def calcularErro(x):
    e = np.zeros(len(x), float)
    emax = 0
    esoma = 0
    for i, y in enumerate(x):
        e[i] = math.fabs(y - 1)
        esoma += e[i]
        if e[i] > emax:
            emax = e[i]
    print("Erro máximo: ", emax)
    print("Erro médio: ", esoma/len(x))


# Função principal
def main():

    # Realiza as leituras
    n=int(input("Dimensão do sistema (n): "))
    da=float(input("Valor da diagonal a (da): "))
    db=float(input("Valor da diagonal b (db): "))
    dp=float(input("Valor da diagonal p (dp): "))
    dc=float(input("Valor da diagonal c (dc): "))
    dd=float(input("Valor da diagonal d (dd): "))

    # Cria uma matriz e vetores b e x zerados
    A = np.zeros((n,n), float)
    b = [0.]*n
    x = [0.]*n

    # Preenche as cinco diagonais
    for i in range(0,n):
        for j in range(0,n):
            d = i - j
            if d == 2:
                A[i][j] = da
            elif d == 1:
                A[i][j] = db
            elif d == 0:
                A[i][j] = dp
            elif d == -1:
                A[i][j] = dc
            elif d == -2:
                A[i][j] = dd

    # Gera um vetor b tal que a solução seja x=[1.0, 1.0, ... 1.0]
    for i in range(0,n):
        for j in range(0,n):
            b[i] = b[i]+A[i][j]

    print("\n\n\nMÉTODO ELIMINAÇÃO DE GAUSS:")
    Ag = A.copy()
    bg = b.copy()
    xg = x.copy()
    gauss.resolver(Ag, n, bg, xg)
    calcularErro(xg)

    print("\n\n\nMÉTODO GAUSS-SEIDEL:")
    As = A.copy()
    bs = b.copy()
    xs = x.copy()
    seidel.resolver(As, n, bs, xs, dp)
    calcularErro(xs)


# Chama a função principal
main()