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

# recebendo doi números
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

#criando a varíavel opção para ser usada no while e atribuindo o valor 0
opcao = 0

#iniciando o laço while (enquanto a o valor da varíavel opcao for diferente de 5) quando o valor for 5 sai do laço.
while opcao != 5:
    #Imprimindo as opção para o usuario.    
    print("O que você deseja fazer.\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair")
    #Recebendo a opção do usuario e salvando na variável opcao.    
    opcao = int(input("Qual a sua opção? "))
    #Criando a primeira opção 1 (soma) se opção igual a 1
    if opcao == 1:
        #Somando dois números.
        soma = n1 + n2
        #Imprimindo o resultado para o usuário.        
        print("A soma de {} + {} é = {}".format(n1,n2,soma))
    #Criando a segunda condição opção 2 (multiplicação) se opção igual a 2        
    elif opcao == 2:
        #Multiplicando dois números.        
        mult = n1 * n2
        #imprimindo o resultado para o usuário.        
        print("A multiplicação de {} e {} é = {} ".format(n1,n2,mult))
    #Criando a terceira condição, opção 3 (Maior número) se opção igual a 3       
    elif opcao == 3:
        #Validando do n1 é maior que n2
        if n1 > n2:
        #Se n1 for maior, a varíavel maior recebe o valor de n1.    
            maior = n1
        #senão    
        else:
            #se n1 não for maior, então maior recebe o valor da varíavel n2.
            maior =n2
        #Imprimindo o resultado do maior número.    
        print("O maior número é {}".format(maior))
    #Criando a quarta condição, opção 4 (Digitar novos números) se opção igual a 4.    
    elif opcao == 4:
        #Recebendo o novo primeiro número.
        n1 = int(input("Digite o primeiro valor: "))
        #Recevendo o novo segundo número.
        n2 = int(input("Digite o segundo valor: "))
    #Criando a quinta condição, opção 5 (Sair do programa) se opção igual a 5.    
    elif opcao == 5:
        #Imprindo para o usúario que o programa foi finalizado.
        print("Finalizando...")
    #Se as opção não forem (1,2,3,4 ou 5) o programa vai mostrar opção invalida.    
    else:
        #Imprimindo o a mensagem de erro.
        print("Opçao invalida, tente novamente.")

#Fim do programa.
print("Fim do programa...")
