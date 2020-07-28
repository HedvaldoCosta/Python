# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
while True:
    nome = str(input('Seu nome:'))
    while len(nome) <= 3:
        print('INVALIDO')
        nome = str(input('Seu nome: '))

    idade = int(input('Sua idade:'))
    while idade < 0 or idade > 150:
        print('INVALIDO')
        idade = int(input('Sua idade:'))

    salario = float(input('Seu salario: '))
    while salario < 0:
        print('INVALIDO')
        salario = float(input('Seu salario: '))

    sexo = str(input('Seu sexo:[F/M]')).upper().strip()[0]
    while sexo not in 'FM':
        print('INVALIDO')
        sexo = str(input('Seu sexo:[F/M]')).upper().strip()[0]

    est = str(input('''Estado Civil:
[ s ] para solteiro
[ c ] para casado
[ v ] para viuvo
[ d ] para divorciado
opção: ''')).upper().strip()[0]
    while est not in 'SCVD':
        print('INVALIDO')
        est = str(input('''Estado Civil:
[ s ] para solteiro(a)
[ c ] para casado(a)
[ v ] para viuvo(a)
[ d ] para divorciado(a)
opção: ''')).upper().strip()[0]

    if est == 'S':
        est = 'Solteiro'
    elif est == 'C':
        est = 'Casado'
    elif est == 'V':
        est = 'Viuvo'
    elif est == 'D':
        est = 'Divorciado'

    if sexo == 'F':
        sexo = 'Feminino'
    else:
        sexo = 'Masculino'
    break

print(f'''Nome: {nome}
Idade: {idade} anos
sexo: {sexo}
salario: {salario}R$
Estado Civil: {est}''')






