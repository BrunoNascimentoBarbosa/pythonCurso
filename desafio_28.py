'''
Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random

print('O computador vai pensar um número de 0 a 5.')
print('Você deve adivinhar o número para ganhar.')
numero = random.randrange(5)

jogada = int(input('Digite um número de 0 a 5: '))

if jogada == numero:
    print('Você ganhou o número escolhido foi :{}'.format(numero))
else:
    print('Você perdeu o número escolhido foi {} e não {}'.format(numero,jogada))
