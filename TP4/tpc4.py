def menu():

    print("---------- MENU ----------")
    print("Opção 1 - Criar Lista")
    print("Opção 2 - Ler Lista")
    print("Opção 3 - Soma dos Elementos")
    print("Opção 4 - Média dos Elementos")
    print("Opção 5 - Maior dos Elementos")
    print("Opção 6 - Menor dos Elementos")
    print("Opção 7 - Lista Ordenada por Ordem Crescente")
    print("Opção 8 - Lista Ordenada por Ordem Decrescente")
    print("Opção 9 - Procurar um Elemento")
    print("Opção 0 - Sair")

import random

def criarLista(n):
    i = 0
    res = []
    while i < n:
        num = random.randint(1,100)
        res.append(num)
        i = i + 1
    return res

def lerLista(num):
    res = []
    for i in range(num):
        n = int(input("Introduza o número a ser adicionado à lista:"))
        res.append(n)
    return res

def somaLista(res):
    total = 0
    for c in res:
        total = total + c
    return total

def mediaLista(res):
    if len(res) == 0:
        total1 = 0
    else:
        total1 = somaLista(res)/len(res)
    return total1

def maiorLista(res):
    maior = res[0]
    for c in res[1:]:
        if c > maior:
            maior = c
    return maior

def menorLista(res):
    menor = res[0]
    for c in res[1:]:
        if c < menor:
            menor = c
    return menor

def estaOrdenadaC(res):
    cond = True
    for c in range(len(res) - 1):
        if res[c] > res[c + 1]:
            cond = False
    return cond
    
def estaOrdenadaD(res):
    cond = True
    for c in range(len(res) - 1):
        if res[c] < res[c + 1]:
            cond = False
    return cond
    
def procura(res):
    if elem in res:
        total2 = res.index(elem)
        return total2
    else:
        total2 = -1
        return total2

cond = True
res = []
while cond:
    menu()
    opcao = int(input("Escolha a opção:"))
    while opcao!=0 and opcao!=1 and opcao!=2 and opcao!=3 and opcao!=4 and opcao!=5 and opcao!=6 and opcao!=7 and opcao!=8 and opcao!=9:
        print("Resposta inválida!")
        opcao = int(input("Escolha a opção:"))

    if opcao == 1:
        n = int(input("Introduza o número de elementos que quer na lista:"))
        res = criarLista(n)
        print(res)
    elif opcao == 2:
        num = int(input("Introduza os números que quer na lista:"))
        res = lerLista(num)
        print(res)
    elif opcao == 3:
        total = somaLista(res)
        print(f"A soma de todos os elementos da lista é: {total}")
    elif opcao == 4:
        total1 = mediaLista(res)
        print(f"A média de todos os elementos da lista é: {total1}")
    elif opcao == 5:
        maior = maiorLista(res)
        print(f"O maior elemento da lista é: {maior}")
    elif opcao == 6:
        menor = menorLista(res)
        print(f"O menor elemento da lista: {menor}")
    elif opcao == 7:
        if estaOrdenadaC(res) == True:
            print("Sim, a lista está por ordem crescente!")
        else:
            print("Não, a lista não está por ordem crescente!")
    elif opcao == 8:
        if estaOrdenadaD(res) == True:
            print("Sim, a lista está por ordem decrescente!")
        else:
            print("Não, a lista não está por ordem decrescente!")
    elif opcao == 9:
        elem = int(input("Que elemento quer procurar na lista?"))
        total2 = procura(res)
        if total2 != -1:
            print(f"O elemento que procura está na posição: {total2}.")
        else:
            print(total2)
            print("O elemento que procura não está lista.")
    elif opcao == 0:
            print(res)
            print("Aplicação encerrada. Volte sempre!")
            cond = False