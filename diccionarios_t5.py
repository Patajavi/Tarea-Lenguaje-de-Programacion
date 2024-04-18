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
