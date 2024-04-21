# Función para imprimir los subdiccionarios que tienen una clave con el valor especificado en una posición específica
def imprimir_subdiccionarios(diccionario, nombre_posicion, valor):
    subdiccionarios_coincidentes = []
    for subdiccionario in diccionario.values():
        # Verificar si el subdiccionario tiene la clave en la posición especificada con el valor especificado
        if nombre_posicion in subdiccionario and subdiccionario[nombre_posicion] == valor:
            subdiccionarios_coincidentes.append(subdiccionario)
    if subdiccionarios_coincidentes:
        print("Los subdiccionarios que coinciden son:")
        for subdiccionario in subdiccionarios_coincidentes:
            print(subdiccionario)
    else:
        print("No se encontraron subdiccionarios que coincidan con los criterios especificados.")

# Diccionario de ejemplo con diccionarios anidados
diccionario_anidado = {
    'dicc1': {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'},
    'dicc2': {'clave1': 'valorX', 'clave2': 'valor2', 'clave3': 'valor3'},
    'dicc3': {'clave1': 'valor1', 'clave2': 'valorX', 'clave3': 'valor3'},
    'dicc4': {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valorX'}
}

# Pedir al usuario que introduzca la clave y el valor
nombre_posicion_especificada = input("Introduce la clave que deseas buscar: ")
valor_especifico = input("Introduce el valor que deseas buscar: ")

# Verificar si la clave y el valor son válidos
while nombre_posicion_especificada not in diccionario_anidado['dicc1']:
    print("La clave introducida no es válida. Inténtalo de nuevo.")
    nombre_posicion_especificada = input("Introduce la clave que deseas buscar: ")

while valor_especifico not in set(diccionario_anidado[dicc].get(nombre_posicion_especificada) for dicc in diccionario_anidado):
    print("El valor introducido no es válido. Inténtalo de nuevo.")
    valor_especifico = input("Introduce el valor que deseas buscar: ")

# Llamar a la función para imprimir los subdiccionarios que coinciden
imprimir_subdiccionarios(diccionario_anidado, nombre_posicion_especificada, valor_especifico)
