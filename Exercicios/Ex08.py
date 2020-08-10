#8-Conversor de medidas
medida = float(input("Me diga um valor em metros:"))
cen = medida * 100
mil = medida * 1000
print(f"centimetros:\033[33m{cen}\033[m e milimetros:\033[30m{mil}\033[m")
