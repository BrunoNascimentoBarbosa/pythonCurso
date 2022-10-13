'''
Desenvolva um programa que leia o primeiro
termo e a razão de uma PA. No final, mostre
os 10 primeiros termos dessa progressão.
'''

termo = int(input("Digite o primeiro termo dessa PA: "))
razao = int(input("Escolha a razão da sua PA: "))
soma = 0
for c in range(termo,(termo+10)):
    soma = soma + razao
    print(soma  ,end=" | ")
print("ACABOU")