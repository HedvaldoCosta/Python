#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que
# calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a
# população do país B, mantidas as taxas de crescimento.
c = 0
popA = 80000
popB = 200000
while popA < popB:
    c = c + 1
    popA = popA + (popA * 0.03)
    popB = popB + (popB * 0.015)
print(f'População A: {popA:.0f}')
print(f'População B: {popB:.0f}')
print(f'Numero de anos: {c}')