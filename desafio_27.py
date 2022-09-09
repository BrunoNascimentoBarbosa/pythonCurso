'''
Faça um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o último nome separamente.
Ex: Ana maria de souza
Primeiro= Ana
último = Souza
'''

import color

nome =str(input(color.cor['azul'] + 'Digite o seu nome completo:' + color.cor['limpa'])).strip()
print(nome.split())
nome = nome.split()
print('Seu primeiro nome é: {} '.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))