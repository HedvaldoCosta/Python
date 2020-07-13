#Media
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota2 + nota1)/2

if media < 5:
    print('\033[31mREPROVADO')
elif media >= 5 and media <= 6.9:
    print('\033[33mRECUPERAÇÃO')
elif media >= 7:
    print('\033[32mAPROVADO')