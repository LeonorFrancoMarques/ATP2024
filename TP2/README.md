# Relatório do TP2

## Data: 2024/09/18
## Autor: Leonor Franco Marques

## Resumo:

O TP2 consistiu na criação de um programa de jogo, que poderia ter duas modalidades: 
* 1 - o computador pensar num número e o utilizador tentar adivinhar esse número;
* 2 - o utilizador pensar num número e o computador tentar adivinhar esse número. 

Primeiramente, teve de se escolher a modalidade pretendida. Se não se obtivesse uma resposta válida (escolher entre o número 1 ou 2), era novamente questionado com que modalidade pretendia jogar. Foi com esse objetivo que foi usada a primeira estrutura cíclica while.

O número a adivinhar teria de ser compreendido entre 0 e 100 e, para isso, usei a função random (para escolher um número aleatório). Para além disso, as únicas respostas possíveis de dar à tentativa de adivinhar o tal número eram: "Acertou", "Maior" (se o número pretendido fosse maior) ou "Menor" (se o número pretendido fosse menor). No final, eram contabilizadas as tentativas que foram necessárias até chegar à solução pretendida (através do raciocínio tentativas = tentativas + 1).

De cada vez que o computador tentava adivinhar o número, o raciocínio que era feito era o de dividir o intervalo de números possíveis em dois, reduzindo assim, por cada tentativa feita, o número de respostas possíveis à sua metade.
Usei uma estrutura cíclica (while) para o raciocínio ser sempre repetido, até conseguir chegar à resposta pretendida.
Para além disso, usei estruturas condicionais, que foram essenciais para adaptar o raciocínio das próximas tentativas, tendo em conta a resposta anteriormente dada.
Foram usadas também a soma de uma unidade, quando o número era maior que o palpite, e a subtração de uma unidade, quando o número era menor que o palpite dado. Isto foi usado para restringir ainda mais o intervalo de números possíveis de dar como resposta.

Na modalidade 2, para além do já referido anterioremente, usei ainda "num" para representar a primeira tentativa e "num1" para as restantes tentativas.

Este trabalho foi bastante desafiante, principalmente devido ao raciocínio de ter de dividir o intervalo de números a meio, a cada tentativa dada, para assim encurtar significativamente as respostas possíveis. Também foi difícil encontrar a função certa para criarmos uma amostra aleatória de números.