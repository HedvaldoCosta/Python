# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário.
from datetime import date
salario = 1015
aumento = 0.030
data = date.today().year
for c in range(1997, data):
    salario = salario + (aumento * salario)
    aumento = aumento * 2
print(f'Salario atual: {salario:.2f}')


