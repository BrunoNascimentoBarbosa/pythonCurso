"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os
valores 'M' OU 'F'. Caso esteja errado, peça a digitação novamente
até ter um valor correto.
"""

sexo = input("Digite o seu sexo: [M] ou [F]").strip().upper()[0]
print(sexo)
while sexo not in 'MmFf':
    sexo = input("Dados  inválidos. Por favor, informe seu sexo: [M] ou [F]").strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))


 
