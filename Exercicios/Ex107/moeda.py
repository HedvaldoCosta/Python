from Ex107 import conversor
preco = float(input('Preço:  '))
print(f'{preco} + 10% = {conversor.aumento(preco):.2f}')
print(f'{preco} - 10% = {conversor.diminuir(preco):.2f}')
print(f'O dobro de {preco} é {conversor.dobro(preco):.2f}')
print(f'A metade de {preco} é {conversor.metade(preco):.2f}')
