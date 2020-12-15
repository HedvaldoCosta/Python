from Ex115.Lib.interface import cabeçalho


def ArquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado')


def LerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('ERRO AO LER O ARQUIVO')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(arquivo.read())
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', ' ')
            print(f'{dado[0]:<25}{dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Houve um erro')
    else:
        try:
            arquivo.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro')
        else:
            print(f'Registro de {nome} adicionado')
            arquivo.close()