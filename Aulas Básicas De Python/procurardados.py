lista = "abcdefghi"
procurar = input("Digite oque procura: ")

if procurar in lista:
    print(f"'{procurar}' está na lista")
else:
    print(f"'{procurar}' não está na lista")