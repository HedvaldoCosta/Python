
# Analisando grupos
totmul = 0
maiori = 0
somai = 0
for c in range(1, 5):
    nome = str(input(f'Nome da {c}º pessoa: '))
    idade = int(input(f'Idade da {c}º pessoa: '))
    somai = idade + somai
    sexo = str(input(f'Sexo da {c}º pessoa(M/F): ')).upper()
    if c == 1 and sexo == 'M':
        maiori = idade
        nomev = nome
    if sexo == 'M' and idade > maiori:
        maiori = idade
        nomev = nome
    if sexo == 'F' and idade < 20:
        totmul = totmul + 1


print(f"O homem mais velho possui {maiori} anos e seu nome é {nomev} ")
print(f"Media = {somai/c:.2f}")
print(f'Total de mulheres com menos de 20 anos: {totmul}')