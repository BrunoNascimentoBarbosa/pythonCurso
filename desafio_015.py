"""
 Escreva um programa que pergunte a quantidade de km
 percorridos por um carro alugado e a quantidade de
 dias pelos quais ele foi alugado. Calcule o preço
 a pagar. Sabendo que o carro custa R$60 por dia e R$0.15
 por km rodado.
"""
dias = float(input('Quantos dia o carro foi alugado: '))
km = float(input('Quantos km o carro rodou: '))

custoKm = km*0.15
custoDia = dias*60
custoTotal = custoKm + custoDia

print('O valor a pagar é R${}'.format(custoTotal))

