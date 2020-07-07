#17-Encontrando a hipotenusa de um triangulo
import math
catO = float(input("Valor do cateto oposto:"))
catA = float(input("Valor do cateto adjacente:"))
pit = (catA**2) + (catO**2)
hip = math.sqrt(pit)
print(f"Hipotenusa:{hip:.2f}")
