# Relatório do TP4:

## Autor: Leonor Franco Marques
## Data: 2024/10/02

## Resumo:

O TP4 consistiu na criação de uma aplicação que manipula números inteiros. Esta aplicação foi criada em Python.

Esta aplicação tem um menu, onde se encontram todas as operações possíveis de realizar. Cada opção tem o seu número correspondente:
*(1) Criar Lista 
*(2) Ler Lista
*(3) Soma
*(4) Média
*(5) Maior
*(6) Menor
*(7) Está ordenada por ordem crescente
*(8) Está ordenada por ordem decrescente
*(9) Procura um elemento
*(0) Sair

Primeiramente, é perguntado ao utilizador qual a opção que este quer escolher (entre 0 e 9). Se o utilizador não escolher uma opção válida, é pedido para escolher outra opção. Enquanto a opção for diferente da opção Sair: é realizada a função correspondente ao número escolhido e, depois de executada, é novamente colocado no monitor o menu. Se o utilizador escolher a opção Sair: o programa encerra com uma mensagem. É para isto que se criou o menu, ou seja, para a aplicação executar a função que o utilizador escolher no menu.

Para cada opção foi construída uma função específica, de modo a obtermos o resultado esperado. Para ser uma amostra aleatória, usamos a variável random. 

Na opção 1, é gerada uma lista aleatória com números entre 1 e 100. O tamanho desta lista é escolhido pelo utilizador.
Na opção 2, é o utilizador que cria e escolhe o tamanho da lista e os seus elementos.
Na opção 3, é calculada a soma dos elementos da lista (usa-se a variável total para representar a soma e c para representar um caractér).
Na opção 4, é calculada a média dos elementos da lista. Neste caso, foi usada a função soma já criada anteriormente na opção 3. A esse soma dividi o número de elementos da lista, obtendo-se assim a média. Se o tamanho da lista for zero, a média será também zero.
Na opção 5 e 6, é retirado o maior e o menor elemento da lista, respetivamente. Para isso, criei uma função que tem como base a comparação do primeiro elemento da lista com os restantes.
Na opção 7 e 8, é verificado se a lista está ordenada por ordem crescente ou decrescente, respetivamente. A resposta, neste caso, não é um valor numérico (é Sim ou Não). Aqui, comparam-se todos os elementos com o respetivo elemento que o procede na lista, para ver se estão devidamente ordenados.
Na opção 9, procura-se um determinado elemento e dá-nos como resposta a posição deste tal elemento na lista. Para isso, usei o index (que nos dá a posição do elemento na lista). Se esse elemento não existir na lista, é retornado -1.
Na opção 0, a aplicação é encerrada e é mostrada no monitor uma mensagem de despedida.

Este trabalho foi desafiante, pois inicialmente eu tinha designado, por exemplo, na opção da soma dos elementos da lista, o seu total como soma. Ora, deste modo, o computador não me estava a dar os resultados pretendidos, pois estava a associar o resultado soma à operação soma. Isto aconteceu também com a média dos elementos. Visto isto, tive de refazer e alterar alguns elementos nas funções, para que tudo funcionasse corretamente no final.
