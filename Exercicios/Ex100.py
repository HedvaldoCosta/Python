codigo = 1234
senha = 9999
numeros = [0, 1]
#Código pricipal
while True:
    codigo_registro = int(input('Codigo:  '))
    if codigo_registro != codigo:
        print('ACESSO NEGADO')
        break
    else:
        senha_registro = int(input('Senha:'))
        if senha_registro == senha:
            print('ACESSO PERMITIDO')
        elif senha_registro != senha:
            print('Senha incorreta!')
            escolha = int(input('''[0] continuar
[1] sair
'''))
            while escolha not in numeros:
                escolha = int(input('''[0] continuar
[1] sair
'''))
            while escolha == 0:
                senha_registro = int(input('Senha:'))
                if senha_registro == senha:
                    print('ACESSO PERMITIDO')
                    exit()
                elif senha_registro != senha:
                    print('Senha incorreta!')
                    escolha = int(input('''[0] continuar
[1] sair
'''))
            if escolha == 1:
                break



