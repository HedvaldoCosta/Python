# Faça um programa que calcule o mostre a média aritmética de N notas.
c = s = 0
while True:
    c = c + 1
    nota = float(input(f'{c}º nota[ -1 para parar ]: '))
    if nota == -1:
        break
    else:
        s = s + nota
        media = s / c
print(f'{media:.2f}')

