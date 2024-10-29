def menu():

    print("---------- MENU ----------")
    print("Opção 1 - Criar a tabela meteorológica")
    print("Opção 2 - Listar a tabela meteorológica")
    print("Opção 3 - Temperatura média")
    print("Opção 4 - Guardar a tabela meteorológica")
    print("Opção 5 - Carregar a tabela meteorológica")
    print("Opção 6 - Temperatura mínima")
    print("Opção 7 - Amplitude térmica")
    print("Opção 8 - Precipitação máxima")
    print("Opção 9 - Precipitação superior a p")
    print("Opção 10 - Maior número consecutivo de dias com precipitação abaixo de p")
    print("Opção 11 - Gráficos da temperatura máxima, temperatura mínima e pluviosidade")
    print("Opção 0 - Sair da aplicação")

menu()

import random

def medias(TabMeteo):
    res = []
    for data, min, max, prec in TabMeteo:
        media = (min + max) / 2
        res.append((data, media))
    return res

def guardaTabMeteo(t, fnome):      
    file = open(fnome, "w")             
    for dia in t: 
        data, min, max, prec = dia
        ano, mes, dia = data
        registo = f"{ano}-{mes}-{dia}&{min}&{max}&{prec}\n"
        file.write(registo)
    file.close()

def carregaTabMeteo(fnome):
    res = []
    file = open(fnome, "r")
    for linha in file:
        linha = linha.strip()               
        campos = linha.split("&")           
        data, min, max, prec = campos       
        ano, mes, dia = data.split("-")
        dia = ((int(ano), int(mes), int(dia))), float(min), float(max), float(prec)
        res.append(dia)

    file.close()
    return res

def minMin(TabMeteo):
    minimo = TabMeteo[0][1]         
    for data, min, *_ in TabMeteo:
        if minimo > min:
            minimo = min
    return minimo

def amplTerm(TabMeteo):
    res = []
    for data, min, max, *_ in TabMeteo:
        amplitude = max - min
        res.append((data, amplitude))
    return res 

def maxChuva(TabMeteo):
    maximo_prec = TabMeteo[0][3]
    for data, _, _, prec in TabMeteo:
        if prec > maximo_prec:
            maximo_prec = prec
            res.append((data, maximo_prec))
    return res

def diasChuvosos(TabMeteo, p):
    res = []
    for dia in TabMeteo:
        if dia[3] > p:
            meteo = (dia[0], dia[3])
            res.append(meteo)
    
    return res

def maxPeriodoCalor(TabMeteo, p):
    consec_local = 0
    consec_global = 0
    for data, min, max, prec in TabMeteo:
        if prec < p:
            consec_local += 1                             
        else:
            if consec_local > consec_global:            
                consec_global = consec_local
            consec_local = 0                              
    
    if consec_local > consec_global:       
        consec_global = consec_local 

    return consec_global


import matplotlib.pyplot as plt                        

def grafTabMeteo(t):
    datas = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]         
    temps_min = [min for _, min, *_ in t]                                       
    temps_max = [max for _, _, max, _ in t]
    precs = [prec for _, _, _, prec in t]

    plt.plot(datas,temps_min, label="Temp Mínima")                         
    plt.plot(datas,temps_max, label = "Temp Máxima")
    plt.xlabel("Data")                                                       
    plt.ylabel("Temperatura ºC")                                
    plt.title("Temperatura Mínima e Máxima")                             
    plt.legend()                                                                                                                      
    plt.show()                                                                
    
    plt.bar(datas,precs)
    plt.xlabel("Data")                                                         
    plt.ylabel("Precipitação mm")                                
    plt.title("Pluviosidade")                                           
    plt.show()

    return


opcao = 1
TabMeteo = []
cond = True
while opcao != 0 and cond:
    opcao = int(input("Introduza a sua opção:"))
    if opcao == 1:
        dia_1 = int(input("Introduza o dia:"))
        mes = int(input("Introduza o mês:"))
        ano = int(input("Introduza o ano:"))
        Data = (ano,mes,dia_1)
        TempMin = float(input("Introduza a temperatura mínima:"))
        TempMax = float(input("Introduza a temperatura máxima:"))
        Precipitacao = float(input("Introduza a precipitação:"))
        dia = (Data, TempMin, TempMax, Precipitacao)
        TabMeteo.append(dia) 
    elif opcao == 2:
        print(TabMeteo)
    elif opcao == 3:
        res = medias(TabMeteo)
        print(f"A temperatura média é {res}.")
    elif opcao == 4:
        guardaTabMeteo(TabMeteo, "meteorologia.txt")    
    elif opcao == 5:
        tabMeteo2 = carregaTabMeteo("meteorologia.txt")
        print(tabMeteo2)
    elif opcao == 6:
        minimo = minMin(TabMeteo)
        print(f"A temperatura mínima é {minimo}.")
    elif opcao == 7:
        res = amplTerm(TabMeteo)
        print(f"A amplitude térmica é {res}.")
    elif opcao == 8:
        res = maxChuva(TabMeteo)
        print(f"A precipitação máxima é {res}.")
    elif opcao == 9:
        p = float(input("Introduza o valor de precipitação p:"))
        res = diasChuvosos(TabMeteo, p)
        print(f"A precipitação foi superior a {p} em {res}.")
    elif opcao == 10:
        p1 = float(input("Introduza o valor de precipitação p:"))
        consec_global = maxPeriodoCalor(TabMeteo, p1)
        print(f"O maior número de dias com precipitação abaixo de {p1} foram {consec_global}.")
    elif opcao == 11:
        grafTabMeteo(TabMeteo)

    else:
        if opcao != 0:
            print("Resposta inválida!")
        elif opcao == 0:
            cond = False
if opcao == 0:
    print("Aplicação encerrada, volte sempre!")