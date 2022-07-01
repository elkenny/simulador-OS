from aplicativos.calendario import Calendario
from aplicativos.contatos import menuContatos
from jogos.adivinha import adivinha
from aplicativos.calculadora import Calculadora
import os
#import time
import platform

so = platform.system()

def Limpar():
    if so == 'Windows':
        os.system('cls')
    elif so == 'Linux':
        os.system('clear')

def SelecionarApp():
    print('''
    [01] - calculadora
    [02] - calendario
    [03] - contatos
    ''')
    selectApp = int(input("=> "))
    if selectApp == 1:
        Limpar()
        Calculadora()
    elif selectApp == 2:
        Limpar()
        Calendario()
    elif selectApp == 3:
        Limpar()
        menuContatos()
    else:
        print("selecione uma opçao valida")
        Limpar()
        SelecionarApp()
def SelecionarJogos():
    print('''
    *JOGOS DISPONIVEIS*
    [01] - jogo de adivinha
    ''')
    selectJogo = int(input("=> "))
    if selectJogo == 1:
        Limpar()
        adivinha()
    else:
        print("selecione uma opçao valida")
        Limpar()
        SelecionarJogos()
#daqui p baixo é o menu
def main():
    Limpar()
    print('''
    [01] - aplicativos
    [02] - jogos
    [03] - configuraçoes (indisponivel)
    ''')
    select = int(input("=> "))
    if select == 1:
        Limpar()
        SelecionarApp()
    elif select == 2:
        Limpar()
        SelecionarJogos()
    elif select == 3:
        pass
    else:
        print("selecione uma opçao valida")
        Limpar()
        main()
main()

   # advinha()
  #  contatos()
 #  calendario()
#     calculadora()