#Lendo dados

c18 = cm = cf = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        c18 = c18 + 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        cm = cm + 1
    if sexo == 'F' and idade < 22:
        cf = cf + 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar?[S/N]:')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Pessoas maiores de 18 anos: {c18}')
print(f'Mulheres com menos de 22 anos: {cf}')
print(f'Total de homens cadastrados: {cm}')