#Crie um programa que leia quanto dinheiro um pessoa tem na
#carteira e mostre quantos Dólares ele pode comprar.
import requests


print('\033[0;32;40m===== Desafio ===== \033[m')
valueWallet = float(input("Quantos reais você tem na carteira? R$ "))
requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD,EUR")
requisicao_dic = requisicao.json()
contacaoDolar = float(requisicao_dic["USDBRL"]["bid"])
contacaoEuro = float(requisicao_dic["EURBRL"]["bid"])

conversionDola = valueWallet/contacaoDolar
conversionEuro = valueWallet/contacaoEuro
message = 'Com R${:.2f} você pode comprar U${:.2f} dolares ou €{:.2f} Euros. '.format(valueWallet,conversionDola,conversionEuro)
print(message)
 