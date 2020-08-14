#52-Numero Primo
s = 0
num = int(input('Diga-me um numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[31m", end=" ")
        s = s + 1
    else:
        print("\033[30m", end=" ")
    print(c, end=" ")
if s == 2:
        print(f"{num} NÚMERO PRIMO")
else:
        print(f"{num} NÃO É PRIMO")
