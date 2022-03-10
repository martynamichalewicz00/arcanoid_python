import turtle
import time
import random
import math

i=0
ii=0
j=0

okno=turtle.Screen()
okno.title("odbijaj pilki")
okno.bgcolor("white")
okno.setup(width=600, height=800,starty=0)
okno.tracer(0)

gracz=turtle.Turtle()#utworzenie obiektu
gracz.speed(0)#szybkosc renderu
gracz.shape("square")#ksztalt
gracz.shapesize(stretch_wid=0.5,stretch_len=10)#zmiana ksztaltu
gracz.color("black")#kolor obiektu
gracz.penup()#obiekt moze sie poruszac bez pozostawiania sladow
gracz.goto(0,-300)#polozenie obiektu

pilka=turtle.Turtle()#utworzenie obiektu
pilka.speed(3)#szybkosc renderu
pilka.shape("circle")#ksztalt
pilka.shapesize(stretch_wid=0.5,stretch_len=0.5)#zmiana ksztaltu
pilka.color("black")#kolor obiektu
pilka.penup()#obiekt moze sie poruszac bez pozostawiania sladow
pilka.goto(0,250)#polozenie obiektu
pilka.dx=0.001
pilka.dy=0.001

predkosc=0.1
predkoscc=1
wypadlo=0
limit=10
moc=0
max=0
dlugosc=0
prawda=1

wynik=turtle.Turtle()
wynik.speed(0)
wynik.color("black")
wynik.penup()
wynik.hideturtle()
wynik.goto(0,260)
wynik.write("Pilka wypadla ci 0 razy, aktualna predkosc pilki: 1",align="center",font=("Courier",12,"normal"))

emodzi=turtle.Turtle()
emodzi.speed(0)
emodzi.color("black")
emodzi.penup()
emodzi.hideturtle()
emodzi.goto(0,0)
reakcje=[':(','noooh','ale zal','a niech to','D:',':[[','cholera','no nieee']

punkty=turtle.Turtle()
punkty.speed(0)
punkty.color("black")
punkty.penup()
punkty.hideturtle()
punkty.goto(0,320)
punkty.write("Punkty:0",align="center",font=("Courier",35,"normal"))

najlepszy=turtle.Turtle()
najlepszy.speed(0)
najlepszy.color("gray")
najlepszy.penup()
najlepszy.hideturtle()
najlepszy.goto(0,300)
najlepszy.write("Najlepszy wynik: 0",align="center",font=("Courier",10,"normal"))


def ruch_w_lewo():
    x=gracz.xcor()
    x-=15
    gracz.setx(x)
def ruch_w_prawo():
    x=gracz.xcor()
    x+=15
    gracz.setx(x)
def szybciej():
    pilka.dx += 0.03
    pilka.dy += 0.03
    #predkosc+=1


pozycja_y=0
predkosc_y=0
okno.listen()
pozycja_x_obiektu=0
kat=1
grawitacja=0.00025
pkt=0
okno.onkeypress(ruch_w_lewo,"Left")
okno.onkeypress(ruch_w_prawo,"Right")
#okno.onkeypress(szybciej,"w")


while True:
    okno.update()
    pilka.setx(pilka.xcor() - pilka.dx)
    pilka.sety(pilka.ycor() - pilka.dy)
    pilka.dy+=grawitacja
    pozycja_x_obiektu=gracz.xcor()
    if prawda==1:
        dlugosc += 0.005
        if dlugosc > 5:
            prawda = 0
    elif prawda==0:
        dlugosc-=0.005
        if dlugosc<0:
            prawda=1


    gracz.shapesize(stretch_wid=0.5, stretch_len=10-dlugosc)  # zmiana ksztaltu

    if i!=0:
        gracz.goto(pozycja_x_obiektu, -300 - i)
        i-=1
        ii+=1
    if ii==23:
        if j>0:
            gracz.goto(pozycja_x_obiektu,-300+1*j)
            j-=1
        if j==0:
            ii=0




    najlepszy.clear()

    punkty.clear()
    punkty.write("Punkty:{}".format(pkt), align="center", font=("Courier", 35, "normal"))
    if pkt>max:
        max=pkt

    if pilka.ycor()<-390:
        pilka.goto(0,0)
        pilka.dx = 0.05
        pilka.dy = 0.05
        wypadlo+=1
        wynik.clear()
        wynik.write("Pilka wypadla ci {} razy, aktualna predkosc pilki: 1".format(wypadlo), align="center",
                    font=("Courier", 12, "normal"))
        predkoscc=0
        emodzi.write(random.choice(reakcje), align="center", font=("Courier", 30, "normal"))
        time.sleep(1)
        emodzi.clear()
        gracz.goto(0,-300)
        pkt=0
    if pilka.ycor()>200:
        pilka.dy+=0.0005
    if pilka.ycor()>390:
       pilka.dy*=-1
    if pilka.xcor()<-300:
        pozycja_y=pilka.ycor()
        #pilka.goto(300,pozycja_y)
        pilka.dx*=-1
    if pilka.xcor()>300:
        pozycja_y=pilka.ycor()
        #pilka.goto(-300,pozycja_y)
        pilka.dx *= -1
    if gracz.xcor()<-380:
        gracz.goto(380,-300)
    if gracz.xcor()>380:
        gracz.goto(-380,-300)
    if pilka.ycor()<-300 and pilka.ycor()>-310 and (pilka.xcor()<gracz.xcor()+100-dlugosc and pilka.xcor()>gracz.xcor()-100-dlugosc):
        i=25
        j=15
        pilka.sety(-300)
        predkosc=(abs(pilka.xcor()-gracz.xcor()))/300
        kat=abs(pilka.xcor()-gracz.xcor())
        pilka.dx = pilka.dx+predkosc*pilka.dx
        pilka.dy = pilka.dy + predkosc * pilka.dy
        if pilka.xcor()<gracz.xcor() and pilka.dx<0:
            pilka.dx*=-1
        elif pilka.xcor()>gracz.xcor() and pilka.dx>0:
            pilka.dx*=-1
        if kat>20:
            pilka.dx-=0.2
            pilka.dx *= kat / 100
        elif kat<=20:
            pilka.dx-=0.4

        pilka.dy *= -1
        predkoscc+=predkosc
        pkt+=1
        #wynik.clear()
        #wynik.write("Pilka wypadla ci {} razy, aktualna predkosc pilki: {}".format(wypadlo,float(predkoscc)), align="center",
               #     font=("Courier", 12, "normal"))
    wynik.clear()
    wynik.write("Pilka wypadla ci {} razy, aktualna predkosc pilki: {}".format(wypadlo, round(abs(pilka.dy),2)),align="center",font=("Courier", 12, "normal"))
    najlepszy.write("Najlepszy wynik: {}".format(max), align="center", font=("Courier", 10, "normal"))






