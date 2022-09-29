'''
Faça um programa que leia um número
inteiro e diga se ele é ou não
um número primo.
'''

import color
number = int(input("Digite um número inteiro e descubra se ele é PRIMO: "))
total = 0
for c in range (1,number +1):
    if number % c == 0:
        print(color.cor['amarelo'],end=' ')
        total += 1
    else:
        print(color.cor['vermelho'],end=' ')
    print('{}'.format(c),end=' ')
print('\nO numero  {} foi divisível {} vezes'.format(number,total))
if total == 2:
    print('E por isso é PRIMO!')
else:
    print('E por isso ele não é PRIMO')