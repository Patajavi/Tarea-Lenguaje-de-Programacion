#1 Escribe un programa en Python para multiplicar todos los elementos de un diccionario.
def multiplicar_valores_diccionario(diccionario):
    producto=1#inicializar el producto en 1
    for i,j in diccionario.items():
        if isinstance(j, dict):
            #si el valor es otro diccionario, hacer una llamada recursiva a sí misma
            producto*=multiplicar_valores_diccionario(j)
        elif isinstance(j, (int, float)):
            #si el valor es un número (int o float), multiplicarlo con producto
            producto*=j
        else:
            #ignorar los valores que no sean numéricos
            print(f"El valor asociado a '{i}' no es numérico y será ignorado.")
    
    return producto

diccionario={
    "a":2,
    "b":{"b_1":3,"b_2":"nonumero"},
    "c":4
}
    
#multiplicar todos los valores numéricos del diccionario
producto=multiplicar_valores_diccionario(diccionario)
    
print(f"El producto de todos los valores numéricos del diccionario es: {producto}")

#2 Escribe un programa en Python para eliminar una clave de un diccionario.
diccionario={
    "a":2,
    "b":3,
    "c":4
}
a="b"
print(diccionario)
def eliminar_clave(diccionario, clave):
# Verificar si la clave existe en el diccionario
    if clave in diccionario:
        # Eliminar la clave utilizando la instrucción `del`
        del diccionario[clave]
        print(f"La clave '{clave}' ha sido eliminada del diccionario.")
    else:
        print(f"La clave '{clave}' no existe en el diccionario.")

    return diccionario

eliminar_clave(diccionario,a)    
print(diccionario)

#3 Escribe un programa en Python para convertir dos listas en un diccionario.
def convertir_listas_a_diccionario(claves, valores):
    #verificar si las listas tienen la misma longitud
    if len(claves) != len(valores):
        raise ValueError("Las listas de claves y valores deben tener la misma longitud.")
    
    #usar zip para emparejar las listas y convertirlas en un diccionario
    diccionario = dict(zip(claves, valores))
    
    return diccionario
    
A=["a","b","c"]
B=[2,3,4]

diccionario=convertir_listas_a_diccionario(A,B)

print(diccionario)

#4 Escribe un programa en Python para ordenar un diccionario dado por clave.
def ordenar_diccionario_por_clave(diccionario):
    #ordenar las claves del diccionario
    claves_ordenadas = sorted(diccionario)
    
    #crear un nuevo diccionario ordenado utilizando las claves ordenadas
    diccionario_ordenado={clave: diccionario[clave] for clave in claves_ordenadas}
    
    return diccionario_ordenado
    
diccionario={
    "z": 1,
    "c":2,
    "a":3
}
A=ordenar_diccionario_por_clave(diccionario)
print(A)

#5 Escribe un programa en Python para obtener los valores máximo y mínimo de un diccionario.
def obtener_maximo_minimo(diccionario):
    #obtener los valores del diccionario
    valores=diccionario.values()
    
    #encontrar el valor mínimo y máximo utilizando las funciones min() y max()
    valor_minimo=min(valores)
    valor_maximo=max(valores)
    
    return print(valor_minimo, valor_maximo)
    
diccionario={
    "a":1,
    "b":2,
    "c":3
}
obtener_maximo_minimo(diccionario)

#6 Escribe un programa en Python para obtener un diccionario a partir de los campos de un objeto.
class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

def crear_diccionario():
    #solicitar claves para una persona
    nombre = input("Introduce el nombre: ")
    edad=0
    while edad<=0:
        print("introduce una edad valida")
        try:
            edad=int(input("Introduce la edad: "))
        except ValueError:
            print("introduce una edad valida")
    ocupacion = input("Introduce la ocupación: ")
    
    #crear una instancia de Persona con los valores introducidos
    persona=Persona(nombre, edad, ocupacion)
    
    #convertir los campos del objeto a un diccionario utilizando vars()
    diccionario_persona=vars(persona)
    return diccionario_persona
    
    
persona=crear_diccionario()

print("El diccionario resultante a partir de los campos de Persona es:", persona)

#7 Escribe un programa en Python para eliminar duplicados del diccionario.
def eliminar_duplicados(diccionario):
#eliminar valores duplicados manteniendo la primera clave que tenga el valor repetido
    # Diccionario para almacenar los pares clave-valor sin duplicados
    diccionario_sin_duplicados = {}
    
    # Conjunto para llevar un registro de los valores que ya han aparecido
    valores_vistos = set()
    
    # Iterar sobre los pares clave-valor del diccionario
    for clave, valor in diccionario.items():
        # Si el valor no se ha visto antes, agregarlo al diccionario sin duplicados
        if valor not in valores_vistos:
            diccionario_sin_duplicados[clave] = valor
            # Marcar el valor como visto
            valores_vistos.add(valor)
    
    return diccionario_sin_duplicados

diccionario={
    "a":1,
    "b":2,
    "c":3,
    "d":2
}
print(diccionario)
    
diccionario_sin_duplicados=eliminar_duplicados(diccionario)
print(f"El diccionario sin duplicados es: {diccionario_sin_duplicados}")

#8 Escribe un programa en Python para verificar si un diccionario está vacío o no.
def verificar_diccionario_vacio(diccionario):
    return len(diccionario) == 0
diccionario1={"a":1}
diccionario2={}

# Verificar si el diccionario está vacío
esta_vacio = verificar_diccionario_vacio(diccionario1)
    
    # Mostrar el resultado
if esta_vacio:
    print("El diccionario está vacío.")
else:
    print("El diccionario no está vacío.")
        
#repetir para el otro diccionario
esta_vacio = verificar_diccionario_vacio(diccionario2)
    
if esta_vacio:
    print("El diccionario está vacío.")
else:
    print("El diccionario no está vacío.")

#9 Escribe un programa en Python para extraer una lista de valores de una lista dada de diccionarios. Diccionario original:[{'Matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}]
    
#10 Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Ciencias [92, 94, 88] Diccionario original: [{'matematicas': 90, 'ciencia': 92}, {'Matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}] 

#11 Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Matemáticas [90, 89, 92]

#12 Escribe un programa en Python para encontrar la longitud de un diccionario de valores.

#13 Escribe un programa en Python para obtener la profundidad de un diccionario.

#14 Escribe un programa en Python para acceder al elemento de la clave de un diccionario por índice. Salida esperada: física matemáticas química

#15 Escribe un programa en Python para convertir un diccionario en una lista de listas.
#Diccionario original: {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'} Convierte el mencionado diccionario en una lista de listas: [[1, 'rojo'], [2, 'verde'], [3, 'negro'], [4, 'blanco'], [5, 'negro']]

#16 Escribe un programa en Python para filtrar números pares de un diccionario de valores.
#Diccionario original: {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]} Filtra números pares de los valores del diccionario mencionado: {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
#Diccionario original: {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]} Filtra números pares de los valores del diccionario mencionado: {'V': [], 'VI': [], 'VII': [2]}
