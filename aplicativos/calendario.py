import platform
import calendar
import os
from datetime import date

so = platform.system()

def Limpar():
    if so == 'Windows':
        os.system('cls')
    elif so == 'Linux':
        os.system('clear')
def Calendario():
    Limpar()

    aa = 2022
    mm = 6
    print(calendar.month(aa, mm))
    DiaDeHoje = date.today()
    print(f"O dia de hoje é: {DiaDeHoje}")