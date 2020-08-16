#62-PA2.0
termo = float(input('Me diga um numero: '))
razão = float(input('Razão entre eles: '))
c = 1
total = 0
resp = 10
while resp != 0:
    total = total + resp
    while c <= total:
        c = c + 1
        print(f'{termo} ->', end=' ' )
        termo = termo + razão
    print('...')
    resp = int(input('''Deseja adicionar mais quantos termos?(0 para sair)
    '''))
print('Programa finalizado')
print(f'{total} termos')
