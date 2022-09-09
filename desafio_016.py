"""
Crie um programa que leia um número real
qualquer pelo teclado e mostre na tela
a sua porção inteiro.
Ex: Digite um número: 6.127
O numero 6.127 tem a parte inteira 6.
"""
import color

from math import trunc

numero = float(input('Digite um numero: '))

resultado = trunc(numero)
print(color.cor['verde'],resultado,color.cor['limpa'])