def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mMe diga um valor inteiro valido!!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário interrompeu o sistema\033[m')
            return 0
        else:
            return n


def linha():
    return '===' * 10


def cabeçalho(msg):
    print(linha())
    print(msg.center(35))
    print(linha())


def menu(lista):
    cabeçalho('\033[33mSISTEMA MENU\033[m')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua Opção: ')
    return opc
