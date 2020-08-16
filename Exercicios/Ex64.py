#64-Varios valores
num = int(input('Diga- me um numero inteiro(999 para sair): '))
c = soma = 0

while num !=999:
    c = c + 1
    soma = soma + num
    num = int(input('Outro numero(999 para sair):'))


print(f'{c} números digitados')
print(f'A soma entre os numeros: {soma}')
