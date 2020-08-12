#37-Conversor de bases numericas
numero = int(input('Me diga um numero inteiro:'))
resp = int(input("""[1] para binario
[2] para octal
[3] para hexadecimal
"""))

if resp == 1:
    print(bin(numero)[2:])
elif resp == 2:
    print(oct(numero)[2:])
elif resp == 3:
    print(hex(numero)[2:])
else:
    print('\033[31mCOMANDO INVALIDO')
