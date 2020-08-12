#30-Ler se o numero é par ou impar
numero = int(input('Me fale um numero:'))
num = numero % 2

if num == 0:
    print('Numero par')
else:
    print('Numero impar')
