pessoas = {}
nomes = []
media = soma = 0
while True:
    pessoas.clear()
    pessoas['nomes'] = str(input('Nome: '))
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    pessoas['sexo'] = (str(input('Sexo[M/F]: ')).upper()[0].strip())
    while pessoas['sexo'] not in 'MmFf':
        sexo = (str(input('Sexo[M/F]: ')).upper()[0].strip())
    nomes.append(pessoas.copy())
    resp = str(input('''Deseja continuar?[S/N]
''')).upper().strip()[0]
    while resp not in 'SsNn':
        resp = str(input('''Deseja continuar?[S/N]
''')).upper().strip()[0]
    if resp == 'N':
        break
media = soma / len(nomes)
print(f'Número de pessoas cadastradas: {len(nomes)}')
print(f'Média de idades = {media:.2f}')
print('Mulheres na lista')
for c in nomes:
    if c['sexo'] in 'F':
        print(f'{c["nomes"]}, ', end='')
print()
print('Homens na lista')
for h in nomes:
    if h['sexo'] in 'M':
        print(f'{h["nomes"]}, ', end='')
print()
print('Pessoas acima da media de idade')
for i in nomes:
    if i['idade'] > media:
        print(f'{i["nomes"]}, ', end='')


