# ACADEMIA DE IDIOMAS
# Impide retirar elementos de una cola vacia

class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)

        # TODO 1: agregar al final
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agregar a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: retirar el ultimo elemento
        if len(self.items) == 0:
            print("La pila esta vacia.")
            return None
        return self.items.pop()


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agregar al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: controlar cola vacia
        if len(self.items) == 0:
            print("Error: la cola esta vacia.")
            print("No se puede retirar ninguna solicitud.")
            return None
        return self.items.pop(0)


# PRUEBAS DEL PROGRAMA

print("================================")
print("       ACADEMIA DE IDIOMAS")
print("================================")

# Lista enlazada
lista = ListaEnlazada()
lista.agregar("A01", "Ingles")
lista.agregar("A02", "Frances")
lista.agregar("A03", "Aleman")

print("\nLISTA DE IDIOMAS:")
lista.mostrar()

# Pila
pila = Pila()
pila.apilar("A01: Ingles")
pila.apilar("A02: Frances")
pila.apilar("A03: Aleman")

print("\nPILA:")
print("Elemento retirado:", pila.desapilar())

# Cola
cola = Cola()
cola.encolar("A01: Ingles")
cola.encolar("A02: Frances")
cola.encolar("A03: Aleman")

print("\nSOLICITUDES DE LA COLA:")
print("Atendida:", cola.desencolar())
print("Atendida:", cola.desencolar())
print("Atendida:", cola.desencolar())

# Prueba de cola vacia
print("\nPRUEBA DE COLA VACIA:")
cola.desencolar()

print("\nPrograma finalizado correctamente.")
