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

#9 Escribe un programa en Python para extraer una lista de valores de una lista dada de diccionarios. Diccionario original:[{'Matematicas': 90, 'Ciencia': 92}, {'Matematicas': 89, 'Ciencia': 94}, {'Matematicas': 92, 'Ciencia': 88}]
#10 Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Ciencias [92, 94, 88]
#11 Extrae una lista de valores de dicha lista de diccionarios donde la asignatura = Matemáticas [90, 89, 92]
def extraer_valores(lista_diccionarios, clave):
    #usar listas comprimidas para extraer los valores asociados con la clave especificada
    valores = [diccionario[clave] for diccionario in lista_diccionarios if clave in diccionario]
    return valores
lista_diccionarios=[
    {'Matematicas': 90, 'Ciencia': 92},
    {'Matematicas': 89, 'Ciencia': 94},
    {'Matematicas': 92, 'Ciencia': 88}
]
clave = 'Matematicas'
clave2 = 'Ciencia'
valores = extraer_valores(lista_diccionarios, clave)
print(f"Lista de valores de la clave '{clave}': {valores}")
valores = extraer_valores(lista_diccionarios, clave2)
print(f"Lista de valores de la clave '{clave2}': {valores}")

#12 Escribe un programa en Python para encontrar la longitud de un diccionario de valores.
def calcular_longitud_diccionario(diccionario):
    #usar len() para calcular la longitud del diccionario
    longitud=len(diccionario)
    return longitud
diccionario={
    "a":1,
    "b":2,
    "c":3,
    "d":4
}
longitud=calcular_longitud_diccionario(diccionario)
print(f"La longitud del diccionario es: {longitud}")

#13 Escribe un programa en Python para obtener la profundidad de un diccionario.
def calcular_profundidad_diccionario(diccionario):
    profundidad_maxima = 1
    for valor in diccionario.values():
        #recursividad go brrr
        if isinstance(valor, dict):
            profundidad_dic_anidado = calcular_profundidad_diccionario(valor)
            profundidad_maxima = max(profundidad_maxima, 1 + profundidad_dic_anidado)
    return profundidad_maxima
    
diccionario={
    "a":{"b":{"c":{"d"}}}
}

pmax=calcular_profundidad_diccionario(diccionario)
print(f"la profundidad del diccionario es:{pmax}")

#14 Escribe un programa en Python para acceder al elemento de la clave de un diccionario por índice. Salida esperada: física matemáticas química
def acceder_elemento_por_indice(diccionario, indice):
    # Obtener una lista de claves del diccionario
    claves = list(diccionario.keys())
    # Acceder a la clave en el índice especificado
    clave = claves[indice]
    # Obtener el valor de la clave en el índice especificado
    valor = diccionario[clave]
    # Retornar la clave y el valor
    return clave, valor
diccionario = {"física": 90, "matemáticas": 80, "química": 70}
    
# Imprimir todos los elementos del diccionario por índice
print("Salida esperada:")
for indice in range(len(diccionario)):
    # Acceder al elemento de la clave por índice
    clave, valor = acceder_elemento_por_indice(diccionario, indice)
        
    # Mostrar la clave
    print(clave)
#no es esto mas facil?
for i in diccionario:
    print(i)
#15 Escribe un programa en Python para convertir un diccionario en una lista de listas.
#Diccionario original: {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'} Convierte el mencionado diccionario en una lista de listas: [[1, 'rojo'], [2, 'verde'], [3, 'negro'], [4, 'blanco'], [5, 'negro']]
def convertir_diccionario_a_lista(diccionario):
     #usar listas comprimidas para convertir el diccionario en una lista de listas
    lista_de_listas = [[clave, valor] for clave, valor in diccionario.items()]
    
    return lista_de_listas
    
diccionario_original={1:'rojo', 2:'verde', 3:'negro', 4:'blanco', 5:'negro'}

lista=convertir_diccionario_a_lista(diccionario_original)
print(f"la lista de listas obtenida es: {lista}")

#16 Escribe un programa en Python para filtrar números pares de un diccionario de valores.
#Diccionario original: {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]} Filtra números pares de los valores del diccionario mencionado: {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
#Diccionario original: {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]} Filtra números pares de los valores del diccionario mencionado: {'V': [], 'VI': [], 'VII': [2]}
def filtrar_numeros_pares(diccionario):
    #usar compresion de diccionarios para filtrar los valores
    diccionario_filtrado = {
        clave:[numero for numero in valores if numero % 2 == 0]
        for clave, valores in diccionario.items()
    }
    return diccionario_filtrado
diccionario1 = {'V':[1, 4, 6, 10], 'VI':[1, 4, 12], 'VII':[1, 3, 8]}
diccionario2 = {'V':[1, 3, 5], 'VI':[1, 5], 'VII':[2, 7, 9]}

diccionario_filtrado1=filtrar_numeros_pares(diccionario1)
print("Diccionario original:")
print(diccionario1)
print("Diccionario filtrado:")
print(diccionario_filtrado1)

diccionario_filtrado2=filtrar_numeros_pares(diccionario2)
print("Diccionario original:")
print(diccionario2)
print("Diccionario filtrado:")
print(diccionario_filtrado2)
