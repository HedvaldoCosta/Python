def leiadinheiro(msg):
    valor = False
    while not valor:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('ERROR')
        else:
            valor = True
            return float(entrada)