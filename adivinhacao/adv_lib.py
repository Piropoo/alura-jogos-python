from time import sleep
from random import randint

# Definindo funções
def abertura():
    print('\n' + '\033[34m=\033[m'*20, 'Número secreto', '\033[34m=\033[m'*20)
    print('Bem vindo ao jogo de adivinhação, Tente descobrir o número secreto!\n')
    sleep(0.8)
    
def definindo_numero() -> int:
    n = randint(1, 100)
    pontos = 1000
    return n, pontos

def perguntando_dificuldade() -> int:
    print('\033[36mQual nível de dificuldade?\033[m')
    print('|\033[32m(1) Fácil\033[m| |\033[33m(2) Médio\033[m| |\033[31m(3) Difícil\033[m|')
    dif = int(input('Digite a dificuldade: '))
    while (dif < 1 or dif > 3):
        dif = int(input('Número inválido, tente novamente: '))
    return dif
    
def definindo_tentativas(dif: int):
    if (dif == 1):
        tentativas = 15
        dif = 'fácil'
    elif (dif == 2):
        tentativas = 10
        dif = 'média'
    else:
        tentativas = 5
        dif = 'difícil'
    return tentativas, dif
        
def validando_chute(chute) -> int:
    while(chute < 1 or chute > 100):
            print('\nVocê deve digitar um número entre 1 e 100!')
            chute = int(input('Tente de novo: '))
            continue
    return chute

def validando_menor(chute: int, n: int, tentativas: int):
    if (chute < n):
                print('O seu número foi menor do que o número secreto.', end=' ') 
                if (tentativas > 0):
                    print(f'Restam {tentativas} tentativas.')
                
def validando_maior(chute: int, n: int, tentativas: int):
    if (chute > n):
                print('O seu número foi maior do que o número secreto.', end=' ') 
                if (tentativas > 0):
                    print(f'Restam {tentativas} tentativas.')
                    
def fim(acertou: bool, pontos: int, n: int):
    if (acertou == True):
        print(f'\nParabéns, \033[32mvocê acertou\033[m!')
        print(f'Pontuação: \033[32m{pontos}\033[m pontos')
    else:
        print(f'\nAcabaram suas tentativas, \033[31mvocê perdeu\033[m! O número era {n}.')
    
    print('\033[34m=\033[m'*20, 'Fim', '\033[34m=\033[m'*20, '\n')