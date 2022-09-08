'''
O mesmo professor do desafio anterior qeur sotear a ordem de
apresentação de trabalhos dos alunos. Faça um programa que leia
o nome dos quadro alunos e mostre a ordem sorteada.
'''

from random import shuffle

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)

print("A ordem dos alunos sorteados é {}.".format(lista))

