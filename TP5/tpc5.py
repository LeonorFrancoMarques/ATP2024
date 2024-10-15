def menu():
        print(""""
        (1) Listar Cinema
        (2) Disponibilidade de Lugares
        (3) Vender Bilhete
        (4) Listar Disponibilidades de Salas
        (5) Existe Sala 
        (6) Inserir Sala Nova
        (7) Remover Sala
        (0) Sair
        """)

import random

def listar( cinema ):
    print("----------Filmes em exibição:----------")
    filmes = []
    for sala in cinema:
        filmes.append(sala[2])
        print(f"Filmes: {filmes}")
    return

def disponivel( cinema, filme, lugar ):
    cond = True
    for sala in cinema:
        if filme in sala[2]:
            vendidos = sala[1]
            if lugar in vendidos:
                cond = False
    return cond

def vendebilhete( cinema, filme, lugar ):
    for sala in cinema:
        if sala[2] == filme:
            if lugar <= sala[0]:
                vendidos = sala[1]
                vendidos.append(lugar)
                print("O bilhete foi vendido!")
            elif lugar > sala[0]:
                print("O lugar já está ocupado, o bilhete não pode ser vendido!")   
    return cinema

def listardisponibilidades( cinema ):
    print("----------Disponibilidade das Salas----------")
    for sala in cinema:
        lugares_disponiveis = sala[0] - len(sala[1])
        print(f"Filme: {sala[2]}, Lugares disponíveis:{lugares_disponiveis}")
    return cinema

def existeSala( cinema, sala ):
    cond = False
    for s in cinema:
        if s[2] == sala[2]:
            cond = True
    return cond

def inserirSala( cinema, sala ):
    if not existeSala( cinema, sala ):
        cinema.append(sala)
    else:
        print("Essa sala já existe!")
    return cinema

def removerSala( cinema, filme ):
    cinema_novo = [sala for sala in cinema if sala[2]!= filme]
    return cinema_novo

cond = True
cinema = []
while cond: 

        opcao = int(input("Escolha uma opção:"))

        while opcao != 0 and opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4 and opcao != 5 and opcao != 6:
            print("Opção inválida, digite a sua opção novamente!") 
            opcao = int(input("Escolha uma opção:"))   

        if opcao == 1:
            listar( cinema )
        elif opcao == 2:
            filme = input("Introduza o nome do filme escolhido:")
            lugar = int(input("Introduza o número do lugar escolhido:"))
            if disponivel( cinema, filme, lugar ):
                print("O lugar está disponível!")
            else:
                print("O lugar já está ocupado!")
        elif opcao == 3:
            filme = input("Introduza o nome do filme escolhido:")
            lugar = int(input("Introduza o número do lugar escolhido:"))
            if disponivel( cinema, filme, lugar ):
                cinema = vendebilhete ( cinema, filme, lugar )
        elif opcao == 4:
            listardisponibilidades( cinema )
        elif opcao == 5:
            existeSala( cinema, sala )
        elif opcao == 6:
            filme = input("Introduza o nome do filme escolhido:")
            nlugares = int(input("Introduza o número de lugares para a sala:"))
            sala = (nlugares, [], filme)
            cinema = inserirSala ( cinema, sala )
        elif opcao == 7:
            filme = input("Introduza o nome do filme escolhido:")
            cinema = removerSala( cinema, filme)
            print(f"A sala do filme {filme} foi removida!")
        elif opcao == 0:
            print("Aplicação encerrada, volte sempre!")
            cond = False 