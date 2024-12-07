class Veiculo:
    def __init__ (self, marca, modelo):
        self._ligado = False
        self._marca = marca
        self._modelo = modelo
    def __str__(self):
        status = 'ligado' if self._ligado else 'desligado'
        return f'{self._marca} {self._modelo} - Status: {status}'