"""
Refaça o Desafio  051, lendo o primeiro
termo e a razão de uma PA, mostrando os 10 primeiros
termos da progresão usando a estrutura while.


termo = int(input("Digite o primeiro termo dessa PA: "))
razao = int(input("Escolha a razão da sua PA: "))
soma = 0
for c in range(termo,(termo+10)):
    soma = soma + razao
    print(soma  ,end=" | ")
print("ACABOU")

"""

termo = int(input( "DIGITE O PRIMEIRO TERMO DESSA PA: "))
razao = int (input("Escolha a razão da PA: "))
cont = 1
while cont <= 10:
    print('{} '.format(termo),end='')
    termo+= razao
    cont +=1
print("Fim...")    
