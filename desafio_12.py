#Faça um algoritimo que leia o preço de um produto e mostre
#seu novo preço, com 5% de desconto.


valueProduct = float(input('Digite o valor do produto R$ ' ))

newValue = valueProduct-(valueProduct*5/100)
print('Com 5% de desconto o produto vai sair a R${:.2f}'.format(newValue))