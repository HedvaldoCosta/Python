#63-Fibonacci

# 1º opção

numero1 = 0
numero2 = 1
termos = int(input('Quantos termos? '))
print(f'{numero1} --> {numero2} -->', end=' ')
for c in range(3, termos + 1):
    numero3 = numero1 + numero2
    print(f'{numero3} -->', end=' ')
    numero1 = numero2
    numero2 = numero3

#2º opção

numero1 = 0
numero2 = 1
termos = int(input('Me diga quantos termos: '))
cont = 3
print(f'{numero1} --> {numero2} -->', end=' ')
while cont <= termos:
    numero3 = numero1 + numero2
    print(f'{numero3}  -->', end=' ')
    cont = cont + 1
    numero1 = numero2
    numero2 = numero3
   
# 3º opção

termos = int(input('Quantos termos: '))
numero1 = 0
numero2 = 1
resposta = 0
print(f'{numero1} -> {numero2} ->', end=' ')
contador = 3
while resposta != -1:
    termos = termos + resposta
    while contador <= termos:

        numero3 = numero1 + numero2
        print(f'{numero3} ->', end=' ')
        contador = contador + 1
        numero1 = numero2
        numero2 = numero3
    print('...')
    resp = int(input('Mais termos(-1 para sair): '))
    
    
