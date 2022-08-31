'''
Crie um programa que leia um nome de uma pessoa
e diga se ela tem "SILVA" no nome.
'''

name = input('Digite o seu nome completo:').strip()
print('Seu nome tem Silva?{}'.format('SILVA' in name.upper()))

