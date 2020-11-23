# Cada string vai receber um conjunto de índice iniciando do 0 (incluindo espaços)
#Ex:
print('Olá')
# Olá possui 3 índices
print('tudo bem')
# Tudo bem possui 8 índices

# Verificando um índice:
frase = ('Curso de python')
# Se fizermos frase[9] ele irá pegar o 9º índice de frase
frase[9] = 'p'

#Escolhendo índices:
# Se fizermos frase[9:14] irá pegar no 9º índice até 13º (no python exclui-se o último termo)
frase[9:13] = 'pytho'

# Se fizermos frase[:5] ele irá pegar do 1º índice até o 4º
frase[:5] = 'Curso'

# Se fizermos frase[3:] ele irá pegar do 3º índice até o último
frase[3:] = 'so de python'
# Pulando índices:
# Se fizermos frase[0:15:2] ele irá pular de 2 em 2
frase[0:15:2] = 'Crod yhn'

# Se fizermos frase[4::3] ele irá do 4º termo até o último pulando de 3 em 3
frase[4::3] = 'oeyo'

# Comprimento da string:
    #Utilizando o método len() podesse encontrar o tamanho de uma string
    # Se utilizarmos len(frase) então:
#len(frase) = 15

# Contando o mesmo termo:
    #Utilizando o método count() podemos verificar quantas vezes o mesmo termo apareceu na string
    # Usando frase.count(termo):
#frase.count('o') = 2

# Verificando se está dentro da variável:
# 'python' in frase
#Irá devolver o valor True se python estiver na variável frase
