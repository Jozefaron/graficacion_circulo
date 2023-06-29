from turtle import *
import time
import math

def dibujarCirculoBasico(radio):
    grados = 5
    while grados <= 360:
        Cx = x + radio * (math.cos(math.radians(grados)))
        Cy = y + radio * (math.sin(math.radians(grados)))
        setup(450, 500, 0, 0)
        screensize(400, 300)
        title("Circulo Con Coordenadas Basicas")
        goto(Cx, Cy)
        print("x:",Cx,"y:",Cy)
        grados = grados + 5
        time.sleep(0.6)


radio = float(input('Introduce el radio:'))
x = float(input('Introduce la coordena x del circuloBasico:'))
y = float(input('Introduce la coordena y del circuloBasico:'))
dibujarCirculoBasico(radio);

