import turtle

def draw_hexagon(t, side_length):
    for i in range(6):
        t.forward(side_length)
        t.left(60)


def draw_triangle(t, side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def draw_hexagon_with_triangles(t, side_length):
    draw_hexagon(t, side_length)

    for i in range(5):
        turtle.forward(side_length)
        turtle.left(120)
        draw_triangle(t, side_length)
        turtle.right(60)

def main():
    window = turtle.Screen()

    t = turtle.Turtle()
    turtle.speed(5)
    side_length = 100

   
  
    draw_hexagon_with_triangles(t, side_length)

    window.mainloop()

if __name__ == "__main__":
    main()
