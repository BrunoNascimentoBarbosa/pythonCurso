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

n = input('Digite um número de 0 a 9999: ')
print(n)
n= (n.strip())

print('Unidade:'+(n[3]))
print('DEZENA:'+(n[2]))
print('CENTENA:'+(n[1]))
print('MILHAR:' +(n[0]))
