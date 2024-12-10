from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    """
    Representa uma bebida no cardápio.
    Herda da classe ItemCardapio e adiciona o atributo tamanho.
    """
    def __init__(self, nome, preco, tamanho):
        """
        Construtor da classe Bebida.

        Args:
            nome (str): Nome da bebida.
            preco (float): Preço da bebida.
            tamanho (str): Tamanho da bebida (e.g., pequeno, médio, grande).
        """
        super().__init__(nome, preco)
        self.tamanho = tamanho
        
    def __str__(self):
        """
        Retorna uma representação em string da bebida.
        Por padrão, retorna apenas o nome da bebida.
        """
        return self._nome
    
    def aplicar_desconto(self):
        """
        Aplica um desconto de 8% no preço da bebida.
        """
        self._preco -=(self._preco * 0.08)