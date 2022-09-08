'''
Faça um programa que leia três números e
mostre qual é o maior e qual é o menor.
'''

a = int(input('Digite o primeiro número.'))
b = int(input('Digite o segundo número.'))
c = int(input('Digiete o terceiro número.'))

# verificando o menor número.
menor = a
if b < a and c < a:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é menor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))
