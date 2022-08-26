n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2
print('A soma vale = {} '.format(s), end='') #o end não quebra a linha.
print('A mutiplicação é = {} '.format(m))
print('A divisão é = {}'.format(d))
print('A divisão inteira é = {}'.format(di))
print('A exponenciação é = {} '.format(e))
print('O resto da divisão é = {}'.format(rd))