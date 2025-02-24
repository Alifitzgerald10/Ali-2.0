
import turtle
wn = turtle.Screen

alice = turtle.Turtle()
for aColor in ["red", "blue", "green", "yellow", "cyan", "pink"]:
    alice.color(aColor)
    alice.left(150)
    alice.forward(100)
    for _ in range(5):
        alice.left(80)
        alice.forward(100)
    alice.right(4)
    alice.forward(4)