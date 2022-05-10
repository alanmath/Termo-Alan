from random import randint
from palavras import *
from unidecode import unidecode

def sorteia_palavra():      #Função criada pra sortear a palavra do jogo!
    indice = randint(0, len(palavras())-1)
    palavra = palavras()[indice]
    palavra1 = unidecode(palavra)       #unidecode remove acentos!
    palavramaiusc = palavra1.upper()    #deixei tudo maiusculo!
    return palavramaiusc        

def valida_palavra_sorteio():           #validar palavra do sorteio
    lista_de_letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']     #letras validas dos usuários!
    ok = True
    while ok:           
        booleano = True
        finaliza = True
        palavra_jogador = input("Diga uma palavra com 5 caracteres: ")
        removeacento = unidecode(palavra_jogador)
        palavra_maiuscula = removeacento.upper()        #entrada já validada
        if palavra_maiuscula not in palavras():         
            print("Ação inválida, digite um nome válido")
        else:
            for letra in palavra_maiuscula:         #validar letra por letra!
                if not letra in lista_de_letras:
                    print("Ação inválida, tem que ser só letra")
                    booleano = False
                    finaliza = False
            if len(palavra_jogador) != 5 and booleano:      #se a palavra tiver mais de 5 letras
                print("Ação inválida, tem que ter 5 letras")
                finaliza = False
            elif finaliza:  
                ok = False
    return palavra_maiuscula

def corteclado(contador, dicionario_de_palavras, dicionario_de_cor, dict_letras):   #Função que vai dar as cores usadas para o teclado!!!
    for i in range(5):
        if dict_letras[dicionario_de_palavras[f'{contador}'][i]] == 40:
            dict_letras[dicionario_de_palavras[f'{contador}'][i]] = dicionario_de_cor[f'{contador}c'][i]
        if dict_letras[dicionario_de_palavras[f'{contador}'][i]] == 43 and dicionario_de_cor[f'{contador}c'][i] == 42:
            dict_letras[dicionario_de_palavras[f'{contador}'][i]] = dicionario_de_cor[f'{contador}c'][i]
        if dicionario_de_cor[f'{contador}c'][i] == 40 and dict_letras[dicionario_de_palavras[f'{contador}'][i]] == 40:
            dict_letras[dicionario_de_palavras[f'{contador}'][i]] = ''
    return dict_letras