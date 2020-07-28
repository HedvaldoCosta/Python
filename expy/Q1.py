# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido
while True:
    nota = -1
    nota = int(input('Me diga uma nota entre 0 e 10: '))
    while nota < 0 or nota > 10:
        print('Valor invalido')
        nota = int(input('Me diga uma nota entre 0 e 10: '))
    if nota >= 0 and nota < 10:
        break