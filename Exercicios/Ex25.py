#25-Verificar se existe 'Silva' no nome da pessoa
nome = str(input('Diga-me seu nome:')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
