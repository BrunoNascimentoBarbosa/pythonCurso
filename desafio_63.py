"""
Escreva um programa que leia um número n
inteiro qualquer e mostre na tela os n
primeiros elementos de uma sequência de Fibonacci.
EX: 0 1 1 2 3 5 8
"""

n = int(input("Digite um número para descobrir a sequência Finonacci: "))
t1 = 0
t2 = 1
cont =3
print("{} - {} ".format(t1,t2), end="")

while cont <= n:
    t3 = t1 + t2
    print(" - {}".format(t3),end="")
    t1 =t2
    t2 = t3
    cont += 1
print(" Fim...")
