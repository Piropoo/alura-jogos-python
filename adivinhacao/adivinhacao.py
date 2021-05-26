from . import adv_lib
from time import sleep

def jogar(): # Função que inicia o jogo
    
    n, pontos = adv_lib.definindo_numero()
    acertou = False
    
    adv_lib.abertura() # Exibe titulo e descrição do jogo
    
    dif = adv_lib.perguntando_dificuldade() 
    tentativas, dif = adv_lib.definindo_tentativas(dif)

    print(f'\nVocê escolheu a dificuldade {dif} e tem {tentativas} tentativas.')
    sleep(0.8)
    chute = int(input('Digite seu número entre 1 e 100: '))

    while (acertou == False and tentativas > 1): # Game loop
        
        chute = adv_lib.validando_chute(chute)

        if (chute == n):
            acertou = True
        else:
            print('\nVocê errou!', end=' ')
            tentativas -= 1
            
            adv_lib.validando_menor(chute, n, tentativas) # Valida se o chute é menor ou maior
            adv_lib.validando_maior(chute, n, tentativas)
                
            pontos -= abs((n - chute))

            chute = int(input('Tente de novo: '))        
            
    adv_lib.fim(acertou, pontos, n)

if __name__ == '__main__':
    jogar() 