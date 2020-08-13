#42-Classificando triangulos
r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3:'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Pode formar um triangulo!')
    if r1 == r2 == r3:
        print('Triangulo equilatero')
    if (r1 == r2 != r3) or (r1 == r3 != r2) or (r3 == r2 != r1):
        print('triangulo isosceles')
    if (r1 != r2 and r3) and (r2 != r1 and r3) and (r3 != r1 and r2):
        print('Triangulo escaleno')
else:
    print('Não pode formar um triangulo!')

