import random
from os import read, stat_result

# Definindo funções
def abertura():
    print('\n' + '\033[34m=\033[m'*20, 'Forca', '\033[34m=\033[m'*20)
    print('Bem vindo ao jogo da forca!\n')
    
def lendo_arquivo_palavras() -> list:
    arquivo_palavras = open('palavras.txt', 'r', encoding='UTF-8')
    palavras = arquivo_palavras.read().replace(',', '').strip().split()
    arquivo_palavras.close
    
    return palavras
    
def define_palavra_secreta(palavras: list) -> str:
    palavra_secreta = palavras[random.randint(0, len(palavras))].upper()
    acertadas = ['_' for letra in palavra_secreta]
    return palavra_secreta, acertadas

def digita_chute() -> str:
    chute = input('\nQual letra? ').strip().upper() 
    print('')
    
    return chute

def validar_chute(chute: str, digitadas: list) -> str: # Valida se é um valor válido
    while len(chute) > 1 or chute.isalpha() == False:
       chute = input('Digite UMA LETRA: ')
       print('')
       
    if chute not in digitadas: # Valida se ja foi digitado
        digitadas.append(chute)
    else: 
        while chute in digitadas: 
            print('Você já digitou esta letra, tente novamente.')
            chute = input('Tente de novo: ').upper()
            print('')

    
    return chute, digitadas

def coloca_letras(chute: str, palavra_secreta: str, acertadas: list):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            acertadas[index] = letra
        index += 1
        
def desenho_forca(tentativas: int):
    print('  _______     ')
    print(' |/      |    ')
    if tentativas == 7:
        print (' |            ')
        print (' |            ')
        print (' |            ')
        print (' |            ')
        
    if tentativas == 6:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        
    if tentativas == 5:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")
        
    if tentativas == 4:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
        
    if tentativas == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
        
    if tentativas == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
        
    if tentativas == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        
    if tentativas == 0:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    
    print(" |            ")
    print("_|___         ")
    print()
        
def fim(acertou: bool, palavra_secreta: str):
    if acertou:
        print("\nParabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else: 
        print("\nPuxa, você foi enforcado!")
        print(f"A palavra era {palavra_secreta.lower()}!")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    
    print('\033[34m=\033[m'*20, 'Fim', '\033[34m=\033[m'*20, '\n')