pares = 0
impares = 0

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    resto = num % 2
    if (resto == 0):
        pares = pares + 1
        print(f"A quantidade de números pares até agora são: {pares}")
    else:
        impares = impares + 1
        print(f"A quantidade de números ímpares até agora são: {impares}")

print(f"O resultado da conta foi {impares} numeros impares e {pares} numeros pares ")
