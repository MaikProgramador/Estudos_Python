nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")
    
    if " " in nome:
        print("Seu nome tem espaço")
    else:
        print("Seu nome NÂO contem espaço")
    print(f"Seu nome tem {len(nome)} Letras")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A última letra do seu nome é: {nome[-1]}")

else:
    print("Desculpe, você nçao digitou nada!")