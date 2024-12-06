# 1) Crie uma classe chamada `ContaBancaria` com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False  # Atributo protegido
    @property
    def titular(self):
        return self._titular
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def titular(self):
        return self._titular

# 2) Na classe ContaBancaria, adicione um método especial `__str__` que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    def __str__(self):
        return f"Conta de {self._titular} - Saldo: R${self._saldo}"
    
# 3) Adicione um método de classe chamado `ativar_conta` à classe `ContaBancaria` que define o atributo ativo como `True`. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

# 7) Crie um método de classe para a conta `ClienteBanco`.
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta
    
# Exemplo de uso do método de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1._saldo}")

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)

print(conta1)
print(conta2)

# 5) Crie uma instância da classe e imprima o valor da propriedade titular.
conta4 = ContaBancaria("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.titular}")
