# Método de eliminação de Gauss e Método iterativo de Gauss-Seidel

Leonardo Nascimento dos Santos - [lleooNS](https://github.com/lleooNS "lleooNS")<br>
Vinícius Berger - [viniciush4](https://github.com/viniciush4 "viniciush4")

## 1. Introdução
Em Matemática, um sistema de equações lineares é um conjunto finito de equações de grau 1 aplicadas num mesmo conjunto, igualmente finito, de variáveis. Uma solução para um sistema linear é uma atribuição de valores às incógnitas que satisfazem simultaneamente todas as equações do sistema. 

Existem inúmeros métodos para resolução de sistemas lineares. Dois deles serão tratados neste trabalho: o método de “Eliminação de Gauss” e o método iterativo de “Gauss-Seidel”. O objetivo principal é comparar as soluções e o esforço computacional de cada método.

Um tipo particular de sistema linear será usado: sistemas cuja matriz de coeficientes é pentadiagonal. Matrizes pentadiagonais são aquelas cujos elementos se concentram em uma faixa central da matriz, tendo elementos não nulos nas cinco diagonais centrais e todo o restante nulo.

Levando em consideração essa particularidade, serão apresentadas as implementações dos dois métodos já mencionados, usando a linguagem python. O programa está dividido em três partes: o módulo principal (main.py), responsável por realizar a leitura dos dados do problema, invocar os métodos de resolução e calcular os erros; o módulo referente ao método “Eliminação de Gauss” (gauss.py), responsável pela resolução do sistema por meio do método de mesmo nome; e o módulo referente ao método iterativo de “Gauss-Seidel” (seidel.py), responsável pela resolução do sistema via método de Gauss-Seidel.

## 2. Método numérico 1: Eliminação de Gauss

A implementação deste método foi fortemente baseada na implementação fornecida nas aulas de laboratório (elimGauss_Com_pivot.c) e está dividida basicamente em duas partes: a triangularização e a resolução.

A parte de triangularização consiste em transformar o sistema fornecido em um sistema que possui uma matriz de coeficientes triangular superior. A maneira de se conseguir isso é percorrendo cada elemento da diagonal principal e zerando todos os elementos que estão abaixo deste na coluna via aplicação de operações matriciais elementares nas linhas correspondentes. Antes, porém, é definido o elemento pivô, ou seja, o elemento que permanecerá na diagonal principal. Este elemento deve ser o maior em valor absoluto dentre o que já está na diagonal mais os que serão zerados. Considerando o caso particular de um sistema pentadiagonal, os loops aninhados para acessar somente os elementos não nulos ficam assim:

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-30-19.png?raw=true" />

Exemplo: considerando um sistema com n=20, os elementos acessados abaixo de A[2][2] (k=2) serão A[2+1][2] e A[2+2][2], pois a função range(k+1, k+3) retorna os valores: k+1 e k+2. Considerando o mesmo sistema, o elemento percorrido abaixo de A[18][18] (k=18) é A[18+1][18], pois a função range(k+1, n) retorna o valor k+1. Isso acontece porque 18 == 20-2, uma das condições que define qual range será aplicado.

Após a triangularização, a resolução do sistema é feita de forma retroativa. Enfatizando os intervalos percorridos, temos:

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-37-00.png?raw=true" />

O intervalo percorrido à direita do elemento da diagonal foi definido como sendo de tamanho máximo igual a quatro elementos. Essa estratégia foi utilizada pois verificou-se que no pior caso, após o pivoteamento, a linha pivô irá abrigar 4 elementos após o elemento da diagonal, como exemplificado a seguir.

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-37-18.png?raw=true" />

As últimas linhas receberão tratamento especial: por não conter 4 posições a partir da diagonal, o limite superior do intervalo é definido como o fim da matriz, ou seja, o intervalo é dado por range(i+1, n). Isso evita o erro “List index out of range”. Para as demais linhas, o intervalo considera 4 elementos: range(i+1, i+5), que retornará os índices i+1, i+2, i+3 e i+4.

## 3. Método numérico 2: Gauss-Seidel

Para realizar a implementação do método de Gauss-Seidel foi necessário analisar a matriz pentadiagonal. A estratégia adotada foi realizar a solução do sistema em três partes. Analisando a matriz, foi observado que existe um padrão nas duas primeiras linhas, nas linhas do "meio" e nas duas últimas linhas.

Na implementação desse método numérico, três funções foram criadas:

  * solucionarDuasPrimeirasLinhas
  * solucionarCentro
  * solucionarDuasUltimasLinhas

As três funções realizam um comportamento semelhante, sofrendo diferenças apenas nos parâmetros que foram fornecidos e na manipulação de listas internas. Basicamente, a matriz é percorrida armazenando os elementos não nulos em uma lista auxiliar sem o elemento da diagonal.

A lista auxiliar é percorrida realizando as operações necessárias e logo após o vetor X é atualizado com a solução encontrada.

Para obter o número de iterações necessárias para encontrar a solução, foi utilizado uma estrutura de repetição que foi executada até a diferença relativa ser menor do que a tolerância fornecida. 

## 4. Resultados

### 4.1 Execução 1

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-37-39.png?raw=true" />

Vale ressaltar que o método de Gauss-Seidel precisou de 21 iterações para ser concluído.

Matriz A original:

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-37-54.png?raw=true" />

Vetor b original: 

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-38-07.png?raw=true" />

Matriz A após a aplicação do método 1 (Eliminação de Gauss): 

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-38-17.png?raw=true" />

Vetor b após a aplicação do método 1 (Eliminação de Gauss):

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-38-27.png?raw=true" />

Os elementos pintados na cor cinza são aqueles cujo valor garantidamente é nulo e portanto não são acessados durante a execução do algoritmo do método de “Eliminação de Gauss”.


### 4.2 Execução 2

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-38-40.png?raw=true" />

Comparação do esforço computacional dos métodos

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-38-51.png?raw=true" />

### 4.3 Execução 3

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-39-02.png?raw=true" />

### 4.4 Execução 4

<img src="https://github.com/viniciush4/an/blob/master/imagens/Captura%20de%20tela%20de%202019-11-14%2010-39-14.png?raw=true" />
