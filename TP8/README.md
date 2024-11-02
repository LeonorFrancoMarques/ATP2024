# Relatório do TP8:

## Autor: Leonor Franco Marques
## Data: 2024/10/30

## Resumo:

O TP8 consistiu na elaboração de 3 TPC's diferentes:
* TPC1: especificar 3 listas em compreensão;
* TPC2: criar 4 funções;
* TPC3: definir funções de manipulação e consulta de uma rede social.

No TPC1:
* Alínea a: criou-se uma variável que comparava os elementos de duas listas e devolvia os elementos que não são comuns às listas.
* Alínea b: retirava-se de um texto, todas as palavras com mais de três letras. Usei a variável textofinal, para o texto onde foi aplicado o split (onde retirei os espaços brancos).
* Alínea c: devolve o índice e o valor de um determinado elemento de uma lista. Para isso usei o index, que nos dá então os índices e somei-lhe 1 unidade, para a contagem dos índices começar em 1 e não em 0.

No TPC2:
* Alínea a: criou-se uma função que nos mostra quantas vezes uma subtring aparece numa string. Para isso foi preciso analisar a string, secção a secção, para ver se a substring lá aparecia. Essa análise só era possível enquanto o tamanho da substring + i fosse inferior ao tamanho da string. Sempre que a substring aparecia na string, o contador adicionava 1 ao seu valor. A análise começa na posição i e termina em i + tamanho da substring.   
* Alínea b: criou-se uma função que recebe uma lista de números inteiros positivos e devolve o menor produto possível entre os 3 números mais pequenos. Para isso, eu ordenei a lista (através de sorted(lista)) e depois multiplicou os números dessa lista ordenada que estavam na posição 0, 1 e 2, e que, portanto, correspondiam aos elementos mais pequenos da lista.
* Alínea c: criou-se uma função que recebe um número inteiro e que soma os seus dígitos, sucessivamente, até este ficar com apenas 1 dígito. Isso só poderia acontecer enquanto o número tiver mais de um dígito (n >= 10). Começa-se com a soma igualada a zero e vai-se somando a esta os dígitos do número. No final, o número devolvido é igual a essa soma (n = soma).
* Alínea d: criou-se uma função que recebe duas strings e devolve o índice da segunda string na primeira string. Se essa string2 não estivesse na string1 era devolvido o resultado -1. Para isso, usou-se o i que nos daria o índice da string2.

No TPC3:
Criaram-se algumas funções de manipulação de uma rede social, que tinha a sua informação armazenada em vários dicionários. Esta rede social tem vários parâmetros: ID, conteúdo, autor, data de criação e comentários. Por sua vez, os comentários são uma lista de dicionários, com chaves: comentário e autor.
Este tpc tinha várias alíneas e em cada uma era criada uma função diferente:
* Alínea a: devolve o número de posts publicados na rede social. Usa-se a função len para contar o número de posts.
* Alínea b: devolve os posts de um determinado autor. Para isso, são percorridos todos os posts da rede social até encontrar os posts associados ao nome do autor fornecido.
* Alínea c: devolve a lista de autores de posts ordenada alfabeticamente. Para isso, são percorridos todos os posts da rede social e se o autor ainda não estiver na lista é adicionado a esta. No final, usa-se sorted() para ordenar a lista alfabeticamente.
* Alínea d: adiciona um novo post à rede social e devolve a nova rede social atualizada com este novo post. No entanto, o campo do ID tem de ser calculado consoante os posts já existentes.
* Alínea e: apaga um post da rede social. Para isso, são percorridos todos os posts da rede social e se não corresponder ao ID do post que quero apagar, esses posts são adicionados a uma nova lista para a rede social.
* Alínea f: devolve  a contagem de posts de cada autor, na forma de um dicionário. Aqui criei um dicionário e, ao percorrer todos os posts, se esse autor não estiver no dicionário, é acrescentado uma unidade à distribuição. Se esse autor já estiver no dicionário, é devolvida uma nova entrada com o valor igual a 1.
* Alínea g: devolve a lista de posts comentados por um autor em específico. Ou seja, se o autor que foi recebido pela função igualar a um autor de algum comentário, são devolvidos os posts comentados por este. 

A parte mais desafiante para mim foi o tpc3, pois dicionários é uma matéria que, neste momento, ainda não me está muito bem consolidada.