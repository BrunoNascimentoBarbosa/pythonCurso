#Faça um algoritimo que leia o salário de um funcionário e mostre seu
# novo salário com 15% de aumento.

import color

salario = float(input('Digite o salário do funcionario para calcular o aumento R$ '))
novoSalario = salario+(salario*15/100)

print('O novo salário com aumento de 15% passa ser {} R${:.2f} {}'.format(color.cor['verde'],novoSalario,color.cor['limpa']))