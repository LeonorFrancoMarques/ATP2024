# Relatório do TP5:

## Autor: Leonor Franco Marques
## Data: 2024/10/09

## Resumo:

O TP5 consistiu na criação de um programa para gerir um cinema de um determinado centro comercial.

Nesse centro comercial, existe um cinema com um determinado número de salas, ou seja, o cinema é uma lista de salas. Cada sala tem a sua lotação máxima, o número de bilhetes já vendidos e um filme associado, ou seja, cada sala é um tuplo composto por estes três elementos. Cada lugar é identificado por um número inteiro e cada filme é uma string. Os bilhetes vendidos são uma lista de números inteiros.

Esta aplicação tem um menu, onde se encontram todas as operações possíveis de realizar. Cada opção tem o seu número correspondente:
* Opção 1 - Listar Cinema
* Opção 2 - Disponibilidade de Lugares
* Opção 3 - Vender Bilhete
* Opção 4 - Listar Disponibilidade de Salas
* Opção 5 - Existe Sala
* Opção 6 - Inserir Sala Nova
* Opção 7 - Remover Sala
* Opção 0 - Sair

Enquanto não for escolhida uma destas opções, o programa não avança, pois é uma opção inválida. Quando for escolhida uma opção válida, é efetuada a função correspondente a esta.
Ao escolher a opção 1, vai realizar a função listar( cinema ). Esta função lista todos os filmes disponíveis em exibição.
Ao escolher a opção 2, vai realizar a função disponivel( cinema, filme, lugar ). Esta função verifica se um determinado lugar está disponível numa sala. Se o lugar não estiver ocupado retorna a condição True, se estiver ocupado retorna a condição False.
Ao escolher a opção 3, vai realizar a função vendebilhete( cinema, filme, lugar ). Esta função vende um bilhete para um determinado lugar escolhido, se este estiver disponível. Assim, este número de lugar é adicionado à lista de bilhetes já vendidos, atualizando a função como cinema_novo.
Ao escolher a opção 4, vai realizar a função listardisponibilidades( cinema ). Isto atualiza os dados, para obtermos assim os lugares disponíveis em cada sala. Faz isto subtraindo os bilhetes vendidos ao número total de lugares da sala.
Ao escolher a opção 5, vai realizar a função existeSala ( cinema, sala ). Esta função mostra se a sala que estamos a tentar adicionar, não é uma sala já existente no cinema.
Ao escolher a opção 6, vai realizar a função inserirSala ( cinema, sala ). Esta função vai inserir uma nova sala no cinema, se esta não existir já no cinema. Se esta sala já existir, é impressa uma mensagem a avisar de tal situação.
Ao escolher a opção 7, vai realizar a função removerSala( cinema, filme ). Esta função remove uma sala associada a um determinado filme. Seguidamente, é criada uma nova sala de cinema, atualizada com estes novos dados.
Ao escolher a opção 0, encerra a aplicação.
Todo este ciclo é realizado até o utilizador decidir sair da aplicação.

Este trabalho foi desafiante devido às múltiplas designações diferentes que se teve de atribuir a diferentes variáveis, pois chegou a um momento do trabalho em que isto se tornou um pouco confuso.