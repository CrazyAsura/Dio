class Passaro:
    def voar(self):
        print("voando...")
        
class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")
        
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")
        
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando")

def plano_voo(obj):
    obj.voar()
    
plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())