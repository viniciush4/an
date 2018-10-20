import numpy as np
import math

# Função principal
def main():
	
    for i in range(3,0,-1):
        print(i)
    
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
    X = np.zeros(n, float)
    
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
	 
    # Triangularização
    for k in range(0,n):
        maior = math.fabs(A[k][k])
        imaior = k
        for i in range(k+1, n):
            if(math.fabs(A[i][k]) > maior):
                maior = math.fabs(A[i][k])
                imaior=i
        if(imaior != k):
            # Troca a linha k com a linha imaior
            for j in range(0,n):
                aux = A[k][j];
                A[k][j] = A[imaior][j];
                A[imaior][j] = aux;
            baux = b[k]
            b[k] = b[imaior]
            b[imaior] = baux
        for i in range(k+1, n):
             m = A[i][k]/A[k][k]
             A[i][k]=0
             for j in range(k+1, n):
                 A[i][j]= A[i][j]- m*A[k][j]
             b[i]= b[i]- m*b[k]
  
    # Imprime a matriz
    print(A)
    
    # Imprime o vetor b
    print(b)
    
    X[n-1]= b[n-1]/A[n-1][n-1]
    
    for i in range(n-2, 0, -1):
        soma = b[i]
        for j in range(i+1, n):
            soma = soma - A[i][j]*X[j]
        X[i]= soma/A[i][i]


    # Imprime o vetor b
    print(X)
			
			
			
			
			

# Chama a função principal
main()
