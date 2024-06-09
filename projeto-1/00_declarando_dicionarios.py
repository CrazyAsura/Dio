pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"
print(pessoa)

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados ["nome"] # "Guilherme"

dados ["idade"] # 28

dados ["telefone"] # "3333-1234"

dados ["nome"] = "Maria"

dados["idade"] = 18

dados ["telefone"] = "9988-1781"

dados #{"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

contatos = {

"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},

"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},

"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"}, 

"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},

}

contatos["giovanna@gmail.com"]["telefone"] # "3443-2121"

for chave in contatos:
    print(chave, contatos[chave])
    
for chave, valor in contatos.items():
    print(chave, valor)