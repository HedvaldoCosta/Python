#71-caixa eletronico
valor = int(input('Valor que deseja retirar: R$'))
total = valor
ced = 50
sced = 0
while True:
    if total >= ced:
        total = total - ced
        sced = sced + 1
    else:
        if sced > 0:
            print(f'Total de cedulas de {ced}: {sced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        sced = 0
        if total == 0:
            break
