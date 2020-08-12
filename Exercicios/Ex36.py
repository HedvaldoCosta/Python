#36-Aprovando emprestimo bancario
salario = float(input('Seu salario:'))
valor = float(input('Valor da casa:'))
anos = int(input('Em quantos anos deseja pagar?'))
pres = valor/(anos * 12)
mini = 0.3 * salario

if pres <= mini:
    print('Emprestimo APROVADO')
else:
    print('Emprestimo NEGADO')
