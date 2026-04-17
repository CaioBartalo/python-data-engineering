nota_media = 0

for i in range(1,5,1):
    nota = float(input("Qual foi a sua nota? "))
    if (nota >= 7):
        print("Você foi aprovado!")
    else:
        print("Você foi reprovado!")
    nota_media = nota_media + nota

media = nota_media / 4
print(f"A média da turma é:{media}")
