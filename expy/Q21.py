# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se
# a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então,
# dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
somaI = 0
c = 0
while True:
    idade = int(input('Sua idade [ 0 para parar ]: '))
    if idade == 0:
        break
    c = c + 1
    somaI = somaI + idade
    media = somaI/c
print(media)
if (0 < media) and (media < 26):
    print('Turma Jovem')
elif (media > 25) and (media < 61):
    print('Turma adulta')
elif media > 60:
    print('Turma idosa')