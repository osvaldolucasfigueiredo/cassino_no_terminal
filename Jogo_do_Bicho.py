from difflib import restore
from TextColor import *
from random import *
import os
from time import sleep

class Resultado_Bicho:
    def __init__(self):
        self.concurso1 = self.sorteio_concursos()
        self.concurso2 = self.sorteio_concursos()
        self.concurso3 = self.sorteio_concursos()
        self.concurso4 = self.sorteio_concursos()
        self.concurso5 = self.sorteio_concursos()
        self.animal_seca = self.animal(self.concurso1)
        self.animal_simples = self.animal5()
        self.unidade_seca = self.unidade(self.concurso1)
        self.dezena_seca = self.dezena(self.concurso1)
        self.centena_seca = self.centena(self.concurso1)
        self.milhar_seca = self.milhar(self.concurso1)
        self.unidade_simples = self.unidade5()
        self.dezena_simples = self.dezena5()
        self.centena_simples = self.centena5()
        self.milhar_simples = self.milhar5()

    def sorteio(self):
        self.concurso1 = self.sorteio_concursos()
        self.concurso2 = self.sorteio_concursos()
        self.concurso3 = self.sorteio_concursos()
        self.concurso4 = self.sorteio_concursos()
        self.concurso5 = self.sorteio_concursos()
        self.animal_seca = self.animal(self.concurso1)
        self.animal_simples = self.animal5()
        self.unidade_seca = self.unidade(self.concurso1)
        self.dezena_seca = self.dezena(self.concurso1)
        self.centena_seca = self.centena(self.concurso1)
        self.milhar_seca = self.milhar(self.concurso1)
        self.unidade_simples = self.unidade5()
        self.dezena_simples = self.dezena5()
        self.centena_simples = self.centena5()
        self.milhar_simples = self.milhar5()

    def resultado(self):
        print(self.concurso1)

    def unidade(self, concurso):
        numero = int(concurso[3])
        return numero

    def unidade5(self):
        numero = [0,0,0,0,0]
        numero[0] = self.unidade(self.concurso1)
        numero[1] = self.unidade(self.concurso2)
        numero[2] = self.unidade(self.concurso3)
        numero[3] = self.unidade(self.concurso4)
        numero[4] = self.unidade(self.concurso5)
        return numero

    def dezena(self, concurso):
        numero = (concurso[2] * 10) + concurso[3]
        return numero

    def dezena5(self):
        numero = [0,0,0,0,0]
        numero[0] = self.dezena(self.concurso1)
        numero[1] = self.dezena(self.concurso2)
        numero[2] = self.dezena(self.concurso3)
        numero[3] = self.dezena(self.concurso4)
        numero[4] = self.dezena(self.concurso5)
        return numero

    def centena(self, concurso):
        numero = (concurso[1] * 100) + (concurso[2] * 10) + concurso[3]
        return numero

    def centena5(self):
        numero = [0,0,0,0,0]
        numero[0] = self.centena(self.concurso1)
        numero[1] = self.centena(self.concurso2)
        numero[2] = self.centena(self.concurso3)
        numero[3] = self.centena(self.concurso4)
        numero[4] = self.centena(self.concurso5)
        return numero

    def milhar(self, concurso):
        numero = (concurso[0] * 1000) + (concurso[1] * 100) + (concurso[2] * 10) + concurso[3]
        return numero

    def milhar5(self):
        numero = [0,0,0,0,0]
        numero[0] = self.milhar(self.concurso1)
        numero[1] = self.milhar(self.concurso2)
        numero[2] = self.milhar(self.concurso3)
        numero[3] = self.milhar(self.concurso4)
        numero[4] = self.milhar(self.concurso5)
        return numero

    def sorteio_concursos(self):
        valor = [0,0,0,0]
        x = 0
        while(x < 4):
            valor[x] = randint(0,9)
            x += 1
        return valor

    def animal(self, concurso):
        numero = (concurso[2] * 10) + concurso[3]

        resto = int(numero % 4)
        divisao = int(numero / 4)
        if(resto == 0):
            if(divisao == 0):
                resultado = 25
            else:
                resultado = divisao
        else:
            resultado = divisao + 1
        return resultado

    def animal5(self):
        numero = [0,0,0,0,0]
        numero[0] = self.animal(self.concurso1)
        numero[1] = self.animal(self.concurso2)
        numero[2] = self.animal(self.concurso3)
        numero[3] = self.animal(self.concurso4)
        numero[4] = self.animal(self.concurso5)
        return numero


class Jogo_Bicho:
    def __init__(self, dinheiro):
        self.dinheiro = dinheiro
        self.animal = 0
        self.resultado = Resultado_Bicho()

    def tipo_de_aposta(self):
        self.limpar_tela()
        print(negrito_ciano("Escolha o Tipo de Aposta"))
        print(amarelo("[11]. Animal (2x)"))
        print(amarelo("[12]. Animal Seca (10x)"))
        #print(amarelo("[13]. Duque de Grupo (30x)"))
        #print(amarelo("[14]. Terno de Grupo (40x)"))
        #print(amarelo("[15]. Quadra de Grupo (1000x)"))
        #print(amarelo("[16]. Quina de Grupo (5000x)"))
        #print(amarelo("[17]. Passe Vai (60x)"))
        #print(amarelo("[18]. Passe Vai-vem (30x)"))
        #print(amarelo("[21]. Unidade (1,4x)"))
        #print(amarelo("[22]. Unidade Seca (4x)"))
        #print(amarelo("[31]. Dezena (8x)"))
        #print(amarelo("[32]. Dezena Seca (40x)"))
        #print(amarelo("[33]. Duque de Dezena (500x)"))
        #print(amarelo("[34]. Terno de Dezena (5000x)"))
        #print(amarelo("[41]. Centena (80x)"))
        #print(amarelo("[42]. Centena Seca (400x)"))
        #print(amarelo("[51]. Milhar (800x)"))
        #print(amarelo("[52]. Milhar Seca (4000x)"))
        tipo_de_aposta = input()
        self.escolher_aposta(tipo_de_aposta)
        print(negrito_ciano("Quanto apostar (Máximo = NS$ " + str(self.dinheiro) + ")"))
        valor_da_aposta = int(input())
        if(valor_da_aposta <= self.dinheiro):
            self.rodar_jogo(valor_da_aposta, tipo_de_aposta)
        else:
            self.rodar_jogo(self.dinheiro, tipo_de_aposta)

    def rodar_jogo(self, valor_da_aposta, tipo):
        self.dinheiro = self.dinheiro - valor_da_aposta
        self.resultado.sorteio()
        if(tipo == "12"):
            if(self.animal == self.resultado.animal_seca):
                premio = int(valor_da_aposta * 10)
                self.dinheiro += premio
                self.girador_da_sorte()
                print(negrito_branco("#### Resultado ####"))
                print(branco(str(self.resultado.concurso1) + str(self.resultado.animal_simples[0])))
                print(branco(str(self.resultado.concurso2) + str(self.resultado.animal_simples[1])))
                print(branco(str(self.resultado.concurso3) + str(self.resultado.animal_simples[2])))
                print(branco(str(self.resultado.concurso4) + str(self.resultado.animal_simples[3])))
                print(branco(str(self.resultado.concurso5) + str(self.resultado.animal_simples[4])))
                self.ganhou(premio, valor_da_aposta)
            else:
                self.girador_da_sorte()
                print(negrito_branco("#### Resultado ####"))
                print(branco(str(self.resultado.concurso1) + str(self.resultado.animal_simples[0])))
                print(branco(str(self.resultado.concurso2) + str(self.resultado.animal_simples[1])))
                print(branco(str(self.resultado.concurso3) + str(self.resultado.animal_simples[2])))
                print(branco(str(self.resultado.concurso4) + str(self.resultado.animal_simples[3])))
                print(branco(str(self.resultado.concurso5) + str(self.resultado.animal_simples[4])))
                self.perdeu(valor_da_aposta)
        if(tipo == "11"):
            ganhar = False
            w = 0
            while(w < 5):
                if(self.animal == self.resultado.animal_simples[w]):
                    ganhar = True
                w += 1
            if(ganhar):
                premio = int(valor_da_aposta * 2)
                self.dinheiro += premio
                self.girador_da_sorte()
                print(negrito_branco("#### Resultado ####"))
                print(branco(str(self.resultado.concurso1) + str(self.resultado.animal_simples[0])))
                print(branco(str(self.resultado.concurso2) + str(self.resultado.animal_simples[1])))
                print(branco(str(self.resultado.concurso3) + str(self.resultado.animal_simples[2])))
                print(branco(str(self.resultado.concurso4) + str(self.resultado.animal_simples[3])))
                print(branco(str(self.resultado.concurso5) + str(self.resultado.animal_simples[4])))
                self.ganhou(premio, valor_da_aposta)
            else:
                self.girador_da_sorte()
                print(negrito_branco("#### Resultado ####"))
                print(branco(str(self.resultado.concurso1) + str(self.resultado.animal_simples[0])))
                print(branco(str(self.resultado.concurso2) + str(self.resultado.animal_simples[1])))
                print(branco(str(self.resultado.concurso3) + str(self.resultado.animal_simples[2])))
                print(branco(str(self.resultado.concurso4) + str(self.resultado.animal_simples[3])))
                print(branco(str(self.resultado.concurso5) + str(self.resultado.animal_simples[4])))
                self.perdeu(valor_da_aposta)

    def ganhou(self, premio, aposta):
        print(negrito_verde("Parabéns você ganhou"))
        print(verde("Sua aposta NS$" + str(aposta)))   
        print(negrito_amarelo("Prêmio de NS$ " + str(premio)))
        self.limpar_tela()

    def perdeu(self, aposta):
        print(negrito_vermelho("Que pena você perdeu"))
        print(vermelho("Sua aposta NS$ " + str(aposta)))
        self.limpar_tela()

    def girador_da_sorte(self):
        x = 0
        while x < 30:
            print(negrito_branco("#### Resultado ####"))
            self.mostrador()
            sleep(0.12)
            os.system('clear') or None
            x += 1

    def mostrador(self):
        print("["+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +"]" +str(randint(1,25)))
        print("["+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +"]" +str(randint(1,25)))
        print("["+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +"]" +str(randint(1,25)))
        print("["+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +"]" +str(randint(1,25)))
        print("["+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +", "+ self.sorteador_de_numeros() +"]" +str(randint(1,25)))

    def sorteador_de_numeros(self):
        numero = str(randint(0, 9))
        return numero

    def limpar_tela(self):
        print(negrito_amarelo("Seu dinheiro: NS$ " + str(self.dinheiro)))
        print(amarelo("\npressione Enter para continuar"))
        dado = input()
        os.system('clear') or None
        

    def escolher_aposta(self, tipo):
        if(tipo == "11"):
            self.animal_simples()
        elif(tipo == "12"):
            self.animal_seca()

    def animal_simples(self):
        self.animal_seca()

    def animal_seca(self):
        print("\n[1.  🦩][2.  🦅][3.  🐴][4.  🦋][5.  🐶]\n[6.  🐐][7.  🐏][8.  🐫][9.  🐍][10. 🐰]\n[11. 🐎][12. 🐘][13. 🐓][14. 🐱][15. 🐊]\n[16. 🦁][17. 🦍][18. 🐖][19. 🦚][20. 🦃]\n[21. 🐂][22. 🐯][23. 🐻][24. 🦌][25. 🐮]")
        print(negrito_magenta("Escolha qual animal quer apostar (1 - 25)"))
        valor = int(input())
        if((valor > 0) and (valor <= 25)):
            self.animal = valor
        else:
            self.animal = 0


a = Jogo_Bicho(500)
while True:
    a.tipo_de_aposta()

