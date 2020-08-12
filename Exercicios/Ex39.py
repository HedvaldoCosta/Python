#39-Alistamento
from datetime import date
idade = int(input('Ano de nascimento:'))
sexo = str(input('Genero(M/F):')).upper()
ano = date.today().year
alis = ano - idade
pas = alis - 18
che = 18 - alis

if sexo == 'M' and alis == 18:
    print('Esta na hora de se alistar')
elif sexo == 'M' and alis > 18:
    print(f'Ja passou {pas} anos para se alistar')
elif sexo == 'M' and alis < 18:
    print(f'Ainda falta {che} anos para se alistar')
elif sexo =='F':
    print('Não precisa fazer o alistamento')
