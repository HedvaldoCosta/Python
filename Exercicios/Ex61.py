#61-PA
termo = float(input('Primeiro termo: '))
razão = float(input('Razão entre eles: '))
c = 1
while c <= 10:
    print(f'{c}º termo:{termo}')
    c = c + 1
    termo = termo + razão
