""""
 Faça um programa que leia o comprimento do 
 cateto oposto e do cateto adjacente de um 
 triangulo retângulo, calcule e mostre o  comprimento da hipotenusa.
 
"""

# a² + b² = c²

from math import hypot,pow,sqrt

print('='*10)
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite agora o cateto adjacente: '))

cateto = pow(a,2)
catetoAdjacente = pow(b,2)
soma = cateto + catetoAdjacente
hipotenusa = sqrt(soma)

print('O valor da hipotenusa é {:.2f}M  ◣'.format(hipotenusa))


#Solução do professor
print('='*10)
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = float(co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}M'.format(hi))

#Solução usando a biblioteca math.
print('='*10)
catetoOp = float(input('Comprimento da cateto oposto: '))
catetoAd = float(input('Comprimento do cateto adjacente: '))
hipo = hypot(catetoAd,catetoOp)
print('A hipotenusa vai medir {:.2f}'.format(hipo))