import turtle

# Configuración inicial de la ventana
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(-10, -10, 10, 10)

# Crear el objeto Turtle
pen = turtle.Turtle()
pen.penup()
pen.speed(0)  # Configurar la velocidad al máximo

# Función para dibujar la parábola
def dibujar_parabola(a, b, c):
	x = -10.0
	while x <= 10.0:

		y = a * x ** 2 + b * x + c
		pen.goto(x, y)
		x += 0.2
		pen.pendown()
	pen.penup()

# Parámetros de la parábola (coeficientes a, b, c)
a = 1  # Coeficiente cuadrático
b = 0  # Coeficiente lineal
c = 0  # Término independiente

# Dibujar la parábola con los parámetros especificados
dibujar_parabola(a, b, c)

# Mantener la ventana abierta
#screen.mainloop()
