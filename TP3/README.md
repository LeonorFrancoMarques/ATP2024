# Relatório do TP3:

## Autor: Leonor Franco Marques
## Data: 2024/09/25

## Resumo:

O TP3 consistiu na criação de um programa de jogo, chamado 21 fósforos. Este jogo tem duas modalidades:
* Modalidade 1 - o utilizador joga em primeiro lugar e o computador em segundo lugar. 
* Modalidade 2 - o computador joga em primeiro lugar e o utilizador em segundo lugar.

Na modalidade 1, o computador tem sempre que ganhar. Na modalidade 2, o computador ganha apenas se o utilizador tiver um erro nos seus cálculos.

As regras do jogo são simples. O jogo começa com 21 fósforos e cada jogador tira 1, 2, 3 ou 4 fósforos, na sua vez de jogar. Os jogadores jogam alternadamente e quem tirar o último fósforo perde.

O número de fósforos iniciais são 21, logo estabilizei isso na variável inicio. Pergunta-se ao jogador que modalidade quer jogar e, se a resposta for inválida, pergunta-se isso novamente. Depois de escolhida a modalidade, é perguntado qual o número de fósforos que o primeiro jogador quer retirar. Novamente, se a resposta for inválida, é perguntado isso outra vez. Após todas as jogadas, retiram-se ao número total de fósforos os fósforos que o jogador decidiu tirar. Este raciocínio é feito sempre que é perguntado ao jogador quantos fósforos ele quer retirar, até aos fósforos acabarem.

Na modalidade 1:
O utilizador é o primeiro a jogar, escolhendo quantos fósforos quer tirar (entre 1 e 4). Após retirar esses fósforos, é subtraido ao número inicial (variável inicio) o número de fósforos tirados nesta jogada. Seguidamente, é a vez do computador jogar. Este adota o método de retirar sempre uma determinada quantidade de fósforos, que deixe um número de fósforos múltiplo de 5 para o utilizador (isto pois é um número desfavorável de fósforos neste jogo). Novamente, são retirados o número de fósforos tirados pelo computador (variável fosforos_pc) ao número de fósforos totais. Este ciclo é sempre repetido até o número de fósforos finais ser 5 ou menos. Quando isto ocorre, o computador obriga o utilizador a pegar no último fósforo e assim perder o jogo!

Na modalidade 2:
O computador é o primeiro a jogar, escolhendo aleatoriamente quantos fósforos quer tirar (entre 1 e 4). O número de fósforos, que inicialmente eram 21, são atualizados. O computador, tal como na modalidade 1, deixa sempre para o utilizador múltiplos de 5. Por isso, para cada jogada, o computador deixa um número bem definido de fósforos para o utilizador. Só quando já só restam 6 fósforos, é que o computador tira um número de fósforos aleatório. O jogo acaba quando o computador deixa apenas 1 fósforo para o utilizador, forçando-o a perder. Nesta modalidade é possível ser o utilizador o vencedor, mas, para isso, este não pode cometer erros de cálculo na retirada de fósforos (se o fizer, será o computador a ganhar).

O que achei mais desafiante foi conseguir chegar ao raciocínio necessário para que o computador ganhasse sempre (o de deixar sempre um número de fósforos múltiplo de 5 para o utilizador, pois assim este ficaria numa posição desfavorável).