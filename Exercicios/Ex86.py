matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = maior = soma3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Me diga o valor [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        if matriz[l][c] % 2 == 0:
            somap = somap + matriz[l][c]
        if c == 2:
            soma3 = soma3 + matriz[l][2]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
    print()

print(f'A soma dos numeros pares dessa matriz é igual a {somap}')
print(f'A soma dos valores da terceira coluna é igual a {soma3}')
print(f'O maior valor da linha 2 é o {maior}')
