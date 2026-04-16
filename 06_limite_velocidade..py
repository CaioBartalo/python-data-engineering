velocidade = float(input("Qual a velocidade em Km o carro passou? "))
multa = (velocidade - 80) * 7

if (velocidade > 80):

    print("Você ultrapassou o limite permitido,  de multa!")
    print(f"O valor da multa é de R${multa:.2f}")

else:
    print("Boa Viagem!")

