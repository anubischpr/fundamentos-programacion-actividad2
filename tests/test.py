import unittest
import modulos.pila as p
import modulos.cola as c

class TestPila(unittest.TestCase):

    def test_es_vacio(self):
        pila = p.pila([])
        self.assertTrue(pila.es_vacio())
        pila = p.pila([3, 5, 6, 9])
        self.assertFalse(pila.es_vacio())

    def test_agregar(self):
        pila = p.pila([])
        pila.agregar(1)
        self.assertEqual(pila._top(), 1)  # Asumiendo que hay una función _top() que devuelve el último elemento
        pila = p.pila([3, 5, 6, 9])
        pila.agregar(7)
        self.assertEqual(pila._top(), 7)

    def test_eliminar(self):
        pila = p.pila([1, 2, 3])
        pila.eliminar(2)
        self.assertFalse(pila._contiene(2))

    def test_extraer(self):
        pila = p.pila([3, 5, 6, 9])
        extraido = pila.extraer(6)
        self.assertEqual(extraido, [9])
        self.assertFalse(pila._contiene(6))
        pila = p.pila([1, 3, 5, 6, 9, 17])
        extraido = pila.extraer(5)
        self.assertEqual(extraido, [6, 9, 17])
        self.assertFalse(pila._contiene(5))

    def test_buscar(self):
        pila = p.pila([3, 5, 6, 9])
        indice = pila.buscar(9)
        self.assertEqual(indice, 3)  # Asumiendo que la búsqueda devuelve el índice del elemento
        pila = p.pila([3, 5, 6, 9])
        self.assertFalse(pila.buscar(10))  # Asumiendo que la búsqueda devuelve False si no encuentra el elemento

class TestCola(unittest.TestCase):

    def test_es_vacio(self):
        cola = c.cola([])
        self.assertTrue(cola.es_vacio())
        cola = c.cola([3, 5, 6, 9])
        self.assertFalse(cola.es_vacio())

    def test_agregar(self):
        cola = c.cola([])
        cola.agregar(1)
        self.assertEqual(cola._top(), 1)  # Asumiendo que hay una función _top() que devuelve el último elemento
        cola = c.cola([3, 5, 6, 9])
        cola.agregar(7)
        self.assertEqual(cola._top(), 7)

    def test_eliminar(self):
        cola = c.cola([1, 2, 3])
        cola.eliminar(2)
        self.assertFalse(cola._contiene(2))

    def test_extraer(self):
        cola = c.cola([3, 5, 6, 9])
        extraido = cola.extraer(6)
        self.assertEqual(extraido, [3, 5])
        self.assertFalse(cola._contiene(6))
        cola = c.cola([1, 3, 5, 6, 9, 17])
        extraido = cola.extraer(5)
        self.assertEqual(extraido, [1, 3])
        self.assertFalse(cola._contiene(5))

    def test_buscar(self):
        cola = c.cola([3, 5, 6, 9])
        indice = cola.buscar(9)
        self.assertEqual(indice, 3)  # Asumiendo que la búsqueda devuelve el índice del elemento
        cola = c.cola([3, 5, 6, 9])
        self.assertFalse(cola.buscar(10))  # Asumiendo que la búsqueda devuelve False si no encuentra el elemento

if __name__ == '__main__':
    unittest.main()
