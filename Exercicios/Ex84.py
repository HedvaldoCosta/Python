lista = [[], []]
for c in range(1, 8):
    numero = int(input('Numero: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print(f'Numeros pares: {sorted(lista[0])}')
print(f'Numeros impares: {sorted(lista[1])}')
