"""
Elabore um programa que calcule o valor
a ser pago por um produto,
considerando o seu preço normal e
condição de pagamento:
- À vista dinheiro/Cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

print("===== CALCULANDO VALOR DE PRODUTO =====")

produto = float(input("Digite o valor do produto:"))

formaPg = int(input("Escolha a forma de pagamento: \n "
          "> 1 para dinheiro/Cheque. \n"
          " > 2 À vista no cartão.\n"
          " > 3 Para 3 x ou mais no cartão.\n"
          " > 4 Para 3x ou mais no cartão:"))

if formaPg == 1:
    print("Você tem 10% de desconto, vai pagar apenas R${}".format(produto - (produto*10/100)))
elif formaPg == 2:
    print("Você tem 5% de desconto, vai pagar apenas R${}".format(produto - (produto*5/100)))
elif formaPg == 3:
    print("Para parcelamento no cartão não tem desconto R${}".format(produto))
elif  formaPg == 4:
    totParcelas = int(input("Qual o total de parcelas."))
    print("Pagamento com juros de 20%, \n"
          "{} x {:.2f} \n"
          "valor total R${} ".format( totParcelas, (produto/totParcelas),produto + (produto * 20 / 100)))
