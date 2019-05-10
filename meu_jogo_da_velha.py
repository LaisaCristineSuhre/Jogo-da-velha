import sys  #Serve para que no final das funções tem_ganhador e deu_velha, caso for escolhido terminar o jogo, o programa se encerre.
c1, c2, c3, c4, c5, c6, c7, c8, c9 = "1", "2", "3", "4", "5", "6", "7", "8", "9"  #Significa c1="1", c2="2", c3="3", etc.

def tabuleiro():
    print((" %s | %s | %s\n" + \
           "-----------\n" + \
           " %s | %s | %s\n" + \
           "-----------\n" + \
           " %s | %s | %s")%(c1,c2,c3,c4,c5,c6,c7,c8,c9))  #define como é o tabuleiro do jogo e quando chamada deve fazer com que apareça o tabuleiro
#(caso ele sofra alterações por parte do usuário, elas também aparecerão).
#Cada %s pode ser substituido por "X" ou "O", dependendo do que for escolhido pelo jogador.


def tem_ganhador():  #Define a função tem_ganhador.
    global c1,c2,c3,c4,c5,c6,c7,c8,c9
    if(c1==c2==c3 or c4==c5==c6 or c7==c8==c9 or c1==c4==c7 or c2==c5==c8 or c3==c5==c9 or c1==c5==c9 or c3==c5==c7):
        print("Fim de jogo!")
        n2=str(input("Vocês querem jogar de novo? Se quiserem, digitem sim, se não quiserem, digitem não: "))
        #Diz que se c1 for igual ao c2 que também é igual ao c3 ou c4 for igual ao c5 que também é igual ao c6 e assim por diante, irá
        #imprimir "Fim de jogo!" e pedir se os jogadores querem jogar de novo.
        if(n2=="sim" or n2=="Sim"):
            c1, c2, c3, c4, c5, c6, c7, c8, c9 = "1", "2", "3", "4", "5", "6", "7", "8", "9"
            tabuleiro()
            jogo= True
        elif(n2=="não" or n2=="Não"):
            sys.exit()
        return True
    return False
        #Então, se eles quiserem (Sim ou sim), o jogo irá recomeçar, pois c1, c2, c3, c4, c5, c6, c7, c8, c9 = "1", "2", "3", "4", "5", "6", "7", "8", "9"
        #irá zerar o tabuleiro e então será chamada a função tabuleiro, fazendo com que o jogo se inicie de novo. Caso eles não queiram (Não ou não),
        #o programa será fechado.

def deu_velha():  #Define a função deu_velha.
    global c1,c2,c3,c4,c5,c6,c7,c8,c9
    if(c1!="1" and c2!="2" and c3!="3" and c4!="4" and c5!="5" and c6!="6" and c7!="7" and c8!="8" and c9!="9"):
        print("Deu velha!")
        #Diz que se c1 for difernte de "1", e se c2 for diferente de "2", e assim por diante, irá imprimir "Deu velha!" e pedir se os jogadores querem jogar de novo.
        n2=str(input("Vocês querem jogar de novo? Se quiserem, digitem sim, se não quiserem, digitem não: "))
        if(n2=="sim" or n2=="Sim"):
            c1, c2, c3, c4, c5, c6, c7, c8, c9 = "1", "2", "3", "4", "5", "6", "7", "8", "9"
            tabuleiro()
            jogo= True
        if(n2=="não" or n2=="Não"):
            sys.exit()
        return True
    return False
        #Então, se eles quiserem (Sim ou sim), o jogo irá recomeçar, pois c1, c2, c3, c4, c5, c6, c7, c8, c9 = "1", "2", "3", "4", "5", "6", "7", "8", "9"
        #irá zerar o tabuleiro e então será chamada a função tabuleiro, fazendo com que o jogo se inicie de novo. Caso eles não queiram (Não ou não),
        #o programa será fechado.

jogo=True  #Irá repetir o jogo ennquanto ele for verdade.
while jogo:
    n=str(input("Escolha qual você quer (X ou O): "))  #Pede se o primeiro jogador quer "X" ou "O".
    tabuleiro()  #Mostra o tabuleiro.
    while not tem_ganhador() and not deu_velha():  #Diz que enquanto não tem ganhador e não deu velha, será executado o que vem a seguir.
        if(n=="X" or n=="x"):  #Diz que se o jogador escolheu X, deve-se executar o que vem em seguida.
            n1=int(input("X-Digite um número: "))  #Diz que como foi escolhido X, irá dizer para X escolher a casa.
            while(n1>9 or n1<1):  #Diz que enquanto o jogador escolher um número maior que 9 ou menor que 1, a jogada é invalida e ele precisa escolher de novo.
                    print("Jogada inválida!")
                    n1=int(input("X-Digite um número: "))
            if(n1==1):  
                c1="X"  #Diz que se c1 for 1 (linha de cima), c1 passará a ser X.
                tabuleiro() #Mostra o tabuleiro com suas modificações.
                if tem_ganhador() or deu_velha() :
                    break  #Diz que se tem ganhador ou deu velha, o jogo acaba.
                n1=int(input("O-Digite um número: "))  #Já foi a vez do jogador X então agora pede qual posição o jogador O quer.
                while(n1==1):
                    print("Posição ocupada!")
                    n1=int(input("O-Digite um número: "))  #Diz que se a posição que ele escolheu foi 1, ele deve refazer a jogada, pois esta casa já está ocupada.
                if(n1==2):
                    c2="O"
                elif(n1==3):
                    c3="O"
                elif(n1==4):
                    c4="O"
                elif(n1==5):
                    c5="O"
                elif(n1==6):
                    c6="O"
                elif(n1==7):
                    c7="O"
                elif(n1==8):
                    c8="O"
                elif(n1==9):
                    c9="O"  #Estas linhas dizem que se o jogador escolheu uma destas posições deve-se substituir o número por O.
                tabuleiro()  #Mostra o tabuleiro modificado.
                while(n1>9 or n1<1):  #Diz que enquanto o jogador escolher um número maior que 9 ou menor que 1, a jogada é invalida e ele precisa escolher de novo.
                    print("Jogada inválida!")
                    n1=int(input("O-Digite um número: "))

            elif(n1==2):
                c2="X"  
                tabuleiro()
                if tem_ganhador() or deu_velha() :
                    break
                n1=int(input("O-Digite um número: "))
                while(n1==2):
                    print("Posição ocupada!")
                    n1=int(input("O-Digite um número: "))
                if(n1==1):
                    c1="O"
                elif(n1==3):
                    c3="O"
                elif(n1==4):
                    c4="O"
                elif(n1==5):
                    c5="O"
                elif(n1==6):
                    c6="O"
                elif(n1==7):
                    c7="O"
                elif(n1==8):
                    c8="O"
                elif(n1==9):
                    c9="O"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("O-Digite um número: "))
                    
            elif(n1==3):
                c3="X"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("O-Digite um número: "))
                while(n1==3):
                    print("Posição ocupada!")
                    n1=int(input("O-Digite um número: "))
                if(n1==1):
                    c1="O"
                elif(n1==2):
                    c2="O"
                elif(n1==4):
                    c4="O"
                elif(n1==5):
                    c5="O"
                elif(n1==6):
                    c6="O"
                elif(n1==7):
                    c7="O"
                elif(n1==8):
                    c8="O"
                elif(n1==9):
                    c9="O"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("O-Digite um número: "))
                
            elif(n1==4):
                c4="X"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("O-Digite um número: "))
                while(n1==4):
                    print("Posição ocupada!")
                    n1=int(input("O-Digite um número: "))
                if(n1==1):
                    c1="O"
                elif(n1==2):
                    c2="O"
                elif(n1==3):
                    c3="O"
                elif(n1==5):
                    c5="O"
                elif(n1==6):
                    c6="O"
                elif(n1==7):
                    c7="O"
                elif(n1==8):
                    c8="O"
                elif(n1==9):
                    c9="O"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("O-Digite um número: "))
                
            elif(n1==5):
                c5="X"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("O-Digite um número: "))
                while(n1==5):
                    print("Posição ocupada!")
                    n1=int(input("O-Digite um número: "))
                if(n1==1):
                    c1="O"                    
                elif(n1==3):
                    c3="O"
                elif(n1==4):
                    c4="O"
                elif(n1==2):
                    c2="O"
                elif(n1==6):
                    c6="O"
                elif(n1==7):
                    c7="O"
                elif(n1==8):
                    c8="O"
                elif(n1==9):
                    c9="O"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("O-Digite um número: "))
                
            elif(n1==6):
                c6="X"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("O-Digite um número: "))
                while(n1==6):
                    print("Posição ocupada!")
                    n1=int(input("O-Digite um número: "))
                if(n1==1):
                    c1="O"
                elif(n1==3):
                    c3="O"
                elif(n1==4):
                    c4="O"
                elif(n1==5):
                    c5="O"
                elif(n1==2):
                    c2="O"
                elif(n1==7):
                    c7="O"
                elif(n1==8):
                    c8="O"
                elif(n1==9):
                    c9="O"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("O-Digite um número: "))
                
            elif(n1==7):
                c7="X"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("O-Digite um número: "))
                while(n1==7):
                    print("Posição ocupada!")
                    n1=int(input("O-Digite um número: "))
                if(n1==1):
                    c1="O"
                elif(n1==3):
                    c3="O"
                elif(n1==4):
                    c4="O"
                elif(n1==5):
                    c5="O"
                elif(n1==6):
                    c6="O"
                elif(n1==2):
                    c2="O"
                elif(n1==8):
                    c8="O"
                elif(n1==9):
                    c9="O"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("O-Digite um número: "))
                
            elif(n1==8):
                c8="X"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("O-Digite um número: "))
                while(n1==8):
                    print("Posição ocupada!")
                    n1=int(input("O-Digite um número: "))
                if(n1==1):
                    c1="O"
                elif(n1==3):
                    c3="O"
                elif(n1==4):
                    c4="O"
                elif(n1==5):
                    c5="O"
                elif(n1==6):
                    c6="O"
                elif(n1==7):
                    c7="O"
                elif(n1==2):
                    c2="O"
                elif(n1==9):
                    c9="O"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("O-Digite um número: "))
                
            elif(n1==9):
                c9="X"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("O-Digite um número: "))
                while(n1==9):
                    print("Posição ocupada!")
                    n1=int(input("O-Digite um número: "))
                if(n1==1):
                    c1="O"
                elif(n1==3):
                    c3="O"
                elif(n1==4):
                    c4="O"
                elif(n1==5):
                    c5="O"
                elif(n1==6):
                    c6="O"
                elif(n1==7):
                    c7="O"
                elif(n1==8):
                    c8="O"
                elif(n1==2):
                    c2="O"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("O-Digite um número: "))

#O que está escrito entre as linhas 70 e 89 será repetido nas próximas linhas até aqui, de acordo com a posição escolhida.
            
        elif(n=="O" or n=="o"):  #Se o primeiro jogador escolher O o jogo seguirá o que está nas próximas linhas, que são como as anteriores mas voltadas para O como primeiro jogador.
            n1=int(input("O-Digite um número: "))
            while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("O-Digite um número: "))
            if(n1==1):
                c1="O"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("X-Digite um número: "))
                while(n1==1):
                    print("Posição ocupada!")
                    n1=int(input("X-Digite um número: "))
                if(n1==2):
                    c2="X"
                elif(n1==3):
                    c3="X"
                elif(n1==4):
                    c4="X"
                elif(n1==5):
                    c5="X"
                elif(n1==6):
                    c6="X"
                elif(n1==7):
                    c7="X"
                elif(n1==8):
                    c8="X"
                elif(n1==9):
                    c9="X"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("X-Digite um número: "))

            elif(n1==2):
                c2="O"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("X-Digite um número: "))
                while(n1==2):
                    print("Posição ocupada!")
                    n1=int(input("X-Digite um número: "))
                if(n1==1):
                    c1="X"
                elif(n1==3):
                    c3="X"
                elif(n1==4):
                    c4="X"
                elif(n1==5):
                    c5="X"
                elif(n1==6):
                    c6="X"
                elif(n1==7):
                    c7="X"
                elif(n1==8):
                    c8="X"
                elif(n1==9):
                    c9="X"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("X-Digite um número: "))
                    
            elif(n1==3):
                c3="O"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("X-Digite um número: "))
                while(n1==3):
                    print("Posição ocupada!")
                    n1=int(input("X-Digite um número: "))
                if(n1==1):
                    c1="X"
                elif(n1==2):
                    c2="X"
                elif(n1==4):
                    c4="X"
                elif(n1==5):
                    c5="X"
                elif(n1==6):
                    c6="X"
                elif(n1==7):
                    c7="X"
                elif(n1==8):
                    c8="X"
                elif(n1==9):
                    c9="X"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("X-Digite um número: "))
                
            elif(n1==4):
                c4="O"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("X-Digite um número: "))
                while(n1==4):
                    print("Posição ocupada!")
                    n1=int(input("X-Digite um número: "))
                if(n1==1):
                    c1="X"
                elif(n1==2):
                    c2="X"
                elif(n1==3):
                    c3="X"
                elif(n1==5):
                    c5="X"
                elif(n1==6):
                    c6="X"
                elif(n1==7):
                    c7="X"
                elif(n1==8):
                    c8="X"
                elif(n1==9):
                    c9="X"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("X-Digite um número: "))
                
            elif(n1==5):
                c5="O"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("X-Digite um número: "))
                while(n1==5):
                    print("Posição ocupada!")
                    n1=int(input("X-Digite um número: "))
                if(n1==1):
                    c1="X"
                elif(n1==3):
                    c3="X"
                elif(n1==4):
                    c4="X"
                elif(n1==2):
                    c2="X"
                elif(n1==6):
                    c6="X"
                elif(n1==7):
                    c7="X"
                elif(n1==8):
                    c8="X"
                elif(n1==9):
                    c9="X"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("X-Digite um número: "))
                
            elif(n1==6):
                c6="O"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("X-Digite um número: "))
                while(n1==6):
                    print("Posição ocupada!")
                    n1=int(input("X-Digite um número: "))
                if(n1==1):
                    c1="X"
                elif(n1==3):
                    c3="X"
                elif(n1==4):
                    c4="X"
                elif(n1==5):
                    c5="X"
                elif(n1==2):
                    c2="X"
                elif(n1==7):
                    c7="X"
                elif(n1==8):
                    c8="X"
                elif(n1==9):
                    c9="X"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("X-Digite um número: "))
                
            elif(n1==7):
                c7="O"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("X-Digite um número: "))
                while(n1==7):
                    print("Posição ocupada!")
                    n1=int(input("X-Digite um número: "))
                if(n1==1):
                    c1="X"
                elif(n1==3):
                    c3="X"
                elif(n1==4):
                    c4="X"
                elif(n1==5):
                    c5="X"
                elif(n1==6):
                    c6="X"
                elif(n1==2):
                    c2="X"
                elif(n1==8):
                    c8="X"
                elif(n1==9):
                    c9="X"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("X-Digite um número: "))
                
            elif(n1==8):
                c8="O"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("X-Digite um número: "))
                while(n1==8):
                    print("Posição ocupada!")
                    n1=int(input("X-Digite um número: "))
                if(n1==1):
                    c1="X"
                elif(n1==3):
                    c3="X"
                elif(n1==4):
                    c4="X"
                elif(n1==5):
                    c5="X"
                elif(n1==6):
                    c6="X"
                elif(n1==7):
                    c7="X"
                elif(n1==2):
                    c2="X"
                elif(n1==9):
                    c9="X"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("X-Digite um número: "))
                
            elif(n1==9):
                c9="O"
                tabuleiro()
                if tem_ganhador() or deu_velha():
                    break
                n1=int(input("X-Digite um número: "))
                while(n1==9):
                    print("Posição ocupada!")
                    n1=int(input("X-Digite um número: "))
                if(n1==1):
                    c1="X"
                elif(n1==3):
                    c3="X"
                elif(n1==4):
                    c4="X"
                elif(n1==5):
                    c5="X"
                elif(n1==6):
                    c6="X"
                elif(n1==7):
                    c7="X"
                elif(n1==8):
                    c8="X"
                elif(n1==2):
                    c2="X"
                tabuleiro()
                while(n1>9 or n1<1):
                    print("Jogada inválida!")
                    n1=int(input("X-Digite um número: "))
