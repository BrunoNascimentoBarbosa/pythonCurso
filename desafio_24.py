'''
Crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com o nome "SANTO"
'''

city = input('Diginte o nome de uma cidade:').strip()
print(city[:5].upper() == 'SANTO')


city = city.find('SANTO')

