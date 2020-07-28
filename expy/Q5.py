# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.
cA = cB = 0
resposta = ' '
while resposta != 'N':
    pA = int(input('População do país A: '))
    pcA = float(input('Porcentagem de crescimento do país A: '))/100
    pB = int(input('População B: '))
    pcB = float(input('Porcentagem de crescimento do país B: '))/100
    if pB > pA:
        while pA < pB:
            cA = cA + 1
            pA = pA + (pA * pcA)
            pB = pB + (pB * pcB)
        print(f'População A: {pA:.0f}')
        print(f'População B: {pB:.0f}')
        print(f'Numero de anos: {cA}')
    else:
        while pB < pA:
            cB = cB + 1
            pB = pB + (pB * pcB)
            pA = pA + (pA * pcA)
        print(f'População A: {pA:.0f}')
        print(f'População B: {pB:.0f}')
        print(f'Numero de anos: {cB}')
    resposta = str(input('[S/N]')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('[S/N]')).upper().strip()[0]



