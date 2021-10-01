import turtle
t=turtle.Turtle()
while True:
    command = input("명령을 입력하세요:")
    if command == "l":
        t.left(90)
        t.forward(100)

    if command == "r":
        t.right(90)
        t.forward(100)
        
