# Criar um programa para conversão de medidas
#KM
#HM
#DAM
#DM
#CM
#MM
print('\033[0;30;46m===== Desafio 08 ===== \033[m')
valorMetros = float(input('Digite um valor em metros:  '))
print('Você digitou  {}M'.format(valorMetros))
valorkm = valorMetros / 1000
valorHm = valorMetros / 100
valorDam = valorMetros / 10
valorDm = valorMetros * 10
valorCm = valorMetros * 100
valorMm = valorMetros * 1000

print('O valor {}M em km é {}KM'.format(valorMetros,valorkm))
print('O valor {}M em Hm é {}Hm'.format(valorMetros,valorHm))
print('O valor {}m em Dam é {}Dam'.format(valorMetros,valorDm))
print('O valor {}m em Dm é {}Dm'.format(valorMetros,valorDm))
print('o valor {}M em Cm é {}CM'.format(valorMetros,valorMm))

