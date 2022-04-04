import turtle
def ftree(f, branchl, k, angle):
  if branchl > 7:
    f.forward(branchl)
    diff = branchl - k
    f.left(angle)
    ftree(f, diff, k, angle)
    f.right(2*angle)
    ftree(f, diff, k, angle)
    f.left(angle)
    f.backward(branchl)
fractal = turtle.Turtle()
fractal.hideturtle()
fractal.speed(30)
fractal.setheading(90)
fractal.color('green')
ftree(fractal, 75, 10, 30)
turtle.mainloop()