temp_po = 0
temp_ne = 0
menor_temp = 999.0

for i in range(6):
    temperatura = float(input("Digite uma temperatura em Celcius: "))
    if (temperatura >= 0):
        temp_po = temp_po + 1
    else:
        temp_ne = temp_ne + 1

    if temperatura < menor_temp:
        menor_temp = temperatura

print(f"Tiveram {temp_po} temperaturas positivas, e tiveram {temp_ne} temperaturas negativas")
print(f"A menor temperatura foi a: {menor_temp}.")
