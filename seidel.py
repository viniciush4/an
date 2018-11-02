from math import fabs

#Armazena a dimensão da matriz
n=0

#Cria uma matriz zerada e vetores zerados
A = []
b = [0.]*n
X = [0.]*n
xAnterior = [0.]*n

#Variáveis para realizar o cálculo da diferença relativa
numeroOperacoesSeidel = 0
tol = 0.0000000001
difRel = 1
difMax = 0
xMax = 0

#Função que soluciona as duas primeiras linhas da matriz
def solucionarDuasPrimeirasLinhas(linhaInicial, linhaFinal, elementoInicial, elementoFinal, addElemInicial, addElemFinal, diagonalPrincipal):
    
    #Variáveis
    limiteDiag = 0 #Variável utilizada antes e depois do elemento da diagonal
    soma = 0
    posicao = 0
    naoNulos = []
    global numeroOperacoesSeidel
    global difMax
    global xMax

    #Percorre a matriz A utilizando somente elementos não nulos
    for linha in range(linhaInicial, linhaFinal):
        for elemento in range(elementoInicial, elementoFinal):
            #Armazena os elementos em uma lista
            naoNulos.append(A[linha][elemento])

        #Remove o elemento da diagonal
        linhaSemElemDiag = naoNulos[0:limiteDiag] + naoNulos[limiteDiag+1:]
        XsemElemDiag = X[0:limiteDiag] + X[limiteDiag+1:]
        
        #Percorre a linha sem o elemento da diagonal e realiza a soma dos elementos
        for elemento in linhaSemElemDiag:
            soma += elemento*XsemElemDiag[posicao] 
            posicao += 1           
            numeroOperacoesSeidel = numeroOperacoesSeidel + 2

        #Armazena o resultado no vetor X
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
        naoNulos = []
        elementoInicial += addElemInicial
        elementoFinal += addElemFinal

#Função que soluciona a parte central da matriz
def solucionarCentro(linhaInicial, linhaFinal, elementoInicial, elementoFinal, addElemInicial, addElemFinal, diagonalPrincipal):
    
    #Variáveis
    xIni = 0
    xFim = 2
    soma = 0
    posicao = 0
    naoNulos = []
    global numeroOperacoesSeidel
    global difMax
    global xMax

    #Percorre a matriz A utilizando somente elementos não nulos
    for linha in range(linhaInicial, linhaFinal):
        for elemento in range(elementoInicial, elementoFinal):
            #Armazena os elementos em uma lista
            naoNulos.append(A[linha][elemento])

        #Remove o elemento da diagonal
        linhaSemElemDiag = naoNulos[0:2] + naoNulos[3:]
        XsemElemDiag = X[xIni:xFim] + X[xFim+1:xFim+3]
        
        #Percorre a linha sem o elemento da diagonal e realiza a soma dos elementos
        for elemento in linhaSemElemDiag:
            soma += elemento*XsemElemDiag[posicao]
            posicao += 1           
            numeroOperacoesSeidel = numeroOperacoesSeidel + 2
            
        #Armazena o resultado no vetor X      
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
        naoNulos = []
        elementoInicial += addElemInicial
        elementoFinal += addElemFinal

#Função que soluciona as duas últimas linhas da matriz
def solucionarDuasUltimasLinhas(linhaInicial, linhaFinal, elementoInicial, elementoFinal, addElemInicial, addElemFinal, diagonalPrincipal):

    #Variáveis
    xIni = n-4
    xFim = n-2
    soma = 0
    posicao = 0
    naoNulos = []
    global numeroOperacoesSeidel
    global difMax
    global xMax

    #Percorre a matriz A utilizando somente elementos não nulos
    for linha in range(linhaInicial, linhaFinal):
        for elemento in range(elementoInicial, elementoFinal):
            #Armazena os elementos em uma lista
            naoNulos.append(A[linha][elemento])

        #Remove o elemento da diagonal
        linhaSemElemDiag = naoNulos[0:2] + naoNulos[3:]
        XsemElemDiag = X[xIni:xFim] + X[xFim+1:]
        
        #Percorre a linha sem o elemento da diagonal e realiza a soma dos elementos
        for elemento in linhaSemElemDiag:
            soma += elemento*XsemElemDiag[posicao]
            posicao += 1          
            numeroOperacoesSeidel = numeroOperacoesSeidel + 2
            
        #Armazena o resultado no vetor X   
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
        naoNulos = []
        elementoInicial += addElemInicial
        elementoFinal += addElemFinal


#Função principal
def resolver(A2, n2, b2, x2, dp):

    global A
    global n
    global b
    global X
    global xAnterior

    A = A2
    n = n2
    b = b2
    X = x2

    # Preenche vetor inicial
    xAnterior = [0.] * n
    for i in range(0, n):
        xAnterior[i] = b[i]/A[i][i]

    #Variáveis
    global difRel
    global difMax
    global xMax
    numeroIteracoesSeidel = 0

    # print(A, n, b, X, difRel, difMax, xMax, numeroIteracoesSeidel)
    
    #Realiza o método de Gauss Seidel
    while(difRel > tol and numeroIteracoesSeidel < 700):

        #Variáveis
        difMax = 0
        xMax = 0
        numeroIteracoesSeidel += 1

        #Realiza o método de GaussSeidel
        #Parâmetros: linhaInicial, linhaFinal, elementoInicial, elementoFinal, addElemInicial, addElemFinal, diagonalPrincipal
        solucionarDuasPrimeirasLinhas(0,2,0,3,0,1,dp)
        solucionarCentro(2,n-2,0,5,1,1,dp)
        solucionarDuasUltimasLinhas(n-2,n,n-4,n,1,0,dp)

        #Calcula a diferença relativa
        difRel = difMax / xMax

    #Imprime o vetor X de soluções
    # print('O vetor X de soluções:\n\n',X)
    #Imprime o total de iterações
    print('Total de iterações: {}'.format(numeroIteracoesSeidel))
    #Imprime o total de operações realizadas
    print('Operações realizadas: {}'.format(numeroOperacoesSeidel))

