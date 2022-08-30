'''
link da aulda: https://www.youtube.com/watch?v=a7DH88vk2Sk&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=31
Crie um programa que leia o nome completo de uma
pessoa e mostre:
1) O nome com todas as letras maiúsculas.
2) O nome com todas minúsculas.
3) Quantas letras ao todo (sem considerar espaços).
4) Quantas letras tem o primeiro nome.
'''

name = str(input('Digite o nome completo: '))
print(name)
print(name.upper())
print(name.lower())
print(len(name))
name = name.strip()
print(len(name))
name = name.split()
print(name)
print(len(name[0]))