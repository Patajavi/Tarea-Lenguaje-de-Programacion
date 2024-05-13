import random
import turtle

# Función para generar números aleatorios y calcular frecuencias
def generar_histograma(n):
    # Generar n valores aleatorios entre 0 y 1
    valores = [random.random() for _ in range(n)]

    # Inicializar diccionario para almacenar frecuencias
    frecuencias = {}

    # Calcular frecuencias para intervalos de 0.1
    for i in range(11):
        frecuencias[i] = sum(1 for valor in valores if i / 10 <= valor < (i + 1) / 10)

    return frecuencias
# Función para dibujar un histograma con Turtle
def dibujar_histograma(frecuencias):
    pantalla = turtle.Screen()
    pantalla.setup(width=800, height=600)
    pantalla.setworldcoordinates(0, 0, 12, max(frecuencias.values()) + 1)

    pen = turtle.Turtle()
    pen.penup()
    pen.speed(0)
    pen.goto(1, 0)
    pen.pendown()

    for intervalo, frecuencia in frecuencias.items():
        pen.begin_fill()
        pen.left(90)
        pen.forward(frecuencia)
        pen.right(90)
        pen.forward(0.9)
        pen.right(90)
        pen.forward(frecuencia)
        pen.left(90)
        pen.end_fill()
        pen.penup()
        pen.forward(1)
        pen.pendown()

    pantalla.mainloop()

# Generar histograma para 50 valores y dibujarlo
frecuencias_50 = generar_histograma(50)
dibujar_histograma(frecuencias_50)

# Generar histograma para 1000 valores y dibujarlo
frecuencias_1000 = generar_histograma(1000)
dibujar_histograma(frecuencias_1000)
