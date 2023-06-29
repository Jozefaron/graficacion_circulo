from turtle import *
import time
import math

def dibujarCirculo(radio):
    grados = 5
    while grados <= 360:
        Pa = a + radio * (math.cos(math.radians(grados)))
        Pb = b + radio * (math.sin(math.radians(grados)))
        setup(450, 500, 0, 0)
        screensize(400, 300)
        title("Circulo Con Coordenadas Polares")
        goto(Pa, Pb)
        print("a:",Pa,"b:",Pb)
        grados = grados + 5
        time.sleep(0.6)


radio = float(input('Introduce el radio:'))
a = float(input('Introduce la coordena a del circulo:'))
b = float(input('Introduce la coordena b del basico:'))
dibujarCirculo(radio);





