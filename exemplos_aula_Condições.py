n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média é {:.1f}'.format(m))
#print('PARABÉNS' if m >=6 else 'ESTUDE MAIS')  #Condição simplificada.
if  m >= 6.0:
    print('Aluno Aprovado.')
else:
    print('Aluno não aprovado.')
