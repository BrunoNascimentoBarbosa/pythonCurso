'''
Crie um programa que leia um número inteiro
e mostre na tela se ela é par ou impar.
'''
import color
numero = int(input('Digite um número inteiro: '))
resultado = numero % 2

if resultado == 0:
    print("{} O número {} é PAR {} ".format(color.cor['azul'],numero,color.cor['limpa']))
else:
    print("{} O número {} é ÍMPAR {} ".format(color.cor['vermelho'],numero, color.cor['limpa']))