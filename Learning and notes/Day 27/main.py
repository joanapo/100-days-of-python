from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)

label = Label(text='I am a Label', font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input = Entry()
input.grid(column=3, row=3)

window.mainloop()