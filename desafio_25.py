'''
Crie um programa que leia um nome de uma pessoa
e diga se ela tem "SILVA" no nome.
'''
import color

name = input(color.cor['verde'] + 'Digite o seu nome completo:' + color.cor['limpa']).strip()
print('Seu nome tem Silva?{}'.format('SILVA' in name.upper()))

