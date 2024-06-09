#.clear()
contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},

"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},

"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, 

"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

}
print(contatos)

contatos.clear()
print(contatos)

#.copy()
contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},

"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},

"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, 

"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

}

copy = contatos.copy()
copy["guilherme@gmail.com"] = {"nome": "gui"}
print(contatos)
print(copy)

#.fromkeys()
dic = dict.fromkeys(["nome" , "telefone"])
print(dic)
dic = dict.fromkeys(["nome" , "telefone"], "vazio")
print(dic)

#.get()
contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

}

#contatos["chave"] # KeyError

contatos.get("chave") # None

contatos.get("chave", {}) # {}

contatos.get("guilherme@gmail.com", {}) # {"guilherme@gmail.com": {"nome":

#"Guri-therme", "telefone": "3333-2221

#.items()
for chave, valor in contatos.items():
    print(chave, valor)

#.keys()
contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

}

print(contatos.keys())

#.pop()
contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

}

print(contatos.pop("guilherme@gmail.com"))
print(contatos.pop("guilherme@gmail.com", {}))

#.popitem()
contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

}

#print(contatos.popitem("guilherme@gmail.com"))

#.setdefault()
contatos =  {"nome": "Guilherme", "telefone": "3333-2221"}
print(contatos)

print(contatos.setdefault("nome", "Giovanna"))
print(contatos.setdefault("idade", 28))

#.update()
contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}

}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})

contatos # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})

contatos # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com':

{'nome': 'Giovanna', 'telefone': '3322-8181'}

#.values()
contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},

"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},

"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, 

"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

}

print(contatos)

print(contatos.values())

#in
contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},

"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},

"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, 

"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

}

print(contatos)
print("guilherme@gmail.com" in contatos)
#print("megui@gmail.com" in contatos)
print("idade" in contatos["guilherme@gmail.com"])
print("telefone" in contatos["giovanna@gmail.com"])

#del
contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},

"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},

"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, 

"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

}

print(contatos)
del contatos["giovanna@gmail.com"]["telefone"]
print(contatos)
del contatos["chappie@gmail.com"]
print(contatos)