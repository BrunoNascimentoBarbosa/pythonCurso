#Faça um programa que leia um número inteiro
# e mostre na telao seu sucessor e seu antecessor.
print('\033[0;30;47m ===== Desafio 05 ===== \033[m')
numero = int(input('Digite um número e descubra o sucessor e antecessor.'))

print ('O sucessor de {} é {}'.format(numero, numero+1))
print ('O antecessor de {} é {}'.format(numero, numero-1))
