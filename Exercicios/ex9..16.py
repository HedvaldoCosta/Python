#Tabuada
numero = int(input("Me diga um numero:"))
print(f"{numero} x 1 =", numero*1)
print(f"{numero} x 2 =", numero*2)
print(f"{numero} x 3 =", numero*3)
print(f"{numero} x 4 =", numero*4)
print(f"{numero} x 5 =", numero*5)
print(f"{numero} x 6 =", numero*6)
print(f"{numero} x 7 =", numero*7)
print(f"{numero} x 8 =", numero*8)
print(f"{numero} x 9 =", numero*9)
print(f"{numero} x 10 =", numero*10)

#Conversor de dolar
din = float(input("Quanto dinheiro você possui?"))
con = din/3.27
print(f"Você pode comprar:{con}")

#Area da parede
larg = float(input("Largura da parede:"))
alt = float(input("Altura da parede:"))
area = (larg * alt)
print(f"Area da parede:{area} metros²")
pint = area/2
print(f"É necessario {pint} litros de tinta para pintar toda a parede")

#Desconto
preco = float(input("Preço do produto:"))
desc = preco + (0.05 * preco)
print(f"Preço com o desconto: {desc}")

#Salario
salario = float(input("Salario atual:"))
reaj = salario + (0.15 * salario)
print(f"Novo salario:{reaj}")

#Conversor de temperatura(C > F)
cel = float(input("Temperatura em Celsius:"))
far = (cel * (9/5)) + 32
print(f"Temperatura fahrenheit: {far}")
