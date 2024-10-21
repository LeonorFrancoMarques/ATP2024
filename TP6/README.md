# Relatório do TP6:

## Autor: Leonor Franco Marques
## Data: 2024/10/16

## Resumo:

O TP6 consistiu na criação de uma aplicação para gestão de alunos. Cada turma é constituída por uma lista de alunos. Cada aluno é um tuplo onde estão presentes as suas informações: nome, ID e as suas notas. As notas constituem uma lista, que inclui: a nota do TPC, a nota do Projeto e a nota do Teste.

Esta aplicação é constituída por um menu. Nesse menu estão presentes todas as opções disponíveis:
* Opção 1 - Criar uma turma;
* Opção 2 - Inserir um aluno na turma;
* Opção 3 - Listar uma turma;
* Opção 4 - Consultar um aluno por ID;
* Opção 5 - Guardar a turma num ficheiro;
* Opção 6 - Carregar uma turma de um ficheiro;
* Opção 0 - Sair.

Primeiramente, é perguntado ao utilizador que opção quer realizar. No fim de realizar a opção escolhida, é mostrado novamente o menu ao utilizador. O menu é repetido até que o utilizador escolha a opção 0 (sair).

Ao escolher a opção 1, o programa realiza a função criarTurma(). Isto cria uma lista vazia, de modo a iniciar uma nova turma.

Ao escolher a opção 2, realiza a função inserirAluno(turma). Isto cria um aluno, pedindo todos os dados necessários para tal ao utilizador - através da função criarAluno(), que tinha sido criada anteriormente para este efeito. O aluno é descrito então pelo seu nome, ID e notas no TPC, Projeto e Teste. No final, adiciona-se esse aluno à turma (através de append). Se esse aluno já estiver na turma, avisa-se o utilizador de tal com uma mensagem.

Ao escolher a opção 3, realiza a função listarTurma(turma). Isto mostra todos os alunos, o seu ID e as suas notas.

Ao escolher a opção 4, realiza a função idAluno(turma, id). Se o ID escolhido pelo utilizador corresponder ao ID de algum dos alunos, mostram-se todas as informações do aluno com esse ID.

Ao escolher a opção 5, realiza a função guardarTurma(turma, fnome). Isto guarda toda a turma num ficheiro, cujo nome é "turma.txt". Eu coloquei um aluno por cada linha, separei os alunos uns dos outros através do símbolo :: e separei as notas através do símbolo &.

Ao escolher a opção 6, realiza a função carregarTurma(fnome). Isto carrega os dados da turma a partir de um ficheiro. Ou seja, permite recuperar os dados dos alunos anteriormente guardados, para continuar a trabalhar com estes dados.

Ao escolher a opção 0, o programa encerra com uma mensagem para o utilizador.

A minha maior dificuldade neste trabalho foi criar as funções de guardar a turma num ficheiro e a de recuperar a turma de um ficheiro.