"""
Desenvolva um lógica que leia o peso e a
altura de um pessoa, colcule seu IMC e
mostre seu status, de acordo com a
tabela abaixo:
-Abaixo de 18.5: Abaixo do peso.
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: obesidade mórbida.
"""

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print("Seu IMC É: {:.2f}".format(imc))
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Seu IMC É: {:.2f}".format(imc))
    print("Peso ideal")
elif 25 <= imc <30:
    print("Seu IMC É: {:.2f}".format(imc))
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Seu IMC É: {:.2f}".format(imc))
    print("Obesidade")
elif imc >= 40:
    print("Seu IMC É: {:.2F}".format(imc))
    print("obesidade mórbida")