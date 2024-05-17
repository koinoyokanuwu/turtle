import turtle
import random

# Se crea una nueva tortuga para dibujar el cuadro.
my_square = turtle.Turtle()
my_square.color('purple')
my_square.shape('turtle')
# Se crea una nueva tortuga que funciona como puntero.
my_dot = turtle.Turtle()
my_dot.color('red')
my_dot.shape('turtle')

# Se dibuja el nuevo cuadro rotando hacia la izquierda 4 veces
for _ in range(4):
  my_square.forward(200)
  my_square.left(90)

# Se oculta el indicador de la tortuga que dibuja el cuadro
my_square.hideturtle()
# Se posiciona el punto en el centro del cuadro
my_dot.goto(100,100)
# Se borra la línea que se dibuja cuando se posiciona el punto
my_dot.clear()

# Se definen los límetes del cuadro, en forma de coordenadas x,y
minX, maxX = 0, 200
minY, maxY = 0, 200

# Ciclo infinito
while True:
  # Se direcciona el punto en un ángulo cualquiera entre 20 y 340 grados
  my_dot.setheading(random.randint(20,340))
  # Contador para hacer desplazar el punto
  counter = 0
  # Se define una variable para controlar cuando se toque el borde
  border = False
  # Mientras que no se toque el borde
  while border == False:
    # El punto va a avanzar 0.5 px
    my_dot.forward(counter+0.5)
    # Cunado el punto toca alguno de los límites ya sea en x o y
    if not minX <= my_dot.xcor() <= maxX or not minY <= my_dot.ycor() <= maxY:
      # Escritó sólo con propósitos de debug, se puede borrar
      print(my_dot.pos())
      # Se reposiciona el punto en un lugar que no tenga decimales para que sea más fácil su dirección en el otro ciclo
      my_dot.goto(round(my_dot.xcor()),round(my_dot.ycor()))
      # Se dice que tocó el borde y se rompe el ciclo para que vuelva comenzar 
      border = True
