'''
Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final do programa, mostre:
> A média de idade do grupo.
> Qual é o nome do homem mais velho.
> Quantas mulheres têm no menos de 20 anos.
'''
totalIdade = 0
homemVelho = 0
nomeHomemVelho = 'a'
quantMulheres = 0
for c in range(1,5):
    idade = int(input("Digiti a idade: "))
    sexo = input("Digite (M) para Masculino e (F) para feminino: ")
    nome = input("Digite o nome: ").split()
    totalIdade = idade + totalIdade
    if idade > homemVelho and sexo == 'm' or sexo == 'M':
        homemVelho = idade
        nomeHomemVelho = nome
    elif sexo == 'f' or sexo=='F' and idade < 20:
        quantMulheres += 1
print("A média de idade do grupo é {}".format(totalIdade/4))
print("O homem mais velho é {}: ".format(nomeHomemVelho))
print("Quantidade de mulheres com menos de 20 anos é {} ".format(quantMulheres))
