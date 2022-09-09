'''
Faça um programa que leia um número
de 0 a 9999 e mostre na tela cada um dos
dígitos separados.

Ex: Digite um número: 1834
UNIDADE: 4
DEZENA:3
CENTENA:8
MILHAR:1
'''

import color

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('{} Analisando o número {} {} '.format(color.cor['verde'],num,color.cor['limpa']) )
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Millhar:{}'.format(m))
