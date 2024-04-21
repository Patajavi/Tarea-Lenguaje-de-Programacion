import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector3D(0, 0, 0)
        else:
            return self / mag

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

# Ejemplo de uso
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("v1 =", v1)
print("v2 =", v2)
print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 * 2 =", v1 * 2)
print("2 * v2 =", 2 * v2)
print("v2 / 2 =", v2 / 2)
print("Magnitude of v1:", v1.magnitude())
print("Normalized v1:", v1.normalize())
print("Dot product of v1 and v2:", v1.dot_product(v2))
print("Cross product of v1 and v2:", v1.cross_product(v2))


#Esta clase Vector3D tiene las siguientes propiedades y métodos:

#x, y, z: Las coordenadas del vector.
#__init__(): Método para inicializar un vector con sus coordenadas.
#__repr__(), __str__(): Métodos para representar el vector como una cadena.
#__eq__(): Método para verificar si dos vectores son iguales.
#__add__(), __sub__(): Métodos para sumar y restar vectores.
#__mul__(), __rmul__(), __truediv__(): Métodos para multiplicar y dividir un vector por un escalar.
#magnitude(): Método para calcular la magnitud del vector.
#normalize(): Método para normalizar el vector (convertirlo en un vector unitario).
#dot_product(): Método para calcular el producto punto entre dos vectores.
#cross_product(): Método para calcular el producto cruz entre dos vectores.
