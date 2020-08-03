# Uma academia deseja fazer um senso entre seus clientes para descobrir
# o mais alto, o mais baixo, a mais gordo e o mais magro,
# para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
# sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores
# do cliente mais alto, do mais baixo, do mais gordo e do mais magro,
# além da média das alturas e dos pesos dos clientes
c = menor = maior = magro = pesado = mediaA = mediaP = 0
nome = ''
nomeM = ''
nomem = ''
nomep = ''
nomeP = ''
while True:
    codigo = int(input('Digite seu codigo numerico[ 0 para sair ]: '))
    if codigo == 0:
        break
    altura = float(input('Sua altura: '))
    peso = float(input('Seu peso: '))
    c = c + 1
    mediaP = mediaP + peso
    mediaA = mediaA + altura
    if c == 1:
        nome = codigo
        nomeM = codigo
        nomem = codigo
        nomep = codigo
        nomeP = codigo
        maior = altura
        menor = altura
        magro = peso
        pesado = peso
    else:
        if maior < altura:
            nomeM = codigo
            maior = altura
        if menor > altura:
            nomem = codigo
            menor = altura
        if magro > peso:
            nomep = codigo
            magro = peso
        if pesado < peso:
            nomeP = codigo
            pesado = peso
print(f'A pessoa mais alta é código {nomeM} com  {maior}m')
print(f'A pessoa mais baixa é código {nomem} com {menor}m')
print(f'A pessoa mais magra é código {nomep} com {magro}kg')
print(f'A pessoa mais pesada é código {nomeP} com {pesado}kg')
print(f'Peso Medio: {mediaP/ c:.2f}kg')
print(f'Altura Media: {mediaA/ c:.2f}m')