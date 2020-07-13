#Conversor de bases numericas
numero = int(input('Me diga um numero inteiro:'))
resp = int(input("""[1] para binario
[2] para octal
[3] para hexadecimal
"""))

if resp == 1:
    print(bin(numero))
elif resp == 2:
    print(oct(numero))
elif resp == 3:
    print(hex(numero))