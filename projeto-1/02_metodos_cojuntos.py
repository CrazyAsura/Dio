#.union()
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a)
print(conjunto_b)

print(conjunto_a.union(conjunto_b))

#.intersection()
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a)
print(conjunto_b)

print(conjunto_a.intersection(conjunto_b))

#.difference()
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a)
print(conjunto_b)

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#.symmetric_difference()
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a)
print(conjunto_b)

print(conjunto_a.symmetric_difference(conjunto_b))

#.issubset()
conjunto_a = {1, 2, 3}
conjunto_b = {1, 4, 2, 5, 6, 3}
print(conjunto_a)
print(conjunto_b)

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#.issuperset()
conjunto_a = {1, 2, 3}
conjunto_b = {1, 4, 2, 5, 6, 3}
print(conjunto_a)
print(conjunto_b)

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

#.isdisjoint()
conjunto_a = {1, 2, 3, 4 ,5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}
print(conjunto_a)
print(conjunto_b)

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

#.add()
sorteio = {1, 23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)

#.copy()
sorteio = {1, 23}
print(sorteio)

l2 = sorteio.copy
print(l2, sorteio)

#.clear()
sorteio = {1, 23}
print(sorteio)

sorteio = sorteio.clear()
print(sorteio)

#.discard()
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(sorteio)

numeros.discard(1)
print(numeros)
numeros.discard(45)
print(numeros)


#.pop()
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)

numeros.pop()
print(numeros)
numeros.pop()
print(numeros)

#.remove()
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(sorteio)

numeros.remove(0)
print(numeros)

#len()
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(sorteio)
print(len(numeros))

#in
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(sorteio)
print(1 in numeros)
print(10 in numeros)