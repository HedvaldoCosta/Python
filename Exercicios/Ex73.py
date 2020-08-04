# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.

# b) Os últimos 4 colocados.

# c) Times em ordem alfabética.

# d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atletico-PR', 'São Paulo',
         'Internacional', 'Corinthians', 'Fortaleza', 'Goias', 'Bahia', 'Vasco',
         'Atletico-MG', 'Fluminense', 'Botafogo', 'Ceara', 'Cruzeiro', 'CSA',
         'Chapecoense', 'Avai')
print(f'5 primeiros times: {times[0:5]}')
print('====='* 20)
print(f'Ultimos 5 times: {times[15:20]}')
print('====='* 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('====='* 20)
print(f'Posição da Chapecoense: {times.index("Chapecoense")+1}º')