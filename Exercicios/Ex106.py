def ajuda(x):
    print(f'\033[31mACESSANDO O MANUAL DO {x.upper()}\033[m')
    help(x)


#Programa principal
while True:
    comando = str(input('Comando desejado[FIM para sair]: '))
    if comando.upper() == 'FIM':
        print('\033[31mPROGRAMA ENCERRADO\033[m')
        break
    else:
        ajuda(comando)