from Ex108 import conversor
preco = float(input('Preço:  '))
print(f'{conversor.formatar(preco)} + 10% = {conversor.formatar(conversor.aumento(preco))}')
print(f'{conversor.formatar(preco)} - 10% = {conversor.formatar(conversor.diminuir(preco))}')
print(f'O dobro de {conversor.formatar(preco)} é {conversor.formatar(conversor.dobro(preco))}')
print(f'A metade de {conversor.formatar(preco)} é {conversor.formatar(conversor.metade(preco))}')
