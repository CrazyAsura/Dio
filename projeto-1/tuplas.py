frutas = ("laranja", "maçã", "uva",)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1,2,3,4])
print(numeros)

pais = ("Brasil",)
print(pais)

frutas = ("laranja", "maçã", "uva",)
print(frutas[0])
print(frutas[2])

frutas = ("laranja", "maçã", "uva",)
print(frutas[-1])
print(frutas[-3])

#count
cores = ("vermelho", "blue", "green", "blue")

print(cores)

print(cores.count("vermelho"))
print(cores.count("blue"))
print(cores.count("green"))

#index
linguagens = ('python', 'js', 'c', 'java', 'csharp')

print(linguagens)

print(linguagens.index("java"))
print(linguagens.index("python"))

#len
linguagens = ('python', 'js', 'c', 'java', 'csharp')
print(len(linguagens))