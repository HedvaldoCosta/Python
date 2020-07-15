# Numero Primo
for c in range(1, 6):
    num = int(input("Diga-me um numero:"))
    if (num % 2 == 1) or num == 2:
        print("Número primo")
    else:
        print("Não é primo")