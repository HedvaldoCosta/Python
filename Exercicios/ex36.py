#Aprovando emprestimo bancario
salario = float(input('Seu salario:'))
valor = float(input('Valor da casa:'))
anos = int(input('Em quantos anos deseja pagar?'))
mes = anos * 12
sal = (0.3 * salario)
pagar = salario * mes
dif = valor - pagar

if dif > 0:
    print('Você não irá conseguir comprar essa casa nesse tempo')
    print(f'Falta:{valor - dif}')
elif (sal * mes) < valor:
    print('Emprestimo negado')
elif (sal * mes) >= valor:
    print('Emprestimo aceito')


