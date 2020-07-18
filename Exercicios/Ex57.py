#Validando dados
sexo = str(input('Seu sexo(M/F): ')).upper().strip()[0]
if sexo != 'M, F':
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Dado invalido. Digite seu sexo: ')).upper().strip()[0]
if sexo == 'M':
    print('Masculino')
elif sexo == 'F':
    print('Feminino')

