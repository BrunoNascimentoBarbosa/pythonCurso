'''
Faça um programa que jogue par ou impar
com o computador.
O jogo só será interrompido quando o jogador PERDER, 
mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.

'''
import random 
 
soma = 0
while True:
    print("--"*30)
    choicePlay = input("Escolha [PAR] OU [IMPAR] : ") 
    if choicePlay == 'PAR':
        print("Você escoheu PAR.")
    else:
        print("Você escolheu IMPAR.")

    jogada = int(input("Digite um valor para jogar com o computador: "))
    print("--"*30)
    jogadaPc = [0,1,2] 
    computador = random.choice(jogadaPc)
    resultado = jogada + computador
    print(f"{jogada} {computador} {resultado}")
    if choicePlay == 'PAR' and resultado % 2 ==0 :
        print("Você ganhou.")
        soma += 1
    elif choicePlay == 'IMPAR' and resultado % 2 != 0:
        print("Você ganhou.")
        soma += 1
    else:
        print("Você perdeu.")
        break
print(f"Você ganhou {soma} vezes. Voltei sempre ao jogo.")


    