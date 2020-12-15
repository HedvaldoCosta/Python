from urllib import request

try:
    site = request.urlopen('http://pudim.com.br')
except:
    print('Site não acessivel')
else:
    print('Site acessivel')
