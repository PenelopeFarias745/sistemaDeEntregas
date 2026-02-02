from abc import ABC, abstractmethod

class Entrega(ABC):
    @abstractmethod
    def calcular_prazo(self):
        pass

    @abstractmethod
    def calcular_preco(self):
        pass

class EntregaMotoboy(Entrega):
    def calcular_prazo(self):
        return "2 dias"
    
    def calcular_preco(self):
        return 15
    
class EntregaDrone(Entrega):
    def calcular_prazo(self):
        return "1 dia"
    
    def calcular_preco(self):
        return 30
    
class EntregaCorreios(Entrega):
    def calcular_prazo(self):
        return "5 dias"
    
    def calcular_preco(self):
        return 20
    
tipo_entrega = {
    "m": EntregaMotoboy(),
    "d": EntregaDrone(),
    "c": EntregaCorreios()
}


while True:
    opcao = input(("""Seja bem-vindo(a) ao nosso Sistema de Entregas! Escolha uma das opções a seguir:
        m) Motoboy
        d) Drone
        c) Correios
        s) Sair """))

    if opcao == "s":
        break 
    
    if opcao in tipo_entrega:
        entrega = tipo_entrega[opcao]

        calcular = input("""Escolha uma das opções abaixo:
            1) Calcular prazo
            2) Calcular frete
            3) Trocar forma de entrega/sair """)
            
        if calcular == "1":
            print(f"Entregue em até {entrega.calcular_prazo()}")
        elif calcular == "2":
            print(f"R${entrega.calcular_preco()}")
        else:
            print("Escolha uma opção válida.")

    else:
        print("Escolha uma opção válida.")


        
