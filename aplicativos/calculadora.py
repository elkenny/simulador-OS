import platform
import os

limpar = platform.system()

def Limpar():
    if limpar == 'Windows':
        os.system('cls')
    elif limpar == 'Linux':
        os.system('clear')
def Calculadora():
    print('''
   +-------------+
   | CALCULADORA |
   +-------------+
   digite qual calculo vc deseja fazer:
   soma(s)
   multiplicação(m)
   divisão(d)
   subtração(sb)
    ''')
    select = input("=> ")
    if select == "s":
        print("digite dois numeros :")
        n1 = int(input("primeiro numero => "))
        n2= int(input("segundo numero => "))
        soma = n1 + n2
        print(f"a soma entre {n1} e {n2} é: {soma}")
    elif select == "m":
        print("digite dois numeros: ")
        n1 = int(input("primeiro numero => "))
        n2 = int(input("segundo numero => "))
        multi = n1 * n2
        print(f"a multiplicação entre {n1} e {n2} é: {multi}")
    elif select == "d":
        print("digite dois numeros : ")
        n1 = int(input("primeiro numero => "))
        n2 = int(input("segundo numero => "))
        div = n1 / n2
        print(f"a divsão entre {n1} e {n2} é: {div}")
    elif select == "sb":
        print("digite dois numeros: ")
        n1 = int(input("primeiro numero =>  "))
        n2 = int(input("segundo numero => "))
        sub = n1 - n2
        print(f"a subtração entre {n1} e {n2} é: {sub}")
    else:
        print("escolha uma opção válida")
        Calculadora()