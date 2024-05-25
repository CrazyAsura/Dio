# opcao = -1
#
# while opcao != 0:
#     opcao = int(input("Informe um número: "))
#     
#     if opcao == 10:
#         break
#     
#     print(opcao)

    
#while True:
#    numero = int(input("Informe um número: "))
#    
#    if numero == 10:
#        break
#    
#    print(numero)

for numero in range(100):
    if numero == 10:
        break
    
    print(numero)
    
while True:
    if numero == 10:
        break
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        continue
    
    print(numero)
