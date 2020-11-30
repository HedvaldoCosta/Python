def aumento(p=0, formata=False):
    p = p + (p * 0.10)
    return p if not formata else formatar(p)


def diminuir(p=0, formata=False):
    p -= p * 0.10
    return p if not formata else formatar(p)


def dobro(p=0, formata=False):
    p *= 2
    return p if not formata else formatar(p)


def metade(p=0, formata=False):
    p /= 2
    return p if not formata else formatar(p)


def formatar(p=0, formatando='R$'):
    return f'{formatando}{p:.2f}'.replace('.', ',')


def resumo(p=0):
    print(f'Dobro do preço: {dobro(p, True)}')
    print(f'Metade do preço: {metade(p, True)}')
    print(f'Preço + 10% = {aumento(p, True)}')
    print(f'Preço - 10% = {diminuir(p, True)}')



