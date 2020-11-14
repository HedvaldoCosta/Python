def escreva(msg):
    tamanho = len(msg)
    print('~' * tamanho)
    print(msg)
    print('~' * tamanho)


while True:
    mensagem = str(input('Me diga sua mensagem: '))
    escreva(mensagem)
    resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resposta == 'N':
        break