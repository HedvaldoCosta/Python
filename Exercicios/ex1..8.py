#1-Codigo para escrever uma saudação
print("Ola, mundo")

#2-Codigo para dar boas vindas ao usuario
nome = input("Como você se chama?")
print(f"{nome}, seja muito bem-vindo")

#3-Codigo para somar dois numeros
numero1 = int(input("Me diga um numero:"))
numero2 = int(input("Me diga outro:"))
soma = (numero1 + numero2)
print(f"A soma entre {numero1} e {numero2} é igual a {soma}")

#4-Dissecando uma variavel
a = input("Me diga algo")
print("É numerico?", a.isnumeric())
print("É alfabetico?", a.isalpha())
#5-Antecessor e sucessor
num = int(input("Me diga um numero:"))
ant = num - 1
suc = num + 1
print(f"Antecessor:{ant} e sucessor:{suc}")

#6-Codigo para ler o dobro, triplo e a raiz de um numero
numero = int(input("Me diga um numero:"))
dobro = numero * 2
triplo = numero * 3
raiz = numero**(1/2)
print(f"dobro:{dobro}, triplo:{triplo} e raiz:{raiz}")

#7-Media de um aluno
nota = float(input("Me diga a primeira nota:"))
nota2 = float(input("Me diga a segunda nota:"))
media = (nota + nota2)/2
print(f"Media: {media}")

#8-Conversor de medidas
medida = float(input("Me diga um valor em metros:"))
cen = medida * 100
mil = medida * 1000
print(f"centimetros:{cen} e milimetros:{mil}")

