jogador = {}
gols = []
jogadores = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas jogou? '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols fez na {c+1}º partida?')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    pergunta = str(input('Deseja continuar?[S/N]')).upper()[0].strip()
    while pergunta not in 'SsNn':
        pergunta = str(input('Deseja continuar?[S/N]')).upper()[0].strip()
    if pergunta == 'N':
        break
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<16}', end='')
    print()
while True:
    busca = int(input('Selecione o jogador[999 para sair]: '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print('NÃO EXISTE ESSE JOGADOR NA LISTA')
        busca = int(input('Selecione o jogador[999 para sair]: '))
    else:
        print(f'Levantamento do jogador: {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')


