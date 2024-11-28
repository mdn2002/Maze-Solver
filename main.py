from graphics import Window, Point, Line

if __name__ == "__main__":
    window = Window(800, 600)

    p1 = Point(50, 50)
    p2 = Point(450, 50)
    p3 = Point(50, 150)
    p4 = Point(450, 150)

    # Create line objects
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)

    # Draw the lines
    window.draw_line(line1, "black")  # Draw line 1 in black
    window.draw_line(line2, "red")    # Draw line 2 in red
    window.wait_for_close()
