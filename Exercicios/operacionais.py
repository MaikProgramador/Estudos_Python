valor_1 = int(input("Digite um valor: "))
valor_2 = int(input("Digite outro valor: "))

if valor_1 > valor_2:
    print(f"{valor_1} é maior que {valor_2}")
    print("Obrigado!")
elif valor_1 < valor_2:
    print(f"{valor_2} é maior que {valor_1}")
elif valor_1 == valor_2:
    print(f"{valor_1} é igual a {valor_2}")
else:
    print("Vc não digitou um valor")