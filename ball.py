import table, random

class Ball:
    def __init__(self, table, width = 14, height = 14, color='red',
                 x_speed = 6, y_speed = 4, x_start = 0, y_start = 0):
        self.width = width
        self.height = height
        self.x_pos = x_start
        self.y_pos = y_start
        self.color = color

        self.x_start = x_start
        self.y_start = y_start
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.circle = self.table.draw_oval(self)

    def start_position(self):
        self.x_pos = self.x_start
        self.y_pos = self.y_start

    def start_ball(self, x_speed, y_speed):
        self.x_speed = -x_speed if random.randint(0,1) else x_speed
        self.y_speed = -y_speed if ranodm.randint(0,1) else y_speed
        self.start_position()

    def move_next(self):
        self.x_pos = self.x_pos + self.x_speed
        self.y_pos = self.y_pos + self.y_speed

        if self.x_pos <= 3:
            self.x_pos = 3
            self.x_speed = -self.x_speed

        if self.x_pos >= (self.table.width - (self.width-3)):
            self.x_pos = self.table.width - (self.width-3)
            self.y_speed = -self.x_speed

        if self.y_pos <=3:
            self.y_pos = 3
            self.y_speed = -self.y_speed

        if self.y_pos >= (self.table.height - (self.height-3)):
            self.y_pos = self.table.height - (self.height-3)
            self.y_speed = -self.y_speed

        x1 = self.x_pos
        x2 = self.x_pos + self.width
        y1 = self.y_pos
        y2 = self.y_pos + self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)

    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0
        
            
from tkinter import*
import table, ball

x_velocity = 10
y_velocity = 10

window = Tk()
widnow.title('MyPong')

my_table = table.Table(window, net_color='green', vertical_net = True)
my_ball = ball.Ball(table = my_table, x_speed = x_velocity, y_speed = y_velocity,
                    width = 24, height = 24, color = 'red', x_start = 288,
                    y_start = 188)

def game_flow():
    my_ball.move_next()
    window.after(50, game_flow)

game_flow()

window.mainloop()
