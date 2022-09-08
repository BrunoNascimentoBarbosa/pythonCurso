#Desenvolva um programa que leia os duas notas
# de um aluno, calcule e mostre a sua média.
print('\033[0;30;43m=====Desafio 07 ===== \033[m')
nota1 = float(input('Digite a primeira nota do Aluno = '))
nota2 = float(input('Digite a segunda nota do Aluno = '))
soma = nota1 + nota2
media = (nota1 + nota2) / 2
situacao = 'ativo'

if media >= 5:
    situacao ='\033[0;30;42m Aprovado \033[m '
else:
    situacao ='\033[0;30;41m Reprovado \033[m '

print('O aluno teve um total de {} e a média é {} ele foi {}'.format(soma,media,situacao))