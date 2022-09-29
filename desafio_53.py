'''
Crie um programa que leia uma frase
qualquer e diga se ela é um palindromo,
desconsiderando os espacos.
Ex: APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA
'''

frase = input("Digite uma frase: ").strip()
print(frase)

print(frase.replace(" ",""))
frase = (frase.replace(" ",""))
fraseInvertida = frase[::-1]
print(frase[::-1])

if frase == fraseInvertida:
    print("É um POLINDROMO.")
else:
    print("Não é um POLINDROMO.")