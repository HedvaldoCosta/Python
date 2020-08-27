exp = str(input('Me diga a expressão: '))
lista = []
for simbolo in exp:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Expressão valida')
else:
    print('Expressão invalida')
    