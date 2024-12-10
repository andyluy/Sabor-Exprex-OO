from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    """
    Representa um prato no cardápio.
    Herda da classe ItemCardapio e adiciona uma descrição detalhada do prato.
    """
    def __init__(self,nome,preco,descricao):
        """
        Construtor da classe Prato.

        Args:
            nome (str): Nome do prato.
            preco (float): Preço do prato.
            descricao (str): Descrição detalhada do prato.
        """
        super().__init__(nome,preco)
        self.descricao = descricao
    
    def __str__(self):
        """
        Retorna uma representação em string do prato.
        Por padrão, retorna apenas o nome do prato.
        """
        return self._nome
    
    def aplicar_desconto(self):
        """
        Aplica um desconto de 5% no preço do prato.
        """
        self._preco -=(self._preco * 0.05)