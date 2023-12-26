class cola ():
    """
    Clase cola, contiene las funciones:
    1. es_vacio(): verifica si la cola está vacía
    2. agregar(dato): agrega un dato a la cola
    3. eliminar(dato): elimina un dato de la cola
    4. extraer(dato): extrae una lista de elementos de la cola
    5. buscar(dato): busca un dato en la cola
    """
    def __init__ (self, lista = []):
        self.lista = lista

    def es_vacio (self):
        if self.lista == []:
            print ("La cola está vacía")
            return True
        else:
            print (f"La cola contiene los siguientes elementos: {self.lista}")
            return False

    def agregar (self, dato):
        self.lista.append (dato)
        print ("Dato agregado")
        print (self.lista)
        return self.lista

    def eliminar (self, dato):
        self.lista.remove (dato)
        print ("Dato eliminado")
        print (self.lista)
        return self.lista

    def extraer (self, dato):
        try:
            self.lista = self.lista[:self.lista.index(dato)]
            print ("Lista extraida")
            print (self.lista)
            return self.lista
        except:
            print ("Dato no encontrado en la cola")
            return False

    def buscar (self, dato):
        try:
            print (f"El dato {dato} se encuentra en la posición {self.lista.index(dato)} de la cola")
            return self.lista.index(dato)
        except:
            print ("Dato no encontrado en la cola")
            return False

    def _top(self):
        return self.lista[-1]
    
    def _contiene(self, dato):
        return dato in self.lista