# Palindromo
palav = str(input("Me diga uma frase:")).strip().upper()
sep = palav.split()
juntando = ''.join(sep)
inv = ''
for c in range(len(juntando) -1, -1, -1):
    inv = inv + juntando[c]
if inv == juntando:
    print(('Palindromo'))
else:
    print('Não é palindromo')