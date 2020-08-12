#29-Ver a velocidade de um carro e multa-lo se passar o limite de velocidade
velocidade = float(input('Está dirigindo a quantos km/h? '))
vel = velocidade - 80
if velocidade > 80:
    print(f'Terá que pagar um valor de: {vel * 7} reais')
else:
    print('Boa viagem')

