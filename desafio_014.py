#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

import color


temperatura =float(input('Digite uma temperatura em Grau Celsius:'))

temperaturaF = (temperatura*9/5) + 32

print('A temperatura em Grau Fahrenheit é {} {}°F {} '.format(color.cor['amarelo'],temperaturaF,color.cor['limpa']))