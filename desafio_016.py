"""
Crie um programa que leia um número real
qualquer pelo teclado e mostre na tela
a sua porção inteiro.
Ex: Digite um número: 6.127
O numero 6.127 tem a parte inteira 6.
"""

from math import trunc

numero = float(input('Digite um numero: '))

resultado = trunc(numero)
print(resultado)