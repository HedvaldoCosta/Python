from Ex109 import conversor
preco = float(input('Preço:  '))
print(f'{conversor.formatar(preco)} + 10% = {conversor.aumento(preco, True)}')
print(f'{conversor.formatar(preco)} - 10% = {conversor.diminuir(preco, True)}')
print(f'O dobro de {conversor.formatar(preco)} é {conversor.dobro(preco, True)}')
print(f'A metade de {conversor.formatar(preco)} é {conversor.metade(preco, True)}')
