from Ex115.Lib.interface import *
from Ex115.Lib.Arquivo import *

arquivo = 'programa.txt'
if not ArquivoExiste(arquivo):
    CriarArquivo(arquivo)
while True:
    resposta = menu(['[listar usuarios]', '[Adicionar usuario]', '[Sair]'])
    if resposta == 1:
        LerArquivo(arquivo)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        print('\033[31mPrograma finalizado\033[m')
        break
    else:
        print('\033[31mERRO! POR FAVOR, COLOQUE UM VALOR VALIDO\033[m')
