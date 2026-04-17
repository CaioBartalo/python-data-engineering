numero_maior = 0
numero_menor = 0
lista_de_numeros = []  # 1. Criamos a estante vazia antes de tudo

for i in range(5):
    numeros = float(input(f"Digite o {i + 1}º numero: "))

    lista_de_numeros.append(numeros) # 2. O comando mágico: guarda o número na próxima gaveta disponível

    if (numeros > 10):
        numero_maior = numeros + numero_maior
    else:
        numero_menor = numero_menor + 1

print(f"Soma dos maiores que 10: {numero_maior:.2f}")
print(f"Quantidade de menores ou iguais a 10: {numero_menor:.2f}")

# 3. Agora podemos ver todos os números que foram digitados!
print(f"Lista completa de dados salvos: {lista_de_numeros}")
