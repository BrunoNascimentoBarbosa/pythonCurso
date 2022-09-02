'''
Faça um programa que leia o nome completo de uma pessoa
mostrando em seguida o primeiro e o último nome separamente.
Ex: Ana maria de souza
Primeiro= Ana
último = Souza
'''

nome =str(input('Digite o seu nome completo:')).strip()
print(nome.split())
nome = nome.split()
print('Seu primeiro nome é: {} '.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))