nome_funcionario = input("Qual é o seu nome? ")
cargo_funcionario = input("Qual é o seu cargo? ")
salario_atual_funcionario = float(input("Qual é o seu salário atual? R$"))
aumento_porcentagem = float(input("Qual porcentagem do aumento? "))
valor_porcentagem = salario_atual_funcionario * aumento_porcentagem / 100
salario_final = valor_porcentagem + salario_atual_funcionario
print(f"O funcionario {nome_funcionario}, {cargo_funcionario} da nossa empresa, recebeu um aumento de R${valor_porcentagem}, e seu salário atual é R${salario_final}")
''
