lista = []
impar = []
par = []
while True:
    numero = int(input('Me diga um numero'))
    lista.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    resp = input('Deseja continuar?[S/N]').strip().upper()[0]
    while resp not in 'SsNn':
        resp = input('Deseja continuar?[S/N]').strip().upper()[0]
    if resp == 'N':
        break
print(lista)
print(f'Lista impar: {impar}')
print(f'Lista par: {par}')
