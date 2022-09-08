#Modulo de cores com padrão ANSI.

cor = {'limpa':'\033[m',
       'branca':'\033[40m',
       'vermelho':'\033[31;40m',
       'verde':'\033[32;40m',
       'amarelo':'\033[34;40m',
       'azul':'\033[34;40m',
       'roxo':'\033[35;40m',
       'cinza':'\033[47;40m'

       }

if __name__== '__main__':
       print('{} Olá mundo! {}'.format(cor['branca'], cor['limpa']))
       print('{} Olá mundo! {}'.format(cor['vermelho'],cor['limpa']))
       print('{} Olá mundo! {}'.format(cor['verde'], cor['limpa']))
       print('{} Olá mundo! {}'.format(cor['amarelo'], cor['limpa']))
       print('{} Olá mundo! {}'.format(cor['azul'], cor['limpa']))
       print('{} Olá mundo! {}'.format(cor['roxo'], cor['limpa']))
       print('{} Olá mundo! {}'.format(cor['cinza'], cor['limpa']))



