from veiculo import Veiculo

class Carro (Veiculo):
    def __init__ (self, marca, modelo, quantidade_portas, cor):
        super().__init__ (marca, modelo)
        self.quantidade_portas = quantidade_portas
        self.cor = cor

    # def __str__ (self):
    #     status = 'ligado' if self._ligado else 'desligado'
    #     return f'{self._marca} {self._modelo} - Portas: {self.quantidade_portas} - Status {status}'
    
    def ligar(self):
        print(f'O carro {self.modelo} está ligado.')