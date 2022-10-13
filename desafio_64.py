"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
"""

valor = int(input("Digite um valor: "))
cont = 0
soma = 0
while valor != 999:
    cont += 1
    soma += valor
    valor = int(input("Digite um valor: "))
    print("===========================")
print(cont)
print(soma)

