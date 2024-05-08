nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

if nome and idade:
    print(f"Seu nome é: {nome}")
    print(f"{nome} tem {idade} anos de idade")
    print(f"Seu nome invertido é: {nome[::-1]}")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")
    if " " in nome:
        print("Seu nome tem espaço")
    else:
        print("Seu nome não contém espaço")
else:
    print("Você não digitou nada!")