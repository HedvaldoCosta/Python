#15-Aluguel de carro
dias = int(input("Dias com o carro alugado:"))
dist = float(input("KM rodados:"))
valor = (60 * dias) + (0.15 * dist)
print(f"Preço a ser pago:{valor:.2f}")
