'''
Escreva um programa para aprovar o empréstimo bancário paa a compra de uma
casa. O programa vai perguntar o valor da casa , o salário do comprodor e em quantas anos
ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
'''

casa = float(input('Qual o valor da casa R$:'))
salario = float(input('Qual o salário do comprador R$:'))
tempo = int(input('Em quantos anos vai pagar? '))
parcelas = tempo*12
limite = salario*30/100
prestacao = casa / parcelas

if prestacao < limite:
    print('Seu empréstimo foi APROVADO.')
    print('O valor da sua parcela é R$:{}'.format(prestacao))
    print('Número de parcelas:{}'.format(parcelas))
else:
    print('Não aprovado')