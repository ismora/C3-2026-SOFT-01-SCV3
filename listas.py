# nombre_variable = "dato que almacena la variable"

# nombre_lista = [dato1, dato2, dato3, ..., datoN]

provincias = ["Cartago", "Puntarenas", "alajuela", "Limón", "Guanacaste"]
print("Lista de provincias:", provincias)
print(type(provincias))

# Agregar un dato al final de la lista
provincias.append("Guanacaste")
print("Lista de provincias actualizada:", provincias)

# Eliminar el último elemento de la lista
provincias.pop()
print("Lista de provincias actualizada:", provincias)

"""
[
"Cartago", :        índice 0        |   índice -3 
"Puntarenas", :     índice 1        |   índice -2
"Alajuela":         índice 2        |   índice -1 
]
"""

# Agregar "Heredia" después de Cartago y antes de Puntarenas
provincias.insert(1, "Heredia")
print("Lista de provincias actualizada:", provincias)

# ['Cartago', 'Heredia', 'Puntarenas',              'Alajuela']
#                                    , "San José", 
# Agregar "San José" después de Puntarenas
provincias.insert(3, "San José")                           # ToDo: Posiciones negativas (-2, San José)
print("Lista de provincias actualizada:", provincias)

# Acceder a un elemento particular de la lista
print("Elmento en índice 3:", provincias[3])  # San José
print("Elmento en índice -4:", provincias[-4]) # San José

print("Elmento en índice 5:", provincias[5]) # Limón
print("Elmento en índice -2:", provincias[-2]) # Limón

# Actualizar el dato de una posición
provincias[4] = "Alajuela"
print("Lista de provincias actualizada:", provincias)

provincias[-3] = "ALAJUELA"
print("Lista de provincias actualizada:", provincias)


# Ejercicio: Crear una lista de números 
listaNumeros = [1, 2, 3, 4, 5]
lista_numeros_pares = [2, 4, 6, 8, 10]
listaNumerosImpares = [1, 3, 9, 5, 7]
listaCosas = ["computadora", 11, "mouse", "teclado", 12, "monitor", "audifonos", 10, 13]

# Concatenar listas
listas_unidas = listaNumeros + listaCosas + lista_numeros_pares + listaNumerosImpares
print("Listas unidas:", listas_unidas)

listaOperaciones = 2 * lista_numeros_pares
print(listaOperaciones) 

lista_numeros_pares.reverse()
print("Lista pares invertida:", lista_numeros_pares)

listaNumerosImpares.sort()
print("Lista impares ordenada:", listaNumerosImpares)

listaNumerosImpares.sort(reverse = True)
print("Lista impares ordenada:", listaNumerosImpares)

# Largo de la lista (cuánto elemetnos tiene la lista)
print("Cantidad de elementos en la lista provincias:", len(provincias))
print("Cantidad de elementos en la lista listas_unidas:", len(listas_unidas))
print("Cantidad de elementos en la lista lista_numeros_pares:", len(lista_numeros_pares))

print(lista_numeros_pares[12])

# ['Cartago', 'Heredia', 'Puntarenas',              'Alajuela']
#                                    , "San José", 

"""
# Antes de meter el elemento ['Cartago', 'Heredia', 'Puntarenas',
# elemento 
# el resto de la lista : 'Alajuela']

['Cartago', 'Heredia', 'Puntarenas', San José, 'Alajuela']

Hasta índice -2: 'Puntarenas', 'Alajuela']
Elemento: San José
El resto: ['Cartago', 'Heredia',
['Cartago', 'Heredia', San José, 'Puntarenas', 'Alajuela']
"""
# Agregar "San José" después de Puntarenas
provincias.insert(3, "San José")                           # ToDo: Posiciones negativas (-2, San José)