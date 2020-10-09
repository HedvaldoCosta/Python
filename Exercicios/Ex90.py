from random import randint
from operator import itemgetter
dados = {}
dados['results1'] = randint(1, 6)
dados['results2'] = randint(1, 6)
dados['results3'] = randint(1, 6)
dados['results4'] = randint(1, 6)
ranking = {}
for c, v in dados.items():
    print(f'{c} = {v}')
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for c, v in enumerate(ranking):
    print(f'{c+1}º lugar: {v[0]} com {v[1]}')

