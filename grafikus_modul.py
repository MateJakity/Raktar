import turtle
from cikk import Cikk

def rajzol_keszlet(keszlet):

    if not keszlet:
        print("A készlet üres, nincs mit rajzolni.")
        return

    screen = turtle.Screen()
    screen.title("Raktár készlet - turtle grafika")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    info = turtle.Turtle()
    info.hideturtle()
    info.penup()
    info.goto(0, -250)

    max_menny = max(c.mennyiseg for c in keszlet)
    if max_menny == 0:
        max_menny = 1

    bar_width = 20
    spacing = 10
    scale = 200 / max_menny

    start_x = - (len(keszlet) * (bar_width + spacing)) / 2

    bar_areas = []  # (x1, y1, x2, y2, cikk)

    t.penup()
    t.goto(start_x, 0)
    t.pendown()

    for i, c in enumerate(keszlet):
        x = start_x + i * (bar_width + spacing)
        height = c.mennyiseg * scale

        t.penup()
        t.goto(x, 0)
        t.pendown()
        t.begin_fill()
        for _ in range(2):
            t.forward(bar_width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

        t.penup()
        t.goto(x, -20)
        t.write(str(c.id), font=("Arial", 8, "normal"))

        bar_areas.append((x, 0, x + bar_width, height, c))

    def kezelo(x, y):
        for x1, y1, x2, y2, c in bar_areas:
            if x1 <= x <= x2 and y1 <= y <= y2:
                info.clear()
                szoveg = f"ID {c.id} - {c.nev}, {c.mennyiseg} {c.egyseg}, {c.egysegar} Ft"
                info.write(szoveg, align="center", font=("Arial", 10, "normal"))
                break

    screen.onscreenclick(kezelo)

    screen.mainloop()