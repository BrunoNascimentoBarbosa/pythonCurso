#Faça um programa que leia a largura e a altura de uma parede em
#metros, calcule a sua área e a quantidade de tinta necessária para
#pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

import color

largura = float(input('Qual a largura da sua parede em Metros? '))
altura = float(input('Qual a altura da sua parede em Metros ?'))

area = largura * altura
quantidadeTinta = area/2
print('Sua parede tem a dimensão de {}{} x {}{} e sua área é de {}m²'.format(color.cor['verde'],largura,altura,color.cor['limpa'],area))
print('Você vai precisar de {}L para pintar os {}M² de parede.'.format(quantidadeTinta,area))
