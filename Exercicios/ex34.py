#Aumento de salario
salario = float(input('Salario:'))

if salario <= 1250:
    aumento = salario + (salario * 0.15)
else:
    aumento = salario + (salario * 0.10)
print(f'Novo salario:{aumento}')
