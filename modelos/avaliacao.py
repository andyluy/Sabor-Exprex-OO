class Avaliacao:
    """
    Representa uma avaliação realizada por um cliente.

    Attributes:
        _cliente (str): Nome ou identificador do cliente que realizou a avaliação.
        _nota (int): Nota atribuída pelo cliente, em uma escala definida.
    """
    def __init__(self, cliente, nota):
        """
        Construtor da classe Avaliação.

        Args:
            cliente (str): Nome ou identificador do cliente.
            nota (int): Nota atribuída pelo cliente.
        """
        self._cliente = cliente
        self._nota = nota