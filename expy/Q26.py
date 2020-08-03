# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles
# estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deverá terminar quando for lido um número negativo.
c = cont = ct = contador = 0
while True:
    num = int(input('Numero desejado [negativo para sair]: '))
    if num < 0:
        break
    if (num >= 0) and (num <= 25):
        c = c + 1
    elif (num > 25) and (num <= 50):
        cont = cont + 1
    elif (num > 50) and (num <=75):
        ct = ct + 1
    elif (num > 76) and (num <= 100):
        contador = contador + 1
print(f'{c} numeros entre [0-25]')
print(f'{cont} numeros entre [26-50]')
print(f'{ct} numeros entre [51-75]')
print(f'{contador} numeros entre [76-100]')