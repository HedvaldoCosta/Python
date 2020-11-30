def aumento(p=0):
    p = p + (p * 0.10)
    return p


def diminuir(p=0):
    p -= p * 0.10
    return p


def dobro(p=0):
    p *= 2
    return p


def metade(p=0):
    p /= 2
    return p


def formatar(p=0, formatando='R$'):
    return f'{formatando}{p:.2f}'.replace('.', ',')