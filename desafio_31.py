'''
Desenvolva um programa que pergunte a distaância de uma viagem
em km. Calcule o preço da passagem, cobrando R$0,50 por KM para
viagens de até 200km e R$0,45 para viagens mais longas.
'''

import color

distância = float(input("Qual é distância da sua viagem em km ? "))

#preço = distância * 0.50 if distância <= 200 else distância * 0.45   #if simplificado conhecido também com if line.

if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print("{} O valor da sua viagem é R${:.2F} {}".format(color.cor['verde'],preço,color.cor))