def ficha(n='desconhecido', g='0'):
    print(f'O jogador {n} marcou {g} gols')


#Programa Principal
nome = str(input('Nome do jogador:  '))
gols = str(input('Número de gols:  '))
if gols.isnumeric():
    int(gols)
else:
   gols = 0
if nome.isalpha():
    str(nome)
else:
    nome = 'Desconhecido'
ficha(nome, gols)