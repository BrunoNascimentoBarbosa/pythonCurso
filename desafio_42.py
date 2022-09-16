"""
Refaça o Desafio 35 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:
-Equilátero: Totos os lados iguais.
-Isósceles: dois lados iguais
-Escaleno: Todos os lados diferentes.
"""

'''
Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem
ou não formar um triângulo.
'''

n1 = float(input("Digite o primeiro comprimento: "))
n2 = float(input("Digite o segundo comprimento: "))
n3 = float(input("Digite o terceiro comprimento: "))
triangulo = False
if n1 + n2 > n3 and n2 + n1 > n2 and n2 +n3 > n1:
    print("É um triangulo.")
    triangulo = True

else:
    print("Não forma um triangulo")


if triangulo == True and n1 == n2 and n2 == n3 and n3 == n1:
    print("O triangulo é equilátero")
elif n1 == n2 or n2 == n3 or n3 == n1:
    print("O triangulo é Isóceles")
elif triangulo == True:
    print("O triangulo é Escaleno")




