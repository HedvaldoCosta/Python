#48-Somando os numeros multiplos de 3
s = 0
for c in range(3, 501, 6):
    s = s + c

print("Soma total: {}".format(s))
