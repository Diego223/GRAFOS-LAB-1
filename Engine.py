#Universidad del Valle de Guatemala
#Graficas por Computadora
#Laboratorio 1
#Diego Crespo 19541
from Base import Dibujador, color
from random import randint


width = 960
height = 540

caja = Dibujador(height,width)
k=0
while k <100:
    caja.glVertex(randint(0, width), randint(0, height), color(1, 1, 1))
    k += 1
caja.glFinish("salida.bmp")




