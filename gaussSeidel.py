import numpy as np
from math import fabs

n=int(input("Dimensão do sistema (n): "))
# Cria uma matriz zerada e um vetor b zerado
A = np.zeros((n,n), float)
#b = np.zeros(n, float)
b = [0.]*n
X = [0.]*n
xAnterior = [0.]*n
matrizSeidel = []
numeroOperacoesSeidel = 0
tol = 0.0000000001
difRel = 1
difMax = 0
xMax = 0

def removerElementosNaoNulos(inicioVarI, fimVarI, inicioVarJ, fimVarJ, incrementaIniVarJ, incrementaFimVarJ):
    
    naoNulos = []
    for i in range(inicioVarI, fimVarI):
        for j in range(inicioVarJ, fimVarJ):
            #Armazena os elementos em uma lista
            naoNulos.append(A[i][j])

        #Armazena a lista na matriz
        matrizSeidel.append(naoNulos)

        #Atualiza as variáveis
        naoNulos = []
        inicioVarJ += incrementaIniVarJ
        fimVarJ += incrementaFimVarJ

def solucionarDuasPrimeirasLinhas(diagonalPrincipal):
    
    limiteDiag = 0
    soma = 0
    posicao = 0
    global numeroOperacoesSeidel
    global difMax
    global xMax

    for linha in matrizSeidel[:2]:
        #Remove o elemento da diagonal
        linhaSemElemDiag = linha[0:limiteDiag] + linha[limiteDiag+1:]
        XsemElemDiag = X[0:limiteDiag] + X[limiteDiag+1:]
        
        for elemento in linhaSemElemDiag:
            soma += elemento*XsemElemDiag[posicao] 
            posicao += 1           
            numeroOperacoesSeidel = numeroOperacoesSeidel + 2

        #Armazena o resultado 
        X[limiteDiag] = (b[limiteDiag] - soma) / diagonalPrincipal
        numeroOperacoesSeidel = numeroOperacoesSeidel + 2

        #Calcula a diferença relativa
        if(fabs(X[limiteDiag] - xAnterior[limiteDiag]) > difMax):
            difMax = fabs(X[limiteDiag] - xAnterior[limiteDiag])

        if(fabs(X[limiteDiag]) > xMax):
            xMax = fabs(X[limiteDiag])

        #Atualiza as variáveis
        xAnterior[limiteDiag] = X[limiteDiag]
        limiteDiag += 1
        posicao = 0
        soma = 0

def solucionarCentro(diagonalPrincipal):
    
    xIni = 0
    xFim = 2
    soma = 0
    posicao = 0
    global numeroOperacoesSeidel
    global difMax
    global xMax

    for linha in matrizSeidel[2:n-2]:
        #Remove o elemento da diagonal
        linhaSemElemDiag = linha[0:2] + linha[3:]
        XsemElemDiag = X[xIni:xFim] + X[xFim+1:xFim+3]
        
        for elemento in linhaSemElemDiag:
            soma += elemento*XsemElemDiag[posicao]
            posicao += 1           
            numeroOperacoesSeidel = numeroOperacoesSeidel + 2
            

        #Armazena o resultado        
        X[xFim] = (b[xFim] - soma) / diagonalPrincipal
        numeroOperacoesSeidel = numeroOperacoesSeidel + 2
        
        #Calcula a diferença relativa
        if(fabs(X[xFim] - xAnterior[xFim]) > difMax):
            difMax = fabs(X[xFim] - xAnterior[xFim])

        if(fabs(X[xFim]) > xMax):
            xMax = fabs(X[xFim])

        #Atualiza as variáveis
        xAnterior[xFim] = X[xFim]
        xFim += 1
        xIni += 1
        posicao = 0
        soma = 0

def solucionarDuasUltimasLinhas(diagonalPrincipal):

    xIni = n-4
    xFim = n-2
    soma = 0
    posicao = 0
    global numeroOperacoesSeidel
    global difMax
    global xMax

    for linha in matrizSeidel[n-2:]:
        #Remove o elemento da diagonal
        linhaSemElemDiag = linha[0:2] + linha[3:]
        XsemElemDiag = X[xIni:xFim] + X[xFim+1:]
        
        for elemento in linhaSemElemDiag:
            soma += elemento*XsemElemDiag[posicao]
            posicao += 1          
            numeroOperacoesSeidel = numeroOperacoesSeidel + 2
            
        #Armazena o resultado    
        X[xFim] = (b[xFim] - soma) / diagonalPrincipal
        numeroOperacoesSeidel = numeroOperacoesSeidel + 2
        
        #Calcula a diferença relativa
        if(fabs(X[xFim] - xAnterior[xFim]) > difMax):
            difMax = fabs(X[xFim] - xAnterior[xFim])

        if(fabs(X[xFim]) > xMax):
            xMax = fabs(X[xFim])

        #Atualiza as variáveis
        xAnterior[xFim] = X[xFim]
        xFim += 1
        xIni += 1
        posicao = 0
        soma = 0


# Função principal
def main():

    global difRel
    global difMax
    global xMax
    numeroIteracoes = 0

    # Realiza as leituras
    
    da=float(input("Valor da diagonal a (da): "))
    db=float(input("Valor da diagonal b (db): "))
    dp=float(input("Valor da diagonal principal (dp): "))
    dc=float(input("Valor da diagonal c (dc): "))
    dd=float(input("Valor da diagonal d (dd): "))

    
    
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
    print('\n',b,'\n')


    #Remove os elementos não nulos duas primeiras linhas
    removerElementosNaoNulos(0,2,0,3,0,1)

    #Remove os elementos não nulos do meio da matriz
    removerElementosNaoNulos(2,n-2,0,5,1,1)

    #Remove os elementos não nulos duas últimas linhas
    removerElementosNaoNulos(n-2,n,n-4,n,1,0)

    #Imprime a matriz sem os elementos nulos
    print('Matriz sem elementos nulos')
    print(matrizSeidel,'\n')


    #Falta calcular a tolerância

    

    while(difRel > tol and numeroIteracoes < 500):

        difMax = 0
        xMax = 0
        numeroIteracoes += 1

        #Realiza o método de GaussSeidel
        solucionarDuasPrimeirasLinhas(dp)
        print('Duas linhas iniciais solucionadas\n',X,'\n')

        solucionarCentro(dp)
        print('Parte central solucionada\n',X,'\n')

        solucionarDuasUltimasLinhas(dp)
        print('Duas últimas linhas solucionadas\n',X,'\n')

        #Imprime o total de operações realizadas
        print('Total de operações realizadas = {} \n'.format(numeroOperacoesSeidel))

        #Calcula a diferença relativa
        difRel = difMax / xMax

        print('\nDiferença Relativa = {}, DifMax = {}, xMax = {}\n'.format(difRel, difMax, xMax))


    print('Total de Iterações = {}\n'.format(numeroIteracoes))    

# Chama a função principal
main()
