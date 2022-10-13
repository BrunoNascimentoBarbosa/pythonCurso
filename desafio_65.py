"""
Crie um programa que leia vários
númeoros inteiros pelo teclado. No final da
execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores.
"""

n = int(input("Digite um número: "))
cont = 1
soma = 0
maior = n
menor = n
media = 0
while n != 00:
    soma += n
    cont += cont
    print("Você digitou {}".format(n))
    if maior < n:
        maior = n
    elif menor > n:
        menor = n
    n = int(input("Digite um número, ou digite [00] para parar. "))
    print(soma, cont)

print("O Maior número é {} e o menor é {}".format(maior, menor))
media = (soma / cont)
print("A media é {} ".format(media))




