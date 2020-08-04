# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('Zero', 'Um', 'dois', 'três', 'Quatro', 'Cinco',
          'Seis', 'sete', 'Oito', 'nove', 'dez',
          'Onze', 'Doze', 'treze', 'catorze', 'quinze',
          'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Me diga um numero entre 0 e 20: '))
    while num < 0 or num > 20:
        print('Numero invalido. Escolha apenas numeros entre 0 e 20')
        num = int(input('Me diga um numero entre 0 e 20: '))
    print(numero[num])


