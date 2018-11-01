import math


# Eliminação de Gauss com Pivoteamento
def resolver(A, n, b, x):
    operacoes = 0
    # Triangularização com pivoteamento
    for k in range(0, n):
        maior = math.fabs(A[k][k])
        imaior = k
        intervalo = range(k + 1, n) if (k == n - 1 or k == n - 2) else range(k + 1, k + 3)
        for i in intervalo:
            if (math.fabs(A[i][k]) > maior):
                maior = math.fabs(A[i][k])
                imaior = i
        if (imaior != k):
            # Troca a linha k com a linha imaior
            for j in range(0, n):
                aux = A[k][j]
                A[k][j] = A[imaior][j]
                A[imaior][j] = aux
            baux = b[k]
            b[k] = b[imaior]
            b[imaior] = baux
        for i in intervalo:
            m = A[i][k] / A[k][k]
            operacoes += 1
            A[i][k] = 0
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - m * A[k][j]
                operacoes += 2
            b[i] = b[i] - m * b[k]
            operacoes += 2

    x[n - 1] = b[n - 1] / A[n - 1][n - 1]

    # Resolve o sistema
    for i in range(n - 2, -1, -1):
        soma = b[i]
        intervalo = range(i + 1, n) if (i == n - 2 or i == n - 3 or i == n - 4) else range(i + 1, i + 5)
        for j in range(i + 1, n):
            soma = soma - A[i][j] * x[j]
        x[i] = soma / A[i][i]

    print("Operações realizadas: ", operacoes)