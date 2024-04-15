def modificar_y_agregar(diccionario, lista):
    producto['id']=(producto['id']+1)
    producto['nombre']=input("Introduce el nombre del producto: ")
    while producto['precio']<1:
        try:
            producto['precio']=float(input("Introduce el precio del producto"))
        except ValueError:
            print("introduce un número valido")
            return
        print("introduce un número valido")
    lista.append(producto)
producto={
    'id': 0,
    'nombre': 'a',
    'precio': 0,
}
lista_productos=[]
modificar_y_agregar(producto, lista_productos)
print(lista_productos)
print(lista_productos[0])
print(lista_productos[0]['nombre'])
