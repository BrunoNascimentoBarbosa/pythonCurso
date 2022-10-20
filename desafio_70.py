'''
Crie um programa que leia o nome e o preço
de vários produtos. O programa deverá perguntar se o usuário
vai continuar. 
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000
C) Qual é o nome do produto mais barato.
'''
print("="*30)
print("PROGRAMA CAIXA Be.PDV")
print("="*30)

soma =0
cont = 0 
menorValor = 99999
barato = ''
while True:

    produto = (input("Nome do produto: "))
    valor = float(input("Valor do produto R$:"))
    
    if valor > 100:
        cont += 1
    
    if valor < menorValor:
        menorValor = valor
        barato = produto

    continuar = input("Deseja continuar [S] ou [N]").upper()
    soma += valor
    if continuar == 'S':
        print("-"*30)
    elif continuar == 'N':
        break
print("="*30)    
print("Compra finalizada")    
print("="*30)    
print(f"Total R$ {soma}")
print(f"{cont} produto custa mais de R$100,00")
print(f"O produto mais barato é {barato} e custa {menorValor}")
print("-"*30)

