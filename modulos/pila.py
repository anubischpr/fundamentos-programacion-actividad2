class pila ():
    """
    Clase pila, contiene las funciones:
    1. es_vacio(): verifica si la pila está vacía
    2. agregar(dato): agrega un dato a la pila
    3. eliminar(dato): elimina un dato de la pila
    4. extraer(dato): extrae una lista de elementos de la pila
    5. buscar(dato): busca un dato en la pila
    """
    def __init__ (self, lista = []):
        self.lista = lista

    def es_vacio (self):
        if self.lista == []:
            print ("La pila está vacía")
            return True
        else:
            print (f"La pila contiene los siguientes elementos: {self.lista}")
            return False

    def agregar (self, dato):
        self.lista.append (dato)
        print ("Dato agregado")
        print (self.lista)
        return dato in self.lista

    def eliminar (self, dato): #eliminar el dato
        self.lista.remove (dato)
        print ("Dato eliminado")
        print (self.lista)
        return dato in self.lista

    def extraer (self, dato):
        try:
            self.lista = self.lista[self.lista.index(dato)+1:]
            print ("Lista extraida")
            print (self.lista)
            return self.lista
        except:
            print ("Dato no encontrado en la pila")
            return False

    def buscar (self, dato):
        try:
            print (f"El dato {dato} se encuentra en la posición {self.lista.index(dato)} de la pila")
            return self.lista.index(dato)
        except:
            print ("Dato no encontrado en la pila")
            return False

    def _top(self):
        return self.lista[-1]
    
    def _contiene(self, dato):
        return dato in self.lista