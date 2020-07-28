# Altere o programa anterior para mostrar no final a soma dos números.
s = 0
num = int(input('1º numero: '))
num2 = int(input('2º numero: ')) + 1
if num < num2:
    for c in range(num, num2):
        s = s + c
else:
    for c in range(num2, num + 1):
        s = s + c
print(f'A soma dos numeros é igual a: {s}')


