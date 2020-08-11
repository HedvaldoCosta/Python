#20-Ordem de escolha dos alunos
import random
n1 = str(input("Nome do primeiro aluno:"))
n2 = str(input("Nome do segundo aluno:"))
n3 = str(input("Nome do terceiro aluno:"))
n4 = str(input("Nome do quarto aluno:"))
ordem = [n1, n2, n3, n4]
random.shuffle(ordem)
print(f"Ordem dos alunos:")
print(ordem)
