"""
A confederação Nacional de Natação
precisa de um programa que leia o
ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade.
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: Master
"""

from datetime import date

year = int(input('Qual o ano de nascimento do ATLETA: '))
currentYear = date.today().year

age = currentYear -year

if age <= 9:
    print('ATLETA MIRIN')
elif age > 10 and age < 14:
    print('ATLETA INFANTIL')
elif age > 14 and age < 19:    #elif 14 < age < 19  SUGESTÃO DO PYCHARM PARA SIMPLIFICAR.
    print('ATLETA JUNIOR')
elif age  <= 25:
    print('ATLETA SÊNIOR')
else:
    print('ATLETA MASTER')