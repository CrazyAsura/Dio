#append()
lista = []

lista.append(1)
lista.append("python")
lista.append([40,30,20])

print(lista)

#clear()
lista = [1, 'python', [40, 30, 20]]
print(lista)

lista.clear()
print(lista)

#.copy()
lista = [1, 'python', [40, 30, 20]]
l2 = lista.copy()

print(lista)

print( id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)

#.count
cores = ["vermelho", "blue", "green", "blue"]

print(cores)

print(cores.count("vermelho"))
print(cores.count("blue"))
print(cores.count("green"))

#.extend()
linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens)

#.index
linguagens = ['python', 'js', 'c', 'java', 'csharp']

print(linguagens)

print(linguagens.index("java"))
print(linguagens.index("python"))

#.pop
linguagens = ['python', 'js', 'c', 'java', 'csharp']

print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))

#.remove
linguagens = ['python', 'js', 'c', 'java', 'csharp']

linguagens.remove("c")

print(linguagens)

#reverse
linguagens = ['python', 'js', 'c', 'java', 'csharp']

linguagens.reverse()

print(linguagens)

#.sort()
linguagens = ['python', 'js', 'c', 'java', 'csharp']

print(linguagens.sort())

linguagens = ['python', 'js', 'c', 'java', 'csharp']

print(linguagens.sort(reverse=True))

linguagens = ['python', 'js', 'c', 'java', 'csharp']

print(linguagens.sort(key=lambda x: len(x)))

linguagens = ['python', 'js', 'c', 'java', 'csharp']

print(linguagens.sort(key=lambda x: len(x), reverse=True))



#len
linguagens = ['python', 'js', 'c', 'java', 'csharp']

print(len(linguagens))

#.sort()
linguagens = ['python', 'js', 'c', 'java', 'csharp']

print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
