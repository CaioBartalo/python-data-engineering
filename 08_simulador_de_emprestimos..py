valor_casa = float(input("Qual valor da casa que você deseja comprar? R$"))
valor_salario = float(input("Qual valor do seu salário? R$"))
anos_pagar = float(input("Em quantos anos pretende pagar? "))
meses = anos_pagar * 12
prestacao_mensal = valor_casa / meses
porcentagem = valor_salario * 30 / 100

if (prestacao_mensal > porcentagem):
    print("Empréstimo negado!")
    print(f"O valor da prestação é R${prestacao_mensal:.2f}")
else:
    print("Empréstimo aceito!")
    print(f"O valor da prestação é R${prestacao_mensal:.2f}")
