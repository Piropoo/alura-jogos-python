from . import forca_lib 


def jogar(): # Começa o jogo   
    forca_lib.abertura() # Título e descrição do jogo
    
    # Define variáveis
    enforcou = False 
    acertou = False
    tentativas = 7
    digitadas = []
    
    palavras = forca_lib.lendo_arquivo_palavras() # Le o arquivo .txt de palavras
    
    palavra_secreta, acertadas = forca_lib.define_palavra_secreta(palavras) # Define qual é a palavra secreta
    forca_lib.desenho_forca(tentativas)    
    print(acertadas) 
    
    while(not enforcou and not acertou): # Executar jogo enquanto não enforcou ou acertou
        
        chute = forca_lib.digita_chute()
        chute, digitadas = forca_lib.validar_chute(chute, digitadas)
        
        if(chute in palavra_secreta): # Acrescenta letra à palavra ou diminue tentativas
            forca_lib.coloca_letras(chute, palavra_secreta, acertadas)  
        else:
            tentativas -=1 
        
        forca_lib.desenho_forca(tentativas)
        print(acertadas)

        
        acertou = '_' not in acertadas # Encerra o jogo caso o jogador acerte ou caso perca
        if tentativas < 1: 
            enforcou = True 
    
    forca_lib.fim(acertou, palavra_secreta) # Mostra mensagem de que o jogador ganhou ou perdeu

if __name__ == '__main__':
    jogar()
    
    

