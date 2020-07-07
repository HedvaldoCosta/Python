#19-Sorteando um aluno
import random
alu1 = str(input("Nome do primeiro aluno:"))
alu2 = str(input("Nome do segundo aluno:"))
alu3 = str(input("Nome do terceiro aluno:"))
alu4 = str(input("Nome do quarto aluno:"))
aleat = [alu1, alu2, alu3, alu4]
print(f"O aluno escolhido foi: {random.choice(aleat)}")
