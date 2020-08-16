#66-Soma com flag
s = c = 0
while True:
    num = int(input('Me diga um numero[999 para sair]: '))
    if num == 999:
        break
    s = s + num
    c = c + 1
print(f'Soma entre os numeros:{s}')
print(f'Numeros digitados: {c}')
