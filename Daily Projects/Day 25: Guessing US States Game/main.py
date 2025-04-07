import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
print(len(all_states))
while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed",
                                    prompt="What's another state's name? Type \"exit\" to exit the game.").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        data_to_learn = pandas.DataFrame(states_to_learn)
        data_to_learn.to_csv("states_to_learn.csv")
        break



screen.exitonclick()
