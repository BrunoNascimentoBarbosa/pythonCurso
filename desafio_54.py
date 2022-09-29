'''
Crie um programa que eleia o ano de
nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não
atingiram a moioridade e quantas já
são maiores.
'''

import datetime as dt

ano_atual = dt.date.today().year
print(ano_atual)

menor_idade = 0
maior_idade =0
for c in range(1, 8):
    ano = int(input("Digite o ano: "))
    if ano_atual - ano <= 18:
        menor_idade += 1
    else:
        maior_idade +=1

print('{} pessoas não atingiram a maior idade'.format(menor_idade))
print('{} pessoas atingiram a maior idade '.format(maior_idade))




