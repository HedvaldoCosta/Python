dic = {}
gols = []
dic['Nome'] = input('Nome do Jogador: ')
dic['jogos'] = int(input('Número de partidas jogadas: '))
for c in range(1, dic['jogos']+1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))

dic['gols'] = gols
dic['Total'] = sum(gols)
print(f'O jogador {dic["Nome"]} jogou {dic["jogos"]} partidas')
for c, v in enumerate(dic['gols']):
    print(f'Na partida {c + 1} fez {v} gols')
print(f'Total de {dic["Total"]} gols')



