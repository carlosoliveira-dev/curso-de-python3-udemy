# Problema do diamante
# Comente os métodos para ver de qual classe ele vai ser chamado
class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    def quem_sou(self):
        print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')


# A ordem da herança importa
# nesse caso tem uma grande chance do método ser
# procurado primeiro em B caso não exista em D, depois em C
class D(B, C):
    ...

    def quem_sou(self):
        print('D')


d = D()
d.quem_sou()

# mostra a ordem de resolução baseada nas heranças múltiplas
# print(D.__mro__)
print(D.mro())