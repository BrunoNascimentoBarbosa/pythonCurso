'''
Crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com o nome "SANTO"
'''
import color

city = input(color.cor['vermelho'] + 'Diginte o nome de uma cidade:' + color.cor['limpa'] ).strip()
print(city[:5].upper() == 'SANTO')


city = city.find('SANTO')

