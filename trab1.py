import numpy as np

# Função principal
def main():
    # Realiza as leituras
    n=int(input("Dimensão do sistema (n): "))
    da=float(input("Valor da diagonal a (da): "))
    db=float(input("Valor da diagonal b (db): "))
    dp=float(input("Valor da diagonal principal (dp): "))
    dc=float(input("Valor da diagonal c (dc): "))
    dd=float(input("Valor da diagonal d (dd): "))

    # Cria uma matriz zerada e um vetor b zerado
    A = np.zeros((n,n), float)
    b = np.zeros(n, float)
    
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

    # Imprime a matriz
    print(A)
    
    # Gera um vetor b tal que a solução seja x=[1.0, 1.0, ... 1.0]
    for i in range(0,n):
        for j in range(0,n):
            b[i] = b[i]+A[i][j]
    
    # Imprime o vetor b
    print(b)

# Chama a função principal
main()