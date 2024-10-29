# Relatório do TP6:

## Autor: Leonor Franco Marques
## Data: 2024/10/23

## Resumo:

O TP7 consistiu na criação de uma aplicação sobre meteorologia, em Python. Cada dia é constituída por uma data, temperatura máxima, temperatura mínima e a precipitação. Na data temos o ano, mês e dia.

Esta aplicação é constituída por um menu. Nesse menu estão presentes todas as opções disponíveis:
* Opção 1 - Criar a tabela meteorológica
* Opção 2 - Listar a tabela meteorológica
* Opção 3 - Temperatura média
* Opção 4 - Guardar a tabela meteorológica
* Opção 5 - Carregar a tabela meteorológica
* Opção 6 - Temperatura mínima
* Opção 7 - Amplitude térmica
* Opção 8 - Precipitação máxima
* Opção 9 - Precipitação superior a p
* Opção 10 - Maior número consecutivo de dias com precipitação abaixo de p
* Opção 11 - Gráficos da temperatura máxima, temperatura mínima e pluviosidade
* Opção 0 - Sair da aplicação

Primeiramente, é perguntado ao utilizador que opção quer realizar. No fim de realizar a opção escolhida, é mostrado novamente o menu ao utilizador. O menu é repetido até que o utilizador escolha a opção 0 (sair).

A opção 1 cria a tabela meteorológica com todos os dados descritos anteriomente (data, temperatura máxima, temperatura mínima e precipitação).
A opção 2 lista essa tabela.
A opção 3 calcula a temperatura média de cada dia (somando a temperatura mínima com a máxima, e dividindo isto por dois). Esta devolve a data e a temperatura média.
A opção 4 guarda a tabela a tabela num ficheiro denominado de "meteorologia.txt".
A opção 5 carrega essa tabela a partir do ficheiro. Separei os elementos da data por "-" e os restantes termos por "&".
A opção 6 calcula a temperatura mínima de todos os registos da tabela.
A opção 7 calcula a amplitude térmica, ou seja, a diferença entre a temperatura máxima e a mínima. Esta devolve também a data.
A opção 8 diz-nos qual foi o dia com maior precipitação e o valor dessa tal precipitação.
A opção 9 indica os dias em que a precipitação foi superior a um determinado valor p de precipitação.
A opção 10 indica o número de dias consecutivos em que a precipitação foi inferior a um determinado valor p.
A opção 11 desenha os gráficos de linha da temperatura mínima e máxima e um gráfico de barras para a pluviosidade (precipitação diária).