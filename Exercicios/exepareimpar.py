"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = (input("Digite um número: "))

if numero.isdigit():
    numero_int = int(numero)
    par = numero_int % 2 == 0
    
    if par:
        print(f"O número '{numero_int}' é par")

if numero.isdigit():
    numero_int = int(numero)
    impar = numero_int % 2 != 0

    if impar:
        print(f"O número '{numero_int}' é impar")

else:
    print("Isso não é um número inteiro!")



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Qual a hora na sua cidade? ")

if hora.isdigit():
    hora_int = int(hora)
    dia = (hora_int >= 0) and (hora_int <= 11)

    if dia:
        print("Bom dia!")

if hora.isdigit():
    hora_int = int(hora)
    tarde = (hora_int >= 12) and (hora_int <= 17)
    
    if tarde:
        print("Boa tarde!")

if hora.isdigit():
    hora_int = int(hora)
    noite = (hora_int >= 18) and (hora_int <= 23)
    
    if noite:
        print("Boa Noite!")

else:
    print(f"'{hora}' Não é um horário!")



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu primeiro nome: ")
contagem = len(nome)
menor = contagem <= 4
normal = contagem >= 5 and contagem <= 6

if menor:
    print("Seu nome é curto!")

elif normal:
    print("Seu nome é normal!")

else:
    print("Seu nome é muito GRANDE!")