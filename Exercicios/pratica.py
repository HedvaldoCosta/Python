from random import randint
from time import sleep
# Advinhando um numero
c=randint(0, 5)
ad=int(input("Tente advinhar um numero entre 0 e 5: "))
print("Processando...")
sleep(1)
if ad==c:
    print("Você acertou!")
else:
    print("Você errou. Eu pensei no {}".format(c))

print("---" * 10)
# par ou impar
n=float(input("Me diga um numero: "))
n1=n%2
if n1==0:
    print("Esse numero é par")
else:
    print("Esse numero é impar")
print("---" * 10)
#Ler o salario
s=float(input("Qual o seu salario fixo mensal? "))
v=float(input("Valor de suas vendas é igual a: "))
v1=v*(3/100)
v2=v-1500
v3=v2*(5/100)
v4=s+v1
v5=s+v1+v3

if v<=1500:
    print("O salario total é de {}".format(v4))
if v>1500:
    print("O salario total é de {}".format(v5))




