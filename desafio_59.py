"""
Crie um programa que leia dois valores
e mostre um menu na tela:
 [1] Somar
 [2] Multiplicar
 [3] Maior
 [4] Novos números
 [5] Sair do programa

 Seu programa deverá realizar a operação
 solicitada em cada caso.
"""
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

opcao = 0
while opcao != 5:
    print("O que você deseja fazer.\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair")
    opcao = int(input("Qual a sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma de {} + {} é = {}".format(n1,n2,soma))
    elif opcao == 2:
        mult = n1 * n2
        print("A multiplicação de {} e {} é = {} ".format(n1,n2,mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior =n2
        print("O maior número é {}".format(maior))
    elif opcao == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opçao invalida, tente novamente.")


print("Fim do programa...")

