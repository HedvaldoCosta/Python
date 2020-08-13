#41-Classificando atletas
idade = int(input('Sua Idade:'))

if idade <= 9 and idade > 0:
    print('MIRIM')
elif idade > 9 and idade <=14 and idade > 0:
    print('INFANTIL')
elif idade > 0 and idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade == 20 and idade > 0:
    print('SÊNIOR')
elif idade > 20 and idade > 0:
    print('MASTER')
if idade < 0:
    print('\033[4;31mHAHA CLASSIC!!!')
