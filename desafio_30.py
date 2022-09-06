'''
Crie um programa que leia um número inteiro
e mostre na tela se ela é par ou impar.
'''

numero = int(input('Digite um número inteiro: '))
resultado = numero % 2

if resultado == 0:
    print("O número {} é PAR".format(numero))
else:
    print("O número {} é ÍMPAR".format(numero))