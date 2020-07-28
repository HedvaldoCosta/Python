# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações
while True:
    nome = str(input('Nome: '))
    senha = input('Senha: ')
    if nome == senha:
        print('Invalido')
    else:
        print('Acesso permitido')
        break