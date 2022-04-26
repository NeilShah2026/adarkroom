# A Dark Room Python

from game_actions import gameActions


controller = gameActions()


fire_time = 0

def game():
    global fire_time

    controller.console("You are in a dark room.")
    controller.console("The room is freezing cold.")
    controller.console("The fire is dead.")

    while True:
        controller.console("What do you do?")
        action = controller.input("[light fire] [walk] [look around]: ")
        if action == "light fire":
            if fire_time == 0:
                controller.console("You light the fire.")
                fire_time = 1
            else:
                controller.console("The fire is already lit.")
        elif action == "walk":
            controller.console("You walk into the dark.")
            break
        elif action == "look around":
            controller.console("You look around.")
        else:
            controller.console("I don't understand.")
            



