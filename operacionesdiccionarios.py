mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
print(mi_diccionario['a'])  # Salida: 1

mi_diccionario['d'] = 4
print(mi_diccionario)  # Salida: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

del mi_diccionario['b']
print(mi_diccionario)  # Salida: {'a': 1, 'c': 3}

valor_eliminado = mi_diccionario.pop('c')
print(valor_eliminado)  # Salida: 3

for clave, valor in mi_diccionario.items():
    print(clave, valor)
  
if 'a' in mi_diccionario:
    print("La clave 'a' está en el diccionario.")

print(len(mi_diccionario))  # Salida: 2

claves = mi_diccionario.keys()
valores = mi_diccionario.values()

otro_diccionario = mi_diccionario.copy()
otro_diccionario.update({'d': 4, 'e': 5})
