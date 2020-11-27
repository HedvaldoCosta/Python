def voto(x=0):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - x
    if idade < 16:
        print(f'Com {idade} anos: voto negado')
    elif (idade >= 16) and (idade <= 17) or (idade >=70):
        print(f'Com {idade} anos: Voto opcional')
    elif (idade >= 18) and (idade < 70):
        print(f'Com {idade} anos: Voto obrigatorio')


#programa principal
ano = int(input('Me diga o ano do seu nascimento: '))
voto(ano)