nome = "Maik"
#altura = 1000.75
altura = 1.75
peso = 95
imc = 64 / (altura**2)

linha1 = f"{nome} tem {altura:,.10f} de altura"
linha2 = f"{nome} pesa {peso} kg"
linha3 = f"o imc é {imc:.2f}"

print(linha1)
print(linha2)
print(linha3)

#formatação = 'f-strings'
#"f" serve para adicionar variaveis
#formatação para casas decimais = ":.2f" (duas casas decimais)
#adicionar virgulas em numeros grande = ":,.2f" (100,050.40)