from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    """
    Representa uma sobremesa no cardápio.
    Herda da classe ItemCardapio e adiciona atributos específicos para sobremesas.
    """
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        """
        Construtor da classe Sobremesa.

        Args:
            nome (str): Nome da sobremesa.
            preco (float): Preço da sobremesa.
            descricao (str): Descrição da sobremesa.
            tipo (str): Tipo da sobremesa (e.g., gelada, quente).
            tamanho (str): Tamanho da sobremesa (e.g., individual, familiar).
        """
        super().__init__(nome, preco)
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho

    def __str__(self):
        """
        Retorna uma representação em string do objeto Sobremesa.
        Por padrão, retorna apenas o nome da sobremesa.
        """
        return self._nome

    def aplicar_desconto(self):
        """
        Aplica um desconto de 15% no preço da sobremesa.
        """
        self._preco -= (self._preco * 0.15)