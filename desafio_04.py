
print ('\033[0;36;40m =====Desafio 04===== \033[m')
info = input('Digite algo ')
print('O tipo primitivo é : ',type(info))
print('É um número? ',info.isnumeric())
print('É um alfabetico? ',info.isalpha())
print('Só tem espaços? ',info.isspace())
print('É alfanumerico', info.isalnum())
print('Está em maiúscula?',info.isupper())
print('Está em minúscula? ',info.islower())
print('Está capitalizada? ',info.istitle())

