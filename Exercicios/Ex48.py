# Somando os numeros multiplos de 3
s = 0
for c in range(0, 501, 3):
    s = s + c
print("Soma total: {}".format(s))