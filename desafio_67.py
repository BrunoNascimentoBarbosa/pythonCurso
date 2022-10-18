'''
Faça um programa que mostre o tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado
for negativo.
'''

 


cont = 0 
print("-----------------------------------")    
while True:
    n = int(input("Deseja ver a tabuada de qual valor? "))
    if n < 0 :
        break
    print('--'*15)
    for c in range (1,11):
        print(f"{n} x {c} = {n*c}")
    print('--'*15)    
print("Programa tabuada encerrado.")
