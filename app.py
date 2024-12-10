from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# Cria um novo restaurante com o nome "praça" e tipo "Gourmet"
restaurante_praca = Restaurante('praça', 'Gourmet')
# Cria uma nova bebida: Suco de Melancia, com preço de R$ 5,00 e tamanho grande
bebida_suco = Bebida ('Suco de Melancia', 5.0, 'grande')
# Aplica um desconto (o método aplicar_desconto deve estar implementado na classe Bebida)
bebida_suco.aplicar_desconto()
# Cria um novo prato: Pãozinho, com preço de R$ 2,00 e descrição
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
# Aplica um desconto (o método aplicar_desconto deve estar implementado na classe Prato)
prato_paozinho.aplicar_desconto()
# Adiciona a bebida e o prato ao cardápio do restaurante
restaurante_praca.adcionar_no_cardapio(bebida_suco)
restaurante_praca.adcionar_no_cardapio(prato_paozinho)


def main():
    """
    Função principal do programa.
    Exibe o cardápio do restaurante "praça".
    """
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()