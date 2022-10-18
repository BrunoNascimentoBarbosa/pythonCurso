'''
crie um programa que leia vários
números inteiros pelo teclado. O programa
só vai para quando o usuário digitar o valor
999, que é a condição  de parada. 

No final,
mostre quantos números foram digitados e qual
foi a soma entre eles.
(Desconsiderando o flag.)
'''


  


n = int(input("Digite um número."))
cont = 0 
soma = 0 
while True:
    n = int(input("Digite um número."))
    cont += 1
    if n == 999 :
        break
    soma = soma + n

print("Programa encerrado.")    
print(f"Foi digitado {cont} números. ")   
print(F"A soma total do valores é {soma}") 

     