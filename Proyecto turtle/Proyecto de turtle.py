import turtle

ventana = turtle.Screen()
ventana.title("Mi primera tortuga")
ventana.setup(600,400,100,100)

tortuga = turtle.Turtle()
tortuga.shape("turtle")


tortuga.speed(0)

tortuga.color("blue")

def cuadrado(x):
    for i in range (20):
        tortuga.forward(70)
        tortuga.right(30)
        tortuga.forward(90)
        tortuga.right(220)

cuadrado(20)

def esfera():
    for i in range (60):
        cuadrado(50)
        tortuga.forward(190)
        tortuga.right(90)
esfera()

tortuga.color("yellow")
def cuadrado(x):
    for i in range (4):
        tortuga.forward(40)
        tortuga.right(60)
        tortuga.forward(40)
        tortuga.right(120)

cuadrado(40)

def esfera():
    for i in range (40):
        cuadrado(40)
        tortuga.forward(15)
        tortuga.right(10)

esfera()

tortuga.color("red")

def estrella():
    for i in range(5):
        tortuga.forward(200)
        tortuga.right(144)

estrella()

def Estrella():
    for i in range (50):
        estrella()
        tortuga.forward(15)
        tortuga.right(10)
Estrella()

tortuga.penup()
tortuga.home()
tortuga.pendown()






tortuga.color("brown")

def pepe(x):
    for i in range (4):
        tortuga.forward(100)
        tortuga.right(90)
        tortuga.forward(90)
        tortuga.right(20)

pepe(60)

def esferape():
    for i in range (50):
        pepe(60)
        tortuga.forward(100)
        tortuga.right(90)
esferape()

tortuga.penup()
tortuga.home()
tortuga.pendown()
tortuga.color("orange")
def victor123(x):
    for i in range (20):
        tortuga.forward(160)
        tortuga.right(75)

victor123(20)

def victor1234():
    for i in range (50):
        victor123(20)
        tortuga.forward(160)
        tortuga.right(84)
        tortuga.left(85)
victor1234()


tortuga.penup()
tortuga.goto(-200,100)
tortuga.pendown()
tortuga.color("red")



def pollo():
    for i in range (6):
        tortuga.forward(95)
        tortuga.right(90)

pollo()

def broaster():
    for i in range (60):
        pollo()
        tortuga.forward(55)
        tortuga.right(15)

broaster()


tortuga.color("violet")
def chaufa():
    for i in range(8):
        tortuga.forward(70)
        tortuga.right(135)

chaufa()

def wantan():
    for i in range(42):
        chaufa()
        tortuga.forward(15)
        tortuga.right(10)

wantan()

tortuga.color("blue")

tortuga.right(180)
def redbull(x):
    for i in range (4):
        tortuga.forward(50)
        tortuga.right(20)
        tortuga.forward(60)
        tortuga.right(2206)

redbull(40)

def frugito():
    for i in range (50):
        redbull(40)
        tortuga.forward(190)
        tortuga.right(10)
frugito()

tortuga.color("green")
def magra(x):
    for i in range (4):
        tortuga.forward(40)
        tortuga.right(90)
        tortuga.forward(90)
        tortuga.right(20)

magra(60)

def petunia():
    for i in range (50):
        magra(60)
        tortuga.forward(90)
        tortuga.right(90)
petunia()

tortuga.color("silver")


def mamani(x):
    for i in range (4):
        tortuga.forward(52)
        tortuga.right(88)
        tortuga.forward(30)
        tortuga.right(88)
        tortuga.left(89)
tortuga.penup()
tortuga.goto(-500,+200)
tortuga.pendown()
def frugos():
    for i in range (90):
        mamani(20)
        tortuga.forward(9)
        tortuga.right(30)
        tortuga.left(88)
        tortuga.forward(30)
        tortuga.right(88)
        tortuga.left(89)


frugos()



ventana.mainloop()