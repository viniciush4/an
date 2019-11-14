# Método de eliminação de Gauss e Método iterativo de Gauss-Seidel

## 1. Introdução
Em Matemática, um sistema de equações lineares é um conjunto finito de equações de grau 1 aplicadas num mesmo conjunto, igualmente finito, de variáveis. Uma solução para um sistema linear é uma atribuição de valores às incógnitas que satisfazem simultaneamente todas as equações do sistema. 

Existem inúmeros métodos para resolução de sistemas lineares. Dois deles serão tratados neste trabalho: o método de “Eliminação de Gauss” e o método iterativo de “Gauss-Seidel”. O objetivo principal é comparar as soluções e o esforço computacional de cada método.

Um tipo particular de sistema linear será usado: sistemas cuja matriz de coeficientes é pentadiagonal. Matrizes pentadiagonais são aquelas cujos elementos se concentram em uma faixa central da matriz, tendo elementos não nulos nas cinco diagonais centrais e todo o restante nulo.

Levando em consideração essa particularidade, serão apresentadas as implementações dos dois métodos já mencionados, usando a linguagem python. O programa está dividido em três partes: o módulo principal (main.py), responsável por realizar a leitura dos dados do problema, invocar os métodos de resolução e calcular os erros; o módulo referente ao método “Eliminação de Gauss” (gauss.py), responsável pela resolução do sistema por meio do método de mesmo nome; e o módulo referente ao método iterativo de “Gauss-Seidel” (seidel.py), responsável pela resolução do sistema via método de Gauss-Seidel.

## 2. Método numérico 1: Eliminação de Gauss

A implementação deste método foi fortemente baseada na implementação fornecida nas aulas de laboratório (elimGauss_Com_pivot.c) e está dividida basicamente em duas partes: a triangularização e a resolução.

A parte de triangularização consiste em transformar o sistema fornecido em um sistema que possui uma matriz de coeficientes triangular superior. A maneira de se conseguir isso é percorrendo cada elemento da diagonal principal e zerando todos os elementos que estão abaixo deste na coluna via aplicação de operações matriciais elementares nas linhas correspondentes. Antes, porém, é definido o elemento pivô, ou seja, o elemento que permanecerá na diagonal principal. Este elemento deve ser o maior em valor absoluto dentre o que já está na diagonal mais os que serão zerados. Considerando o caso particular de um sistema pentadiagonal, os loops aninhados para acessar somente os elementos não nulos ficam assim:

```
# Para cada elemento na diagonal principal
for k in range(0, n):
   [...]

   # Define o intervalo que será percorrido abaixo do elemento.
   # Se for o último ou o penúltimo elemento, o intervalo será
   # [k+1, n) para evitar "List index out of range". 
   # Se for qualquer outro elemento da diagonal principal o 
   # intervalo será [k+1, k+3) para não acessar elementos nulos
   intervalo = range(k+1, n) if (k == n-1 or k == n-2) else range(k+1, k+3)
```

## Comparação das soluções e do esforço computacional na resolução de um sistema de equações lineares para o caso de um problema pentadiagonal
