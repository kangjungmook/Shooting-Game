import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Shooting Game")
screen.bgcolor("white")
screen.tracer(0)

# Create the player turtle
player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Create the bullet
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("red")
bullet.penup()
bullet.speed(0)
bullet.shapesize(stretch_wid=0.5, stretch_len=2)
bullet.hideturtle()

# Create the target
target = turtle.Turtle()
target.shape("circle")
target.color("orange")
target.penup()
target.speed(0)
target.setposition(random.randint(-250, 250), random.randint(100, 250))

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    player.setx(x)

# Shoot the bullet
def shoot():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

# Check for collision between bullet and target
def is_collision(t1, t2):
    distance = ((t1.xcor() - t2.xcor())**2 + (t1.ycor() - t2.ycor())**2)**0.5
    if distance < 15:
        return True
    else:
        return False

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(shoot, "space")

# Initialize the bullet state
bullet_state = "ready"

# Main game loop
while True:
    screen.update()
    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += 20
        bullet.sety(y)
    # Check if bullet is off the screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"
    # Check for collision between bullet and target
    if is_collision(bullet, target):
        target.setposition(random.randint(-250, 250), random.randint(100, 250))
        bullet.hideturtle()
        bullet_state = "ready"

# Start the game
screen.mainloop()
