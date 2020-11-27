def notas(*x):
    dados = dict()
    dados['Quantidade de notas'] = len(x)
    dados['Maior nota'] = max(x)
    dados['Menor nota'] = min(x)
    dados['Média'] = f'{sum(x) / len(x):.2f}'
    return dados


#programa principal
n = notas(5.5, 8.5, 6)
print(n)