lista = list()
dado = list()
for c in range(1, 4):
    dado.append(str(input('Seu nome:')))
    dado.append(int(input('Sua idade: ')))
    lista.append(dado[:])
    dado.clear()
for p in lista:
    if p[1] >= 21:
        print('Maior')
    else:
        print('Menor')
