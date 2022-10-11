"""
Melhore o desafio 061,
perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar O TERMOS.
"""


termo = int(input( "DIGITE O PRIMEIRO TERMO DESSA PA: "))
razao = int (input("Escolha a razão da PA: "))
cont = 1
while cont <= 10:
    print('{} '.format(termo),end='')
    termo+= razao
    cont +=1
    if cont == 10:
        print("--")
        print("Deseja mostrar mais algum termo?")
        termo = int(input( "DIGITE O PRIMEIRO TERMO DESSA PA: "))
        if termo != 0:
           cont = 1
        else:
            print("fim do programa")

print("Fim...")    
