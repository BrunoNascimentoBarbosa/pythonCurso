'''
Crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com o nome "SANTO"
'''

city = input('Diginte o nome de uma cidade:')
print(city)

city = city.find('SANTO')

if city != -1:
    print('Tem SANTOS NO NOME.')
else:
    print('Não tem SANTOS NO NOME.')