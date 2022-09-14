"""
Crie um programa que leia duas notas
de um aluno e calcule sua média, mostrando uma
mensagem no final, de acordo com a média.Atingida:

- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO.
"""

value1 = float(input('Digite a primeira nota: '))
value2 = float(input('Digite a segunda nota: '))

average = (value1 + value2) / 2

print(average)

if average < 5.0:
    print('Aluno REPROVADO.')
elif average == 5.0 or average <= 6.9:
    print('Aluno em RECUPERAÇÃO.')
else:
    print('Aluno APROVADO.' )