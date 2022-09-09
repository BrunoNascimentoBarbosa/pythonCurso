'''
Faça um programa que leia uma frase pelo teclado e mostre:
> Quantos vezes aparece a letra 'A'.
> Em que posição ela aparece a primeira Vez
> Em que posição ela aparece a última vez.
'''
import color

frase = str(input(color.cor['amarelo'] + 'Digite uma frase: ' + color.cor['limpa'])).upper().strip()
print('A letra a aparece:{}'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A primeira letra A apareceu na posição {}'.format(frase.rfind('A')+1))