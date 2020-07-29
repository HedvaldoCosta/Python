# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500
n = n3 = 0
n2 = 1
print(f'{n}...{n2}...', end='')
while n3 < 500:
    n3 = n + n2
    print(f'{n3}...', end='')
    n = n2
    n2 = n3

