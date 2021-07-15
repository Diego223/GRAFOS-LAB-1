#Universidad del Valle de Guatemala
#Graficas por Computadora
#Laboratorio 1
#Diego Crespo 19541
import struct
import numpy
from collections import namedtuple


def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

def color(r, g, b):
    # Acepta valores de 0 a 1
    # Se asegura que la información de color se guarda solamente en 3 bytes
    return bytes([ int(b * 255), int(g* 255), int(r* 255)])


BLACK = color(0,0,0)
WHITE = color(1,1,1)


class Dibujador(object):
    def __init__(self, width, height):
        #Constructor clase
        self.curr_color = WHITE
        self.clear_color = BLACK
        self.glCreateWindow(width, height)
        #Creador Ventana
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glClear()
        self.glViewport(0,0, width, height)
        #Creador del ViewPort
    def glViewport(self, x, y, width, height):
        self.vpX = x
        self.vpY = y
        self.vpWidth = width
        self.vpHeight = height
    

    def glClearColor(self, r, g, b):
        self.clear_color = color(r, g, b)

    def glClear(self):
        # Coloca los pixeles del color default (blanco)
        self.pixels = [[ self.clear_color for y in range(self.height)] for x in range(self.width)]


        #Cambia el color del fondo
    def glColor(self, r, g, b):
        self.curr_color = color(r,g,b)

        #Crea un punto en coordenadas seleccionadas
    def glVertex(self, x, y, color = None):
        if x < self.vpX or x >= self.vpX + self.vpWidth or y < self.vpY or y >= self.vpY + self.vpHeight:
            return

        if (0 < x < self.width) and (0 < y < self.height):
            self.pixels[int(x)][int(y)] = color or self.curr_color

    

    def glFinish(self, filename):
        #Crea un archivo BMP 
        with open(filename, "wb") as file:
            file.write(bytes('B'.encode('ascii')))
            file.write(bytes('M'.encode('ascii')))
            file.write(dword(14 + 40 + (self.width * self.height * 3)))
            file.write(dword(0))
            file.write(dword(14 + 40))

            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])









