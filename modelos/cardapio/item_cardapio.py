from abc import ABC, abstractmethod
 
class ItemCardapio(ABC):
    """
    Classe abstrata que representa um item de cardápio.
    Serve como base para outras classes de itens específicos (e.g., Bebida, Prato, Sobremesa).
    """
    def __init__(self,nome,preco):
        """
        Construtor da classe ItemCardapio.

        Args:
            nome (str): Nome do item.
            preco (float): Preço do item.
        """
        self._nome = nome
        self._preco = preco
    
    @abstractmethod
    def aplicar_desconto(self):
        """
        Método abstrato para aplicar um desconto ao item.
        Deve ser implementado pelas classes filhas.
        """
        pass