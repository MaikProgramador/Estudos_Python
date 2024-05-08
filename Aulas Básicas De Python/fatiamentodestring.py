variavel = "Ola mundo"
#ele vai até a ultima str indicada = [2:7] = r até o m = rlosM
# print(variavel[2:7])
# print(variavel[1:])
# print(variavel[-8:-2])
#[0:3:2] - 0 = Inicio | 3 = informa até onde vai | 
#2 = é quantas casas eu quero pular = "Paço"

contagem = input("Informe a frase que vc quer contar: ")
print(f"A sua frase tem {len(contagem[0:3:2])} caracteres")
print(f"frase invertida {contagem[::-1]}")
print(f"frase invertida {contagem[-1:-10:-1]}") #Tudo negativo para funcionar
