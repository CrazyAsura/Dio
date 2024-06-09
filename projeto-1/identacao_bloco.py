def sacar( valor: float ):
        saldo = 500
        if saldo >= valor:
            print("valor sacado!")
            print("Retire o seu dinheiro na boca do caixa.")
        print("Obrigado por ser nosso cliente, tenha um bom dia!")
        
def depositar( valor:float ):
    saldo = 500
    saldo += valor
    print(saldo)
        
sacar( 100 )
depositar( float(input("Digite quanto deseja depositar: ")) )

#def sacar( valor ):
#        saldo = 500
#        if saldo >= valor:
#            print("valor sacado!")