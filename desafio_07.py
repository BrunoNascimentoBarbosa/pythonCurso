#Desenvolva um programa que leia os duas notas
# de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a primeira nota do Aluno = '))
nota2 = float(input('Digite a segunda nota do Aluno = '))
soma = nota1 + nota2
media = (nota1 + nota2) / 2
situacao = 'ativo'

if media >= 5:
    situacao ='Aprovado 🟢'
else:
    situacao ='Reprovado 🔴'

print('O aluno teve um total de {} e a média é {} ele foi {}'.format(soma,media,situacao))