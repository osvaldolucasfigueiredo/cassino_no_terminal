from random import*
from TextColor import *
from time import sleep
import os


#letras = [negrito_ciano("A"), negrito_magenta("B"), negrito_amarelo("C"), negrito_verde("D"), negrito_branco("E"), negrito_vermelho("G")]
letras = ["🍎", "🍉", "🍒", "🍔", "⚽️", "🏀", "🏈", "💎", "💰"]

while True:
    sorteio = [str(choice(letras)), str(choice(letras)), str(choice(letras))]

    print("\n")
    x = 0
    os.system('clear') or None
    while x < 30:
        roleta = [str(choice(letras)), str(choice(letras)), str(choice(letras))]
        print(roleta[0] + " " + roleta[1] + " " + roleta[2] + " ")
        sleep(0.12)
        os.system('clear') or None
        x += 1
    print(sorteio[0] + " " + sorteio[1] + " " + sorteio[2] + " ")
    if(sorteio[0] == sorteio[1]):
        if(sorteio[1] == sorteio[2]):
            print(negrito_verde("Parabéns você ganhou"))
        else:
            print(negrito_vermelho("Que pena, você perdeu"))
    else:
        print(negrito_vermelho("Que pena, você perdeu"))
    print("\n\nPressione enter para continuar")
    x = input()