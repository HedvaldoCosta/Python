def contador(inicio, fim, passo):
    print()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        contador = inicio
        while contador <= fim:
            print(contador, end='  ')
            contador += passo
    else:
        contador = inicio
        while contador >= fim:
            print(contador, end='  ')
            contador -= passo


contador(1, 10, 1)
contador(10, 0, 2)
print()
print('Sua vez de fazer o contador')
while True:
    print()
    i = float(input('Inicio:'))
    f = float(input('Fim:'))
    p = float(input('Passo:'))
    contador(i, f, p)
    print()
    resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while resposta not in 'SN':
        print()
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        print('Codigo finalizado')
        break

