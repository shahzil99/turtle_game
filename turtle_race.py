import turtle
import random as rnd
from turtle_helper import *

COLORS = (
    "blue",
    "gold",
    "orange",
    "red",
    "maroon",
    "violet",
    "magenta",
    "purple",
    "navy",
    "yellow",
    "skyblue",
    "cyan",
    "turquoise",
    "lightgreen",
    "green",
    "darkgreen",
    "chocolate",
    "brown",
    "black",
    "gray",
)
NR_OF_PLAYERS = 2

# GLOBALLY -> all players are accessible everywhere !!
players: list[turtle.Turtle] = []


def game_setup():
    # We need turtles.
    global players  # We state that we have a global variable that is being used instead !!

    #list comprehension -> local list with player -> only works within the function if the 'global' keyword is not used.
    players = [create_turtle(COLORS[i]) for i in range(NR_OF_PLAYERS)]

    # Draw the board – need a turtle to do the job.
    setup_turtle = create_turtle("red")
    draw_vertical_line(setup_turtle, (-300, -300), 600)
    write_text(setup_turtle, "START", (-310, 310))
    draw_vertical_line(setup_turtle, (300, -300), 600)
    write_text(setup_turtle, "END", (290, 310))
    setup_turtle.hideturtle()

    # Place the player behind the start line.
    set_players_ready(players, -300, 600)


def run_game():
    run = True
    while run:
        # Update the turtle's x-position with a random value between 1 - 20.
        for player in players:
            player.forward(rnd.randint(1, 20))

        # Check if one of the turtles has crossed the finish line
        for player in players:
            x, y = player.pos()
            if x >= 300:
                run = False

    # If we have a winner, the game ends and we call the 'game ending'.
    end_game()


def end_game():
    draw_end_turtle = create_turtle("black")

    # Sort players by x-position to get them in the correct order.
    player_result_list = sorted(players, key=lambda player: player.xcor(), reverse=True)

    # Helper function to print out the results!!
    write_results(draw_end_turtle, player_result_list, (-50, 200))
    draw_end_turtle.hideturtle()


if __name__ == "__main__":
    game_setup()

    screen = turtle.Screen()
    screen.listen()
    screen.onkeypress(run_game, "space")

    turtle.exitonclick()
