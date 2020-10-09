mydic = {}
mydic['nome'] = str(input('Me diga seu nome: '))
mydic['Media'] = float(input('Media: '))
if mydic['Media'] >= 7:
    mydic['resultado'] = 'Aprovado'
else:
    mydic['resultado'] = 'Reprovado'
for c, v in mydic.items():
    print(f'{c} : {v}')