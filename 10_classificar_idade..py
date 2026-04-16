ano = int(input("Em que ano o atleta nasceu? "))
idade = 2026 - ano

if(idade <= 9):
    print("É um atleta Mirim!")

elif(idade <= 14):
    print("É um atleta Infantil!")

elif(idade <= 19):
    print("É um atleta Junior!")

elif(idade <= 25):
    print("É um atleta Sênior!")

else:
    print("É um atleta Master!")


