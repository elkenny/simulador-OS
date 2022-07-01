
import random
import time
import os
import platform

limpar = platform.system()

def Limpar():
    if limpar == 'Windows':
        os.system('cls')
    elif limpar == 'Linux':
        os.system('clear')
def adivinha():
    Pontuacao = 0
    PontosBot = 0
    while True:
        Limpar()
        nmr = random.randint(1, 10)
        os.system('cls')
        print(f"sua pontuaçao {Pontuacao}")
        print(f"pontuaçao do bot {PontosBot}")
        adivinhar = int(input("digite um numero aleatorio de 1 a 10\n=> "))
        print(f"numero sorteado {nmr}")
        time.sleep(1)
        if adivinhar == nmr:
            print("Voce acertou! +1 ponto")
            Pontuacao += 1
            time.sleep(1)
        elif adivinhar != nmr:
            print("Voce errou! -1 ponto")
            time.sleep(1)
            print("+1 ponto para o bot")
            time.sleep(1)
            PontosBot += 1
            if Pontuacao > 1:
                Pontuacao -= 1
            else:
                pass
        else:
            print("tente novamente")
            time.sleep(1)
        os.system('cls')