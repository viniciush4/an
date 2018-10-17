// Resolver um sistema linear via Eliminação de Gauss, SEM PIVOTEAMENTO (ou seja, só se aplica qdo não houver necessidade da troca de linhas)
#include<stdio.h>
#include<math.h>
#define N 100

int main()
{
    float A[N][N],X[N], soma, b[N], m, maior,aux, baux;
    //double A[N][N],X[N], soma, b[N], m, maior,aux, baux;
    int n,k,i,j, imaior;

//------------------------------
//A,  Cheia 4x4 exemplo (1)
     n=4;
     A[0][0]=0.3;    A[0][1]=10.0; A[0][2]=0.3; A[0][3]=4.0;
     A[1][0]=1.0;    A[1][1]=-4.3; A[1][2]=0.5; A[1][3]=2.0;
     A[2][0]=5.5;    A[2][1]=-1.1;  A[2][2]=5.0; A[2][3]=0.0;
     A[3][0]=29.0;   A[3][1]=2.3;  A[3][2]=3.0; A[3][3]=8.2;

//A,  Cheia 4x4 Exemplo (2)
     n=4;
     A[0][0]=60.0;    A[0][1]=10.0; A[0][2]=0.3; A[0][3]=4.0;
     A[1][0]=1.0;    A[1][1]=-4.5; A[1][2]=0.5; A[1][3]=2.0;
     A[2][0]=5.5;    A[2][1]=-1.1;  A[2][2]=10.0; A[2][3]=0.0;
     A[3][0]=29.0;   A[3][1]=2.3;  A[3][2]=3.0; A[3][3]=40.2;


// Gerando um vetor b tal que a solução seja x_sol=[1.0,1.0,...,1.0,1.0] 
//  ou seja, calculando  b=A*x
    for(i=0;i< n;i++)
    {
      b[i]=0;
      for(j=0;j< n;j++)
      {
           b[i]= b[i] + A[i][j];
       }
      }
//----------------------------------------------

//   exemplo 1, exemplo feito em sala  sobre Iterativos
     n=3;
     // A
     A[0][0]=5;  A[0][1]=1; A[0][2]=1; 
     A[1][0]=1;  A[1][1]=10; A[1][2]=8; 
     A[2][0]=2;  A[2][1]=1.5; A[2][2]=4; 
    // B 
     b[0]=2;  b[1]=3;  b[2]= -1;

// --------------------------------
// Mostrando os dados do problema  
    printf("\n --- Sistema  fornecido ---\n");
    for(i=0;i< n;i++)
    {
      for(j=0;j< n;j++)
      {
        printf("  %10.3f ", A[i][j]);
      }
      printf(" | b[%d]: %10.3f\n", i, b[i]);
    }
    printf(" -------------------------------------\n");  
// fim de  mostrando os dados do problema

//     Triangularizacao 
    for(k=0;k<(n-1);k++)
    {
        printf("\n\n---------------   Etapa %d  -------------\n", k);
        //identificar qual eh a melhor linha pivo
        maior=fabs(A[k][k]);
        imaior=k;
	      for(i=k+1;i<n;i++) 
        {
          if(fabs(A[i][k])> maior){maior=fabs(A[i][k]); imaior=i;}
        }
	      if(imaior!=k)// Trocar linha k com linha imaior
        {
	          for(j=0;j<n;j++)
           {
		          aux=A[k][j];
	          	A[k][j]=A[imaior][j];
	          	A[imaior][j]=aux;
           }
	          baux=b[k];
           b[k]=b[imaior];
	         b[imaior]=baux;
	      }// fim do if troca de linhas
       // melhor linha pivo identificada
       for(i=(k+1);i<n;i++)
       {
           m = A[i][k]/A[k][k];
           A[i][k]=0; // para visualização da matriz triangularizada
           //A[i][k]=A[i][k]- m*A[k][k];; // para ver o valor que fica na memória
           printf("   m = %f;", m);
         
           for(j=(k+1);j<n;j++)
           {
              A[i][j]= A[i][j]- m*A[k][j];
           } // fim  j
           b[i]= b[i]- m*b[k];

        } // fim linha i

    // Mostrando a matriz intermediaria
      printf("\n - Matriz apos a etapa %d ------\n", k);
      for(i=0;i< n;i++)
     {
       for(j=0;j< n;j++)
       {
        printf("  %10.3f ", A[i][j]);
        }
        printf(" | b[%d]: %10.3f\n", i, b[i]);
      }
    } // fim etapa K

// Mostrando a matriz triangularizada 
    printf("\n \n --- Matriz triangularizada ---\n");
    for(i=0;i< n;i++)
    {
      for(j=0;j< n;j++)
      {
        printf("  %10.3f ", A[i][j]);
      }
      printf(" | b[%d]: %10.3f\n", i, b[i]);
    }
    printf(" -------------------------------------\n");  


//   resolvendo  o sistema  Triangular Superior via Subst. Regressiva 
    // calculo de x da última equação (indice: n-1, em C)
    X[n-1]= b[n-1]/A[n-1][n-1]; 

    // Calculo das variáveis: começando  da penúltima linha (n-2) até a primeira (indice é zero).
    for(i=(n-2);i>=0;i--)  
    {
      soma=b[i];
      for(j=i+1;j<n;j++)
      {
        soma = soma - A[i][j]*X[j];
      }
      X[i]= soma/A[i][i];
    }
  
   // Mostrando a solucao
    printf("\n O Vetor solucao:\n");
    for(i=0;i< n;i++)
    {
       printf(" X[%d]: %.7f\n", i, X[i]);
    }

    printf(" -- fim --\n");   
    return(0);  
}
