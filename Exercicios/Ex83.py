lista = []
tot = []
c = maior = menor = 0

while True:
    c = c + 1
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if c == 1:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    tot.append(lista[:])
    lista.clear()
    resp = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'Ao todo foram cadastrados {c} pessoas')
print(f'Maior peso:{maior}KG foi de ', end=' ')
for p in tot:
    if p[1] == maior:
        print(f'>{p[0]}<', end=' ')
print()
print(f'Menor peso: {menor}KG foi de ', end= ' ')
for p in tot:
    if p[1] == menor:
        print(f'>{p[0]}<', end=' ')




