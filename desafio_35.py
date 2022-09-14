'''
Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem
ou não formar um triângulo.
'''

import color


print('=='*20)
print('{} Analisador de Triângulos {}'.format(color.cor['amarelo'],color.cor['limpa']))
print('=='*20)
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 + r2 > r3 and r3 + r2 > r1 and r3 + r1 > r2 :
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
