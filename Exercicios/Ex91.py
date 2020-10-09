from datetime import date
dados = {}
ano = date.today().year
dados['nome'] = input('Nome: ')
dados['Ano de Nascimento'] = int(input('Ano de nascimento: '))
dados['idade'] = ano - dados['Ano de Nascimento']
dados['ctps'] = int(input('Carteira de trabalho[0 não tem]: '))
if dados['ctps'] > 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario Atual: '))
    dados['Aposentadoria'] = dados['idade'] + (dados['Ano de contratação'] + 35) - ano
for c, v in dados.items():
    print(f'{c} = {v}')


