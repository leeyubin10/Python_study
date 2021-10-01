import turtle
import random

screen = turtle.Screen()
image1 = "C:\\temp\\dice1.gif"
image2 = "C:\\temp\\dice2.gif"
image3 = "C:\\temp\\dice3.gif"
image4 = "C:\\temp\\dice4.gif"
image5 = "C:\\temp\\dice5.gif"
image6 = "C:\\temp\\dice6.gif"
screen.addshape(image1)
screen.addshape(image2)
screen.addshape(image3)
screen.addshape(image4)
screen.addshape(image5)
screen.addshape(image6)

t1 = turtle.Turtle()

command = ""
while True:
    if command != "q":
        command = input("명령을 입력하시오: ")
        dice = random.randrange(6)
        if dice == 0:
            t1.shape(image1)
            t1.stamp()
        elif dice == 1:
            t1.shape(image2)
            t1.stamp()
        elif dice == 2:
            t1.shape(image3)
            t1.stamp()
        elif dice == 3:
            t1.shape(image4)
            t1.stamp()
        elif dice == 4:
            t1.shape(image5)
            t1.stamp()
        elif dice == 5:
            t1.shape(image6)
            t1.stamp()
    else:
        exit()
