class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Ligando motor")
        
    def __str__(self) -> str:
        return self.cor
    
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas,carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"}")

moto = Motocicleta("preta","ABC-1234", 2 )
carro = Carro("branco","xde-0098" , 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)
caminhao.esta_carregado()