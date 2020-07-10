#Maior numero e menor numero
n1 = int(input('1º numero: '))
n2 = int(input('2º numero: '))
n3 = int(input('3º numero: '))
#Menor valor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Maior valor
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'Maior valor:{maior} ')
print(f'Menor valor:{menor}')
