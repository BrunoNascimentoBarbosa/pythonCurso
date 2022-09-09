"""
Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e
tangente desse ângulo.
"""

import color

from math import radians,sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('{} O seno de {} é {:.2f} {}'.format(color.cor['amarelo'],angulo,seno,color.cor['limpa']))
print('{} O cosseno de {} é {:.2f} {}'.format(color.cor['azul'],angulo,cosseno,color.cor['limpa']))
print('{} A tangente de {} é {:.2f} {}'.format(color.cor['roxo'],angulo,tangente,color.cor['limpa']))