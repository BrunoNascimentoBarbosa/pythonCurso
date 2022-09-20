"""
Escreva um programa que leia dois números
inteiros e compare-os, mostrando na tela
uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior.
- Não existe valor, maior os dois são iguais
"""
import color

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print("{} O número {} é maior. {} ".format( color.cor['verde'], n1 , color.cor['limpa']))
elif n2 > n1:
    print("{} O número {} é maior. {}".format(color.cor['amarelo'] ,n2, color.cor['limpa']))
else:
    print("{} Não existe valor maior, os dois são iguais. {}".format(color.cor['azul'],color.cor['limpa']))
