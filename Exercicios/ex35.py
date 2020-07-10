#Formação de um triangulo
r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3:'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Pode formar um triangulo!')
else:
    print('Não pode formar um triangulo!')