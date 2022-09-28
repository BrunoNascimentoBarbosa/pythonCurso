'''
Refaça o desafio 09, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço de for.
'''

numero = int(input("Digite um número para criar a tabuada dele."))
for c in range (1,11):
    print("{} X {} = {} ".format(c,numero,(c * numero)))