from adivinhacao import adivinhacao
from forca import forca

def escolhe_jogo():
    
    print('\n' + '\033[34m=\033[m'*20, 'Escolha seu jogo', '\033[34m=\033[m'*20) # Mostra título e descrição
    print('Escolha o jogo que você quer jogar!\n')

    print('|\033[36m(1)\033[m Número secreto| |\033[36m(2)\033[m Forca|') # Pergunta ao jogador qual jogo
    jogo = int(input('Digite o número do jogo: '))

    if jogo == 1: # Seleciona jogo
        adivinhacao.jogar()
    elif jogo == 2:
        forca.jogar()

if __name__ == '__main__':
    escolhe_jogo()