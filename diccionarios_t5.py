#1 Escribe un programa en Python para multiplicar todos los elementos de un diccionario.
def multiplicar_valores_diccionario(diccionario):
    producto = 1  #inicializar el producto en 1
    for i in diccionario.values():
        #verificar si el valor es un número (int o float)
        if isinstance(i, (int, float)):
            #multiplicar el producto con el valor actual
            producto*=i
        else:
            print(f"El valor '{i}' no es un número, por lo que será ignorado.")
    
    return producto

diccionario={
    "a":2,
    "b":3,
    "c":4
}
    
#multiplicar todos los valores numéricos del diccionario
producto=multiplicar_valores_diccionario(diccionario)
    
print(f"El producto de todos los valores numéricos del diccionario es: {producto}")
