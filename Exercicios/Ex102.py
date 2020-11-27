def fatorial(x, show=False):
    f = 1
    for c in range(x, 0, -1):
        f *= c
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
    return f


#programa principal
numero = int(input('Diga-me um numero:  '))
print(fatorial(numero, show=True))