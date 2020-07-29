# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o décimo termo.
n = n3 = c = 0
n2 = 1
print(f'{n}...{n2}...', end='')
while c < 8:
    n3 = n + n2
    print(f'{n3}...', end='')
    c = c + 1
    n = n2
    n2 = n3



