#44-Gerenciando pagamentos
produto = float(input('Valor do produto: '))
condição = int(input('''[ 1 ] para à vista/cheque
[ 2 ] para à vista no cartão
[ 3 ] para 2x no cartão
[ 4 ] para 3x ou mais no cartão
Opção desejada: '''))

if condição == 1:
    valor = (produto - (produto * 0.10))
elif condição == 2:
    valor = (produto - (produto * 0.05))
elif condição == 3:
    valor = (produto)
else:
    valor = (produto + (produto * 0.20))
print(f'Valor total a ser pago: {valor}$ ')
