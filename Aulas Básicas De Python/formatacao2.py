a = "Carlos"
b = "Maik"
c = "Carlos"
d = 1.1

#formato = "a={} b={} c={} d={:.2f}".format(a, b, c, d)
formato = "a={0} b={2} c={1} d={3:.2f}".format(a, b, c, d)
#para não depender da ordem. Exp: (a(primeiro), b(segundo), c(terceiro))
#parametro nomeado = é quando dou nome nas coisas dentro da chamada das funções
formato2 = "a={nome2} b={nome2} c={nome3} d={numero:.2f}".format(
    nome1=a, nome2=b, nome3=c, numero=d
    )

print(formato)
print(formato2)

