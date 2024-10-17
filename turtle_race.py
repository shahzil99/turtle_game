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

# GLOBALT -> alle spillere er tilgjengelig overalt !!!
players: list[turtle.Turtle] = []


def game_setup():
    # Vi trenger skilpadder
    global players  # Vi forteller at vi har en global variable som brukes istedet !!!!
    # for i in range(NR_OF_PLAYERS):
    #    col = COLORS[i]
    #    players.append(create_turtle(col))

    # list-comprehension -> local liste med spiller -> virker bare i funksjonen hvis ikke 'global' keyword er brukt
    players = [create_turtle(COLORS[i]) for i in range(NR_OF_PLAYERS)]

    # tegne opp brettet - trenger en turtle som gjør jobben
    setup_turtle = create_turtle("red")
    draw_vertical_line(setup_turtle, (-300, -300), 600)
    write_text(setup_turtle, "START", (-310, 310))
    draw_vertical_line(setup_turtle, (300, -300), 600)
    write_text(setup_turtle, "END", (290, 310))
    setup_turtle.hideturtle()

    # Plassere spiller bak start streken.
    set_players_ready(players, -300, 600)


def run_game():
    run = True
    while run:
        # oppdatere turtle x-posisjon med en random verdi mellom 1 - 20
        for player in players:
            player.forward(rnd.randint(1, 20))

        # sjekke om en av turtle har kommet over målstreken
        for player in players:
            x, y = player.pos()
            if x >= 300:
                run = False

    # har vi en vinner avsluttes spillet og vi kaller på 'game ending'
    end_game()


def end_game():
    draw_end_turtle = create_turtle("black")

    # sortere players etter x-posisjon for å få de i riktig rekkefølge
    player_result_list = sorted(players, key=lambda player: player.xcor(), reverse=True)

    # hjelpe funksjon til å skrive ut resultatene !!
    write_results(draw_end_turtle, player_result_list, (-50, 200))
    draw_end_turtle.hideturtle()


if __name__ == "__main__":
    game_setup()

    screen = turtle.Screen()
    screen.listen()
    screen.onkeypress(run_game, "space")

    turtle.exitonclick()
