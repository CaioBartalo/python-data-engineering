for i in range(5):
    salario = float(input("Qual o seu salário? R$"))
    if (salario < 2000):
        novo_salario =  salario * 15 / 100 + salario
        print(f"Seu salário antigo era de R${salario:.2f}! e o atual é de R${novo_salario:.2f}!")
    else:
        novo_salario =  salario * 10 / 100 + salario
        print(f"Seu salário antigo era de R${salario:.2f}! e o atual é de R${novo_salario:.2f}!")


