#Mostrar quantas vezes a letra A foi escrita e em que posição
frase = str(input('Digite uma frase:')).strip()
print('A letra A aparece: {} vezes'.format(frase.upper().count('A')))
print('A primeira letra A encontrada esta na posição: {}'.format(frase.upper().find('A')+1))
print('A ultima letra A encontrada esta na posição: {}'.format(frase.upper().rfind('A')+1))