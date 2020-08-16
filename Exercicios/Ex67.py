#67-Tabuada 3.0
while True:
    num = int(input('''Deseja ver a tabuada de que numero?
[Numero negativo para sair]
R: '''))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} X {c} = {num * c}')
print('\033[31mPROGRAMA FINALIZADO')

