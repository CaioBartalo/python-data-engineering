print("Me fale o comprimento de 3 lados para saber se podemos fazer um triângulo!")

A = float(input("Primeiro Lado: "))
B = float(input("Segundo Lado: "))
C = float(input("Terceiro Lado: "))

if (B < A + C) and (A < B + C) and (C < B + A):
    print(f"A soma de {A:.0f}, {B:.0f} e {C:.0f}, formam um triângulo!")

else:
    print(f"A soma de {A:.0f}, {B:.0f} e {C:.0f}, NÃO formam um triângulo!")
