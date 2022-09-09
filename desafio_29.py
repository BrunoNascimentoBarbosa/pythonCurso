'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h , mostre um mensagem dizendo que
ele foi multado.
A multa vai custar R$7,00 por cada KM acima do limite.
'''
import color
from time import sleep

velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade-80)*7
print("Processando informação ...")
sleep(3)
if velocidade > 80:
    print('Você foi multado.')
    print('{} O valor da multa é R${} {} '.format(color.cor['vermelho'] ,multa, color.cor['limpa']))
else:
    print('Boa viagem: ')