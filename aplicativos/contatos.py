
import os
import time
import webbrowser
import platform

limpar = platform.system()

def Limpar():
    if limpar == 'Windows':
        os.system('cls')
    elif limpar == 'Linux':
        os.system('clear')
def AdcContato():
    Limpar()
    with open('aplicativos/ContatosSalvos.txt', 'w', encoding='utf-8') as contato:
        nome = input("digite o nome do contato: ")
        numero = int(input(f"insira o numero de {nome} +xx (xx) xxxxxxxx: +"))
        print(f"nome: {nome}\nnúmero de telefone: {numero}")
        dados = input("os dados estao certos? (s/n): ")
        if dados == "s":
            contato.write(f"+-----------------+\n|nome: {nome}\n|número: {numero}\n+-----------------+\n")
            print("contato adicionado!")
            time.sleep(1)
            ChamarContato = input("Deseja chamar o contato no WhatsApp? (s/n): ")
            if ChamarContato == "s":
                SeuNome = input("Digite seu nome: ")
                numeroTotal = numero
                webbrowser.open('https://wa.me/'+str(numeroTotal)+'?text=Ol%C3%A1%2C+'+str(nome)+'+me+chamo+'+str(SeuNome))
                Limpar()
                menuContatos()
            else:
                Limpar()
                menuContatos()
        elif dados == "n":
            AdcContato()
def MostrarContatos():
    with open('aplicativos/ContatosSalvos.txt', 'r', encoding='utf-8') as contato:
        contatos = contato.read()
        print(contatos)
        Limpar()
        menuContatos()
def RemoverContatos():
    with open('aplicativos/ContatosSalvos.txt', 'w', encoding='utf-8') as contato:
        pass
        print("contatos removidos")
def menuContatos():
    Limpar()
    print('''
    [01] - adicionar contato
    [02] - remover contato
    [03] - mostrar contatos
    ''')
    select = int(input("=>"))
    if select == 1:
        Limpar()
        AdcContato()
    elif select == 2:
        Limpar()
        RemoverContatos()
    elif select == 3:
        MostrarContatos()
    else:
        print("selecione uma opcao válida!")
        Limpar()
        menuContatos()