from tkinter import *
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
current_word = {}
to_learn = {}
# ---------------------------- DATAFRAME ------------------------------ #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/lithuanian-word-list.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# ----------------------- NEW WORD GENERATION ------------------------- #
def new_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(language_text, text="Lithuanian", fill="black")
    canvas.itemconfig(word_text, text=current_word["Lithuanian"], fill="black")
    canvas.itemconfig(card_background, image=background_image)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- FLIP CARD ------------------------------ #
def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_word["English"], fill="white")
    canvas.itemconfig(card_background, image=flipped_background)

# ---------------------------- REMOVE CARD ------------------------------ #
def is_known():
    to_learn.remove(current_word)
    new_word()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Lithuanian Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background_image = PhotoImage(file="images/card_front.png")
flipped_background = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=background_image)
language_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

red_image = PhotoImage(file="images/wrong.png")
red_button = Button(image=red_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_word)
red_button.grid(column=0, row=1)

green_image = PhotoImage(file="images/right.png")
green_button = Button(image=green_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
green_button.grid(column=1, row=1)

new_word()

window.mainloop()