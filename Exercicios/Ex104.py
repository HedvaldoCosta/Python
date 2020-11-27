def leiaint(x):
    c = input(x)
    while not c.isnumeric():
        print('Não é número inteiro')
        c = input(x)
    if c.isnumeric():
        print(f'{c} é um número inteiro')


#Programa principal
n = leiaint('Me diga um numero:')
