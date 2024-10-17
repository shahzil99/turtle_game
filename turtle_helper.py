import turtle


# A function that creates a turtle and returns it. 
# It should have the shape of a turtle and a color.
def create_turtle(color: str) -> turtle.Turtle:
    t = turtle.Turtle()
    t.color(color)
    t.shape("turtle")
    return t


def draw_vertical_line(t: turtle.Turtle, pos: tuple[int, int], height: int) -> None:
    # (x, y) = (-300, -300)
    t.penup()
    t.goto(pos[0], pos[1])

    # 0 => right, 90 => up, 180 => left, 270 => down
    t.setheading(90)
    t.pendown()
    t.forward(height)


def write_text(t: turtle.Turtle, text: str, pos: tuple[int, int]) -> None:
    t.penup()
    t.goto(pos[0], pos[1])
    t.write(text)


def set_players_ready(
    players: list[turtle.Turtle], start_left_pos: int, height_start_line: int
) -> None:
    # A simple version -> we know there are two players.
    x = start_left_pos - 20
    y = 150
    for player in players:
        player.penup()
        player.setheading(0)  # Face to the right
        player.goto(x, y)
        y -= 300


def write_results(
    t: turtle.Turtle, result_list: list[turtle.Turtle], pos: tuple[int, int]
) -> None:
    t.penup()
    t.goto(pos[0], pos[1])
    t.write("RESULTATLISTE:")
    x, y = pos
    y -= 20  # Adjust down before we start with the player
    for idx, p in enumerate(result_list):
        t.goto(x, y)
        t.write(f"{idx+1}: {p.color()[0]}")
        y -= 20
