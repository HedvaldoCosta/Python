#50-Soma dos Pares
s = 0
for c in range(1, 7):
    num = int(input(f"Diga-me o {c}º numero:"))
    if num % 2 == 0:
        s = s + num
print(f"Soma dos pares:{s}")

