#70-Preço dos produtos
soma = c = menor = cont =  0
nome = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    cont = cont + 1
    if cont == 1:
        menor = preco
        nome = produto
    else:
        if preco < menor:
            menor = preco
            nome = produto
    if preco > 1000:
        c = c + 1
    soma = soma + preco
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Valor total: {soma:.2f}')
print(f'Numero de produtos que custam mais de 1000$: {c}')
print(f'Produto mais barato: {nome}')
