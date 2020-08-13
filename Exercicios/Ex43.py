#43-IMC
altura = float(input('Sua altura: '))
peso = float(input('Seu peso:'))
imc = peso/(altura**2)

if imc < 18.5:
    print(('ABAIXO DO PESO'))
elif imc > 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBRE PESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')
print(f'O IMC dessa pessoa é {imc:.2f}')
