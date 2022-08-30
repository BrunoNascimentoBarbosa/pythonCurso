'''
Crie um programa que leia um nome de uma pessoa
e diga se ela tem "SILVA" no nome.
'''

name = input('Digite o seu nome completo:')
print(name)

name = name.find('SILVA')
print(name)

if name != -1:
    print('Tem SILVA no nome.')
else:
    print('Não tem SILVA no nome.')