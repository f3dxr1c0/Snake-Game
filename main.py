import turtle
import time
import random

finestra = turtle.Screen()
finestra.title("Snake by f3dxr1c0")
finestra.setup(width=500, height=400)
finestra.bgcolor("grey")
finestra.tracer(0)

testa = turtle.Turtle()
testa.shape("square")
testa.color("green")
testa.penup()
testa.goto(0, 0)
testa.direzione = "fermo"

mela = turtle.Turtle()
mela.shape("circle")
mela.color("red")
mela.penup()
mela.goto(100, 100)

def vai_su():
    testa.direzione = "su"

def vai_giu():
    testa.direzione = "giu"

def vai_sinistra():
    testa.direzione = "sinistra"

def vai_destra():
    testa.direzione = "destra"

finestra.listen()
finestra.onkeypress(vai_su, "Up")
finestra.onkeypress(vai_giu, "Down")
finestra.onkeypress(vai_sinistra, "Left")
finestra.onkeypress(vai_destra, "Right")

def muovi():
    if testa.direzione == "su":
        testa.sety(testa.ycor() + 20)
    elif testa.direzione == "giu":
        testa.sety(testa.ycor() - 20)
    elif testa.direzione == "sinistra":
        testa.setx(testa.xcor() - 20)
    elif testa.direzione == "destra":
        testa.setx(testa.xcor() + 20)

def controlla_bordi():
    if testa.xcor() > 240:
        testa.setx(240)
    if testa.xcor() < -240:
        testa.setx(-240)
    if testa.ycor() > 170:
        testa.sety(170)
    if testa.ycor() < -170:
        testa.sety(-170)

def sposta_mela():
    x = random.randint(-240, 240)
    y = random.randint(-170, 170)
    mela.goto(x, y)

while True:
    finestra.update()
    muovi()
    controlla_bordi()
    if testa.distance(mela) < 20:
        sposta_mela()
    time.sleep(0.1)