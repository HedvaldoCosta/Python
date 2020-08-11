#22- Modificando String
nome = str(input("Qual é o seu nome? ")).strip()
print(f"Nome em maiusculas:{nome.upper()}")
print(f"Nome em minusculas:{nome.lower()}")
print(f"Letras ao todo:{len(nome) - nome.count(' ')}")
print(f"Seu primeiro nome tem {nome.find(' ')} letras")
