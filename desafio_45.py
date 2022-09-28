"""
Crie um programa que faça o computador
jogar jokenpô com você.
Pedra, papel e tesoura.
"""

import random
from time import sleep

print("Vamos Jogar JOKENPÔ")
print ("Escolha:\n 1 Pedra "
       "\n 2 PAPEL \n"
       " 3 TESOURA ")
jogador = int(input("Digite sua jogada:"))
jogadas = [1,2,3]
maquina = (random.choice(jogadas))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print(jogador,maquina)

if jogador == 1 and maquina == 3:
    print("Você venceu :)")
elif jogador == 1 and maquina ==1:
    print("Empate")
elif jogador == 1 and maquina == 2:
    print("Você perdeu e a maquina ganhou.")
elif jogador == 2 and maquina == 1:
    print("Você venceu :)")
elif jogador == 2 and maquina == 2:
    print("Empate")
elif jogador == 2 and maquina == 3:
    print("Você perdeu e maquina ganhou")
elif jogador == 3 and maquina == 2:
    print("Você venceu :)")
elif jogador == 3 and maquina == 1:
    print("Você perdeu e maquina ganhou")
elif jogador == 3 and maquina == 3:
    print("Empate")
