'''
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$1.250,00 , calcule um aumento de 1O%.
Para os inferiores  ou iguais, o aumento é de 15%.
'''
import color

salario = float(input('Digite é o salário do funcionário? R$'))
if salario > 1250:
    novo = salario + (salario * 10/100)
else:
    novo = salario + (salario * 15 /100)
print(color.cor['verde'] + 'Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,novo))



