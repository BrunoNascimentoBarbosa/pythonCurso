"""
Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com sua idade:

-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de alistar.
-Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta
ou passou do prazo.
"""

from datetime import date

year = int(input('Digite seu ano de nascimento: '))
currentYear = date.today().year
age = currentYear - year

print(age)

if age < 17:
    pastYears = 17 - age
    print('Tem apenas {} ano. Ainda vai se alistar ao Serviço militar. Falta {} anos'.format(age,pastYears))
elif age ==  17 or age == 18:
    print('Você tem {} ano. Tá na hora de fazer o seu alistamento. Para mais informação acesse:https://alistamento.eb.mil.br/'.format(age))
else:
    pastYears = age - 18
    print('Você tem {} anos, já passou do tempo do alistamento. Passou {} anos'.format(age,pastYears))