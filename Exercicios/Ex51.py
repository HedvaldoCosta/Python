# Progressão Aritmetica
termo = float(input("Primeiro termo: "))
razão = float(input("Razão:"))
for c in range(2, 11):
    termo = termo + razão
    print(f"{c}º termo: {termo}")
