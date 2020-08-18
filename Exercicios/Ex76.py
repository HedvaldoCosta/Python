#76-Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

precos = ('Computador', 3500,
          'celular', 1250,
          'relogio', 690,
          'notebook', 2100)
for tabela in range(0, len(precos)):
    if tabela % 2 == 0:
        print(f'{precos[tabela]:.<20}', end='')
    elif tabela % 2 == 1:
        print(f'R${precos[tabela]:>3}')
