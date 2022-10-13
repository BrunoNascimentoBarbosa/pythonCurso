'''
Melhore o jogo do Desafio 28 onde o computador
vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários
para vencer.
'''

import random
from time import sleep

print("==== Jogo Iniciado ====")
print('--'*25)
print('O computador vai escolher um número entre 0 e 10.\nVocê precisa acertar qual número ele escolheu.')
print('--'*25)

computador = random.randrange(11)

jogador = int(input("Faça sua joganda. Adivinhe o número entre 0 e 10 que o computador escolheu.: "))
soma = 1
while jogador != computador:
    print('jogada errada')
    soma = soma + 1
    jogador = int(input("Jogue novamente"))
print("Você acertou: Você jogou {} e o computado jogou {}".format(jogador,computador))
print("Você usou {} jogadas até acertar.".format(soma))