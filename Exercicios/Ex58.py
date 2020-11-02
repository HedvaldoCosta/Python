n = 0
while True:
    n = n + 1
    resposta = str(input('Deseja iniciar?'))
    if resposta == 's':
        print(f'P({n}) = {n/(n + 1):.2f}')
    else:
        break