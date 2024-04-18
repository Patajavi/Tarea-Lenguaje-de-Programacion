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
