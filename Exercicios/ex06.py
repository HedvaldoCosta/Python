#6-Codigo para ler o dobro, triplo e a raiz de um numero
numero = int(input("Me diga um numero:"))
dobro = numero * 2
triplo = numero * 3
raiz = numero**(1/2)
print(f"dobro:\033[4;30m{dobro}\033[m, triplo:\033[4;31m{triplo}\033[m e raiz:\033[4;33m{raiz}\033[m")
