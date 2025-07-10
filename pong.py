import turtle
import time

# Ekran ayarı
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Pong - Final Sürüm")
screen.tracer(0)

WIDTH = screen.window_width()
HEIGHT = screen.window_height()

# Paddle sınıfı
class Paddle(turtle.Turtle):
    def __init__(self, pos_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos_x, 0)

    def up(self):
        if self.ycor() < HEIGHT//2 - 50:
            self.sety(self.ycor() + 30)

    def down(self):
        if self.ycor() > -HEIGHT//2 + 50:
            self.sety(self.ycor() - 30)

# Ball sınıfı
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.initial_speed = 3.0
        self.dx = self.initial_speed
        self.dy = self.initial_speed

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

        # Üst-alt kenarlardan sekme
        if self.ycor() > HEIGHT//2 - 10 or self.ycor() < -HEIGHT//2 + 10:
            self.dy *= -1

        # Sağ-sol kenarlardan sekme
        if self.xcor() > WIDTH//2 - 10 or self.xcor() < -WIDTH//2 + 10:
            self.dx *= -1

    def bounce(self):
        # Yön değiştir
        self.dx *= -1
        self.dy *= 1

        # Mevcut hızlar
        current_speed_x = abs(self.dx)
        current_speed_y = abs(self.dy)

        # Maksimum hız = başlangıç hızının 2 katı
        max_speed = self.initial_speed * 2

        # Eğer maksimumdan küçükse hızlandır
        if current_speed_x < max_speed:
            self.dx *= 1.1
        if current_speed_y < max_speed:
            self.dy *= 1.1

# Oyun sınıfı
class PongGame:
    def __init__(self):
        self.left_paddle = Paddle(-WIDTH//2 + 50)
        self.right_paddle = Paddle(WIDTH//2 - 50)
        self.ball = Ball()
        self.running = False
        self.setup_controls()

    def setup_controls(self):
        screen.listen()
        screen.onkeypress(self.left_paddle.up, "w")
        screen.onkeypress(self.left_paddle.down, "s")
        screen.onkeypress(self.right_paddle.up, "Up")
        screen.onkeypress(self.right_paddle.down, "Down")
        screen.onkey(self.start_game, "Return")  # Enter ile başlat

    def show_menu(self):
        yaz = turtle.Turtle()
        yaz.color("white")
        yaz.hideturtle()
        yaz.penup()
        yaz.goto(0, 0)
        yaz.write("ENTER tuşuna basarak oyuna başla", align="center", font=("Courier", 20, "normal"))

        while not self.running:
            screen.update()
            time.sleep(0.01)

        yaz.clear()

    def start_game(self):
        self.running = True

    def play(self):
        self.show_menu()

        while True:
            screen.update()
            time.sleep(0.01)
            self.ball.move()

            # Sağ paddle çarpması
            if self.ball.xcor() > self.right_paddle.xcor() - 20 and self.ball.distance(self.right_paddle) < 50:
                self.ball.bounce()

            # Sol paddle çarpması
            elif self.ball.xcor() < self.left_paddle.xcor() + 20 and self.ball.distance(self.left_paddle) < 50:
                self.ball.bounce()

# Oyunu başlat
oyun = PongGame()
oyun.play()

