from carro import Carro
from moto import Moto

carro1 = Carro("Toyota", "Corolla", 4, cor="roxo")
carro2 = Carro("Honda", "Civic", 2, cor="sunset")
carro3 = Carro("Ford", "Fusion", 4, cor="azul")

moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
moto2 = Moto("Honda", "CB 500", "Casual")
moto3 = Moto("Yamaha", "MT-09", "Esportiva")

print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)

carro4 = Carro(marca="Ford", modelo="Focus", cor="Preto")
carro5 = Carro(marca="Chevrolet", modelo="Cruze", cor="Prata")
carro6 = Carro(marca="Honda", modelo="Civic", cor="Vermelho")

print(f"Carro 4: {carro4.marca} {carro4.modelo}, Cor: {carro4.cor}")
print(f"Carro 5: {carro5.marca} {carro5.modelo}, Cor: {carro5.cor}")
print(f"Carro 6: {carro6.marca} {carro6.modelo}, Cor: {carro6.cor}")