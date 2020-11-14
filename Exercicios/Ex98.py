def maior(* num):
    maior = contador = 0
    for valor in num:
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(maior)

#Codigo Principal
maior(4556, 0, 567, 90, 120)

