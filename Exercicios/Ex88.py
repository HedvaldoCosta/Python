alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1º nota: '))
    nota2 = float(input('2º nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"Nº":<4} {"Nome":<10} {"Media":>8}')
for i, a in enumerate(alunos):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')
while True:
    esc = int(input('''Deseja ver as notas de qual aluno? [999 para sair]
'''))
    if esc == 999:
        break
    if esc <= len(alunos) - 1:
        print(f'Notas do {alunos[esc][0]} são {alunos[esc][1]}')