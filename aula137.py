# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

# minha implementação
class Carro:
    def __init__(self, nome):
        self.nome = nome

    @property
    def motor(self):
        if not hasattr(self, '_motor'):
            return 'motor não cadastrado'
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

    @property
    def fabricante(self):
        if not hasattr(self, '_fabricante'):
            return 'fabricante não cadastrado'
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

volkswagen = Fabricante('Volkswagen')
motor_volkswagen = Motor('Motor Volkswagen')
motor = Motor('motor1')
fusca = Carro('Fusca')
gol = Carro('Gol')

chevrolet = Fabricante('Chevrolet')
motor_chevrolet = Motor('Motor Chevrolet')
corsa = Carro('Corsa')
celta = Carro('Celta')

corsa.motor = motor_chevrolet
corsa.fabricante = chevrolet

celta.motor = motor_chevrolet
celta.fabricante = chevrolet

fusca.motor = motor_volkswagen
fusca.fabricante = volkswagen

gol.motor = motor_volkswagen
gol.fabricante = volkswagen

print(corsa.nome)
print(corsa.motor.nome)
print(corsa.fabricante.nome)
print()

print(celta.nome)
print(celta.motor.nome)
print(celta.fabricante.nome)
print()

print(fusca.nome)
print(fusca.motor.nome)
print(fusca.fabricante.nome)
print()

print(gol.nome)
print(gol.motor.nome)
print(gol.fabricante.nome)
print()