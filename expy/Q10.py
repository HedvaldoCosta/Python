# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no
# intervalo compreendido por eles.
num = int(input('1º numero: '))
num2 = int(input('2º numero: '))
if num < num2:
    for c in range(num, num2 + 1):
        print(c)
else:
    for c in range(num2, num + 1):
        print(c)