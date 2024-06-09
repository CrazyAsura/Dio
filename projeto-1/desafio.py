menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite= 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        
        print("Depósito\n")
        
        valor = float(input("Informe o valor a ser depositado: R$ "))
        
        if valor > 0:
            saldo += valor
            extrato += (f"Foi realizada a operação de depósito de R$ {saldo}\n")
            
    elif opcao == "s":
        print("Saque")
        
        if LIMITE_SAQUES > 0 and LIMITE_SAQUES <= 3 and saldo > 0:
            
            valor = float(input("Quanto deseja sacar,lembre-se que o limite diário de saque são 3 vezes: R$ "))
            saldo -= valor
            
            if saldo <= 0:
                print("Você não possui saldo suficiente para realizar o saque.")
                saldo = 0
                
            else:
                LIMITE_SAQUES -= 1
                extrato += (f"Foi realizada a operação de Saque de R$ {valor}\n")
                
        elif LIMITE_SAQUES <= 0:
            print("Você atingiu o limite de saque diário, por favor tente novamente mais tarde.")
            
        else:
            print("Você não possui saldo suficiente para realizar o saque.")
            
    elif opcao == "e":
        print("Extrato")
        print("############################################################## Menu ##############################################################\n")
        print(f"Os resultados das operações realizadas nessa conta foram: \n{extrato} \n")
        print(f"Saldo: RS {saldo}\n")
        print("##################################################################################################################################\n")
            
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")