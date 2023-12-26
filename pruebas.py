import modulos.pila
import modulos.cola

while True:
    print('En caso quiera validar las funciones de la pila, ingrese (P). En caso quiera validar las funciones de la cola, ingrese (C).')
    opcion = input('Ingrese (P) o (C): ')
    if (opcion == 'P' or opcion == 'p') or (opcion == 'C' or opcion == 'c'):
        break
    else:
        print('El valor ingresado corresponde a ninguna opción válida. Intente nuevamente.')

# Prueba de Pilas
def prueba_pila ():
    P = [3, 5, 6, 9]
    pila = modulos.pila.pila (P)

    pila.es_vacio ()
    pila.agregar (7)
    pila.eliminar (7)
    pila.extraer (6)
    pila.buscar (9)

    P = [1, 3, 5, 6, 9, 17]

    pila = modulos.pila.pila (P)

    pila.es_vacio ()
    pila.agregar (7)
    pila.eliminar (7)
    pila.extraer (5)
    pila.buscar (17)

# Prueba de Colas
def prueba_cola ():
    C = [3, 5, 6, 9]

    cola = modulos.cola.cola (C)

    cola.es_vacio ()
    cola.agregar (7)
    cola.eliminar (7)
    cola.extraer (6)
    cola.buscar (9)

    C = [1, 3, 5, 6, 9, 17]

    cola = modulos.cola.cola (C)

    cola.es_vacio ()
    cola.agregar (7)
    cola.eliminar (7)
    cola.extraer (5)
    cola.buscar (17)


if opcion == 'P' or opcion == 'p':
    print('Prueba de Pilas')
    prueba_pila ()

if opcion == 'C' or opcion == 'c':
    print('Prueba de Colas')
    prueba_cola ()