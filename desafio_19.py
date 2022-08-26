"""
Um professo quer sortear um dos quatro alunos para apagar
o quadro. Faça um programa que ajude ele, lendo o nome deles e
escreva o nome do escolhido.
"""

from  random import choice  #Importando apens o choice

n1 = str(input('Digite o  nome do aluno 1 :'))
n2  = str(input('Digite o nome do aluno 2 : '))
n3 = str(input('Digiete o nome do aluno 2 :'))
n4 = str(input('Digiete o nome do aluno 2 :'))

lista = [n1,n2,n3,n4]
escolhido = choice(lista)

print('O aluno escolhido foi {}:'.format(escolhido))

