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


def leiafloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mMe diga um valor real valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário interrompeu o sistema\033[m')
            return 0
        else:
            return numero


numint = leiaint('Me diga um numero inteiro:  ')
print(f'O valor digitado foi {numint}')
numfloat = leiafloat('Me diga um numero real:  ')
print(f'O valor real foi {numfloat}')

