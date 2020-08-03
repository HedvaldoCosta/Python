# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
# bem como a média das temperaturas.
menor = maior = c = 0
while True:
    esc = int(input('''[ 1 ] para Celsius
[ 2 ] para Kelvin
[ 3 ] para Fahrenheit
[ 4 ] para sair
Sua opção: '''))
    if esc == 4:
        print('\033[31m PROGRAMA FINALIZADO\033[m')
        break
    c = c + 1
    temp = float(input('Tempertura: '))
    if esc == 2:
        temp = temp - 273.15
    if esc == 3:
        temp = (temp - 32) * 5/9
    if c == 1:
        maior = temp
        menor = temp
    else:
        if maior < temp:
            maior = temp
        if menor > temp:
            menor = temp
    print(f'Maior temperatura: {maior:.2f} °C')
    print(f'Menor temperatura: {menor:.2f} °C')
