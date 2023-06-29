from turtle import *
import time
radio = float(input("intruduce el radio "))
xc = int(input("introduce el valor en x del centro"))
yc =int( input("intriduce el valor en y del centro"))
pk =(5 / 4) - radio
contador=1

def ochopuntos(pk,contador,xc,yc):

    for i in [1,2,3,4,5,6,7,8]:
        x=0
        y=radio
        pk =(5 / 4) - radio
        while y >= x:
            if pk < 0:
                x = x + 1
                pk = pk + (2*x) + 3
            else:
                x = x + 1
                y = y - 1
                pk = pk + 2 * x + 1 -(2 * y)
            setup(450,500,0,0)
            screensize(400,300)
            title("circulo con bresenham")
            if contador == 1:
                goto((x,y))
            if contador == 2:
                goto(y,x)
                pendown()
            if contador == 4:
                goto(x,-y)
                pendown()
            if contador == 7:
                goto(-y,x)
                pendown()
            if contador == 6:
                goto(-y,-x)
                pendown()
            if contador == 5:
                goto(-x,-y)
                pendown()
            if contador == 3:
                goto(y,-x)
                pendown()
            if contador == 8:
                goto(-x,y)
                pendown()
            time.sleep(0.1)
            print(contador)
            print(x,y)
        penup()
        contador =contador + 1
ochopuntos(pk,contador,xc,yc)
