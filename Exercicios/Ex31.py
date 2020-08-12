#31-Calculando o preço da viagem
dist = float(input('Viagem de quantos KM? '))
if dist <= 200:
    print(f'preço a ser pago: {dist * 0.5}')
else:
    print(f'Valor a ser pago: {dist * 0.45}')
