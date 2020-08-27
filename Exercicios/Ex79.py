lista = []
while True:
    numero = int(input('Me diga um numero: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('VALOR REPETIDO')
    resposta = input('Deseja continuar? [S/N]').upper().strip()[0]
    while resposta not in 'SsNn':
        resposta = input('Deseja continuar? [S/N]').upper().strip()[0]
    if resposta == 'N':
        break
print(sorted(lista))
