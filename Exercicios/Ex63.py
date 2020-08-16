#63-Fibonacci
termos = int(input('Quantos termos: '))
t = 0
t1 = 1
resp = 0
print(f'{t} -> {t1} ->', end=' ')
c = 3
while resp != -1:
    termos = termos + resp
    while c <= termos:

        t2 = t + t1
        print(f'{t2} ->', end=' ')
        c = c + 1
        t = t1
        t1 = t2
    print('...')
    resp = int(input('Mais termos(-1 para sair): '))
