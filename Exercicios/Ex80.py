lista = []
while True:
    lista.append(int(input('Me diga um numero: ')))
    resp = input('Deseja continuar?[S/N]').strip().upper()[0]
    while resp not in 'SsNn':
        resp = input('Deseja continuar?[S/N]').strip().upper()[0]
    if resp == 'N':
        break
print(f'Numero de elementos na lista: {len(lista)}')
print(f'Ordem decrescente: {sorted(lista, reverse=True)}')
if 5 not in lista:
    print('Numero 5 não apareceu nessa lista')
else:
    print(f'O numero 5 apareceu {lista.count(5)} vezes')



