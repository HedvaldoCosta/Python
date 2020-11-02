from random import randint
rand = randint(1, 25)
c = 0
while True:
    num = int(input('Chute um numero entre 1 e 25: '))
    c = c + 1
    if num < rand:
        print('Tente chutar um numero maior')
    elif num > rand:
        print('Tente chutar um numero menor')
    else:
        print('Você acertou!')
        break
print(f'Numero de tentativas: {c}')
