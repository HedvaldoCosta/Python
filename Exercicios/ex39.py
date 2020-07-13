#Alistamento
from datetime import date
idade = int(input('Ano de nascimento:'))
ano = date.today().year
alis = ano - idade
pas = alis - 18
che = 18 - alis

if alis == 18:
    print('Esta na hora de se alistar')
elif alis > 18:
    print(f'Ja passou {pas} anos para se alistar')
elif alis < 18:
    print(f'Ainda falta {che} anos para se alistar')