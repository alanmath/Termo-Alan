from termo_funcoes import *
import os
import unidecode

#Listas do jogo:
recomeça = True
conta_tentativas = 1
dic_tentativas = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
conta_rodadas = 1
while recomeça:  
    #Aqui crio os dicionarios que serão usados!
    dicionario_de_palavras = {"1": [' ', ' ', ' ', ' ', ' '], "2": [' ', ' ', ' ', ' ', ' '], "3": [' ', ' ', ' ', ' ', ' '], "4": [' ', ' ', ' ', ' ', ' '], "5": [' ', ' ', ' ', ' ', ' '], "6": [' ', ' ', ' ', ' ', ' ']}
    #Esse dicionario de cor será usado para alterar a cor das strings no jogo!!!
    dicionario_de_cor = {"1c": [40, 40, 40, 40, 40], "2c": [40, 40, 40, 40, 40], "3c": [40, 40, 40, 40, 40], "4c": [40, 40, 40, 40, 40], "5c": [40, 40, 40, 40, 40], "6c": [40, 40, 40, 40, 40]}
    dicionario_de_letras = {}
    #Esse dicionário dict_letras é usado pra ajustar as cores do teclado
    dict_letras = {'A': 40,'B':40 ,'C':40 ,'D':40,'E':40,'F':40,'G':40,'H':40,'I':40,'J':40,'K':40,'L':40,'M':40,'N':40,'O':40,'P':40,'Q':40,'R':40,'S':40,'T':40,'U':40,'V':40,'W':40,'X':40,'Y':40,'Z':40, 'Ç':40}
    print("""
                \033[1;;41mBEM VINDO AO JOGO DESOCBRINDO PALAVRAS!\033[m
            \033[1;;40mVocê precisa acertar a palavra em 6 tentativas! :)\033[m
            Vou te dar algumas dicas ok? Se a palavra ficar \033[1;;42mVERDE\033[m é porque você
            acertou a palavra e a posição!
            Se a cor for \033[1;;43mAMARELA\033[m quer dizer que a palavra \033[4;;40mestá em jogo\033[m, mas não naquela posição!
    """)
    rodajogo = True     #Inicializar o jogo!
    palavra_do_jogo = sorteia_palavra()     #Sorteamos a palavra do jogo!
    contador = 1        
    while rodajogo:         #COMEÇA O JOGO!
        palavra_da_vez = valida_palavra_sorteio()       #validamos a entrada do usuário!
        i = 0
        dicionario_contador_de_letra = {}           #Aqui entra a logistica de validar as cores e palavras!
        for letra in palavra_da_vez:
            dicionario_de_palavras[f'{contador}'][i] = letra    #O dicionario recebe a letra e as coloca na posição adequada!
            i += 1
        for i in range(len(palavra_da_vez)):        
            if palavra_da_vez[i] == palavra_do_jogo[i]:     #Se a palavra for igual, coloca a cor azul
                dicionario_de_cor[f'{contador}c'][i] = 42
                if palavra_da_vez[i] not in dicionario_contador_de_letra:
                    dicionario_contador_de_letra[palavra_da_vez[i]] = 1     #Esse contador de palavras será usado mais a baixo pra validar as cores das outras letras
                else:
                    dicionario_contador_de_letra[palavra_da_vez[i]] += 1
        for i in range(len(palavra_da_vez)):            #Já que ja colocamos a cor verde, vamos pra logistica da cor amarela!
            if palavra_da_vez[i] in palavra_do_jogo and palavra_da_vez[i] != palavra_do_jogo[i]:
                if palavra_da_vez[i] not in dicionario_contador_de_letra:       #Uso o dicionario contador de letra para validar as entradas
                    dicionario_contador_de_letra[palavra_da_vez[i]] = 0
                if dicionario_contador_de_letra[palavra_da_vez[i]] >= palavra_do_jogo.count(palavra_da_vez[i]):
                    dicionario_de_cor[f'{contador}c'][i] = 40       #No caso da repetição de letras!
                else:
                    dicionario_de_cor[f'{contador}c'][i] = 43       
                    dicionario_contador_de_letra[palavra_da_vez[i]] +=1

        dict_teclado = corteclado(contador, dicionario_de_palavras, dicionario_de_cor,dict_letras)          #Aqui ele recebe o tipo de cor que cada letra deve ter!                    
        #Criei um espaço na função de dar a cor para receber o numero de determinada cor: 40, 42, 43 que são as cores usadas!!!
        os.system('cls')     #Limpa o jogo que estava para trás
        print(f"""
         ___________________
    1.  |\033[1;;{dicionario_de_cor[f'{1}c'][0]}m {dicionario_de_palavras[f'{1}'][0]} \033[m|\033[1;;{dicionario_de_cor[f'{1}c'][1]}m {dicionario_de_palavras[f'{1}'][1]} \033[m|\033[1;;{dicionario_de_cor[f'{1}c'][2]}m {dicionario_de_palavras[f'{1}'][2]} \033[m|\033[1;;{dicionario_de_cor[f'{1}c'][3]}m {dicionario_de_palavras[f'{1}'][3]} \033[m|\033[1;;{dicionario_de_cor[f'{1}c'][4]}m {dicionario_de_palavras[f'{1}'][4]} \033[m|        L     _______________________________________                                                            
    2.  |\033[1;;{dicionario_de_cor[f'{2}c'][0]}m {dicionario_de_palavras[f'{2}'][0]} \033[m|\033[1;;{dicionario_de_cor[f'{2}c'][1]}m {dicionario_de_palavras[f'{2}'][1]} \033[m|\033[1;;{dicionario_de_cor[f'{2}c'][2]}m {dicionario_de_palavras[f'{2}'][2]} \033[m|\033[1;;{dicionario_de_cor[f'{2}c'][3]}m {dicionario_de_palavras[f'{2}'][3]} \033[m|\033[1;;{dicionario_de_cor[f'{2}c'][4]}m {dicionario_de_palavras[f'{2}'][4]} \033[m|     S  E    |\033[1;;{dict_teclado['Q']}m Q \033[m|\033[1;;{dict_teclado['W']}m W \033[m|\033[1;;{dict_teclado['E']}m E \033[m|\033[1;;{dict_teclado['R']}m R \033[m|\033[1;;{dict_teclado['T']}m T \033[m|\033[1;;{dict_teclado['Y']}m Y \033[m|\033[1;;{dict_teclado['U']}m U \033[m|\033[1;;{dict_teclado['I']}m I \033[m|\033[1;;{dict_teclado['O']}m O \033[m|\033[1;;{dict_teclado['P']}m P \033[m|
    3.  |\033[1;;{dicionario_de_cor[f'{3}c'][0]}m {dicionario_de_palavras[f'{3}'][0]} \033[m|\033[1;;{dicionario_de_cor[f'{3}c'][1]}m {dicionario_de_palavras[f'{3}'][1]} \033[m|\033[1;;{dicionario_de_cor[f'{3}c'][2]}m {dicionario_de_palavras[f'{3}'][2]} \033[m|\033[1;;{dicionario_de_cor[f'{3}c'][3]}m {dicionario_de_palavras[f'{3}'][3]} \033[m|\033[1;;{dicionario_de_cor[f'{3}c'][4]}m {dicionario_de_palavras[f'{3}'][4]} \033[m|     u  T   |\033[1;;{dict_teclado['A']}m A \033[m|\033[1;;{dict_teclado['S']}m S \033[m|\033[1;;{dict_teclado['D']}m D \033[m|\033[1;;{dict_teclado['F']}m F \033[m|\033[1;;{dict_teclado['G']}m G \033[m|\033[1;;{dict_teclado['H']}m H \033[m|\033[1;;{dict_teclado['J']}m J \033[m|\033[1;;{dict_teclado['K']}m K \033[m|\033[1;;{dict_teclado['L']}m L \033[m|\033[1;;{dict_teclado['Ç']}m Ç \033[m|
    4.  |\033[1;;{dicionario_de_cor[f'{4}c'][0]}m {dicionario_de_palavras[f'{4}'][0]} \033[m|\033[1;;{dicionario_de_cor[f'{4}c'][1]}m {dicionario_de_palavras[f'{4}'][1]} \033[m|\033[1;;{dicionario_de_cor[f'{4}c'][2]}m {dicionario_de_palavras[f'{4}'][2]} \033[m|\033[1;;{dicionario_de_cor[f'{4}c'][3]}m {dicionario_de_palavras[f'{4}'][3]} \033[m|\033[1;;{dicionario_de_cor[f'{4}c'][4]}m {dicionario_de_palavras[f'{4}'][4]} \033[m|     A  R     |\033[1;;{dict_teclado['Z']}m Z \033[m|\033[1;;{dict_teclado['X']}m X \033[m|\033[1;;{dict_teclado['C']}m C \033[m|\033[1;;{dict_teclado['V']}m V \033[m|\033[1;;{dict_teclado['B']}m B \033[m|\033[1;;{dict_teclado['N']}m N \033[m|\033[1;;{dict_teclado['M']}m M \033[m|
    5.  |\033[1;;{dicionario_de_cor[f'{5}c'][0]}m {dicionario_de_palavras[f'{5}'][0]} \033[m|\033[1;;{dicionario_de_cor[f'{5}c'][1]}m {dicionario_de_palavras[f'{5}'][1]} \033[m|\033[1;;{dicionario_de_cor[f'{5}c'][2]}m {dicionario_de_palavras[f'{5}'][2]} \033[m|\033[1;;{dicionario_de_cor[f'{5}c'][3]}m {dicionario_de_palavras[f'{5}'][3]} \033[m|\033[1;;{dicionario_de_cor[f'{5}c'][4]}m {dicionario_de_palavras[f'{5}'][4]} \033[m|     S  A
    6.  |\033[1;;{dicionario_de_cor[f'{6}c'][0]}m {dicionario_de_palavras[f'{6}'][0]} \033[m|\033[1;;{dicionario_de_cor[f'{6}c'][1]}m {dicionario_de_palavras[f'{6}'][1]} \033[m|\033[1;;{dicionario_de_cor[f'{6}c'][2]}m {dicionario_de_palavras[f'{6}'][2]} \033[m|\033[1;;{dicionario_de_cor[f'{6}c'][3]}m {dicionario_de_palavras[f'{6}'][3]} \033[m|\033[1;;{dicionario_de_cor[f'{6}c'][4]}m {dicionario_de_palavras[f'{6}'][4]} \033[m|        S   
        
    """)
        if dicionario_de_cor[f'{contador}c'][0] == dicionario_de_cor[f'{contador}c'][1] == dicionario_de_cor[f'{contador}c'][2] == dicionario_de_cor[f'{contador}c'][3] == dicionario_de_cor[f'{contador}c'][4] == 42:
            break
        contador += 1                   #VALIDA SE O JOGO ACABOU AQUI
        if contador == 7:
            break

    print('fim de jogo')
    if contador == 7:   #ANALISA QUANDO O JOGADOR VAI PERDER OU GANHAR
        if dicionario_de_cor[f'{6}c'][0] == dicionario_de_cor[f'{6}c'][1] == dicionario_de_cor[f'{6}c'][2] == dicionario_de_cor[f'{6}c'][3] == dicionario_de_cor[f'{6}c'][4] == 42:
            print('Você venceu na ultima!! Na 6ª tentativa!')
        else:
            print(f'Perdeu! a palavra do jogo era {palavra_do_jogo}')        
    else:
        print(f'Você venceu na tentativa {contador}!! Parabéns')
    resposta = "qualquercoisa"                  #Pra entrar no while
    while resposta != 's' and resposta != 'n':      #valida entrada!
        resposta = input('Você deseja reiniciar o jogo? (s)sim ou (n)não: ')
    dic_tentativas[f'{contador}'] += 1
    if resposta == 's':        
        recomeça = True     #Recomeça o JOGO!!
        conta_rodadas += 1          #Conta as rodadas do jogo!
    else:
        recomeça = False
#Mostra a pontuação final do jogo
print(f"""
➣Tentativa 1: {(dic_tentativas['1']/conta_rodadas)*100}%
➣Tentativa 2: {(dic_tentativas['2']/conta_rodadas)*100}%
➣Tentativa 3: {(dic_tentativas['3']/conta_rodadas)*100}%
➣Tentativa 4: {(dic_tentativas['4']/conta_rodadas)*100}%
➣Tentativa 5: {(dic_tentativas['5']/conta_rodadas)*100}%
➣Tentativa 6: {(dic_tentativas['6']/conta_rodadas)*100}%
Não conseguiu: {(dic_tentativas['7']/conta_rodadas)*100}%
""")



    