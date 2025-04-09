from tkinter import *

def miles_to_km():
    miles = miles_input.get()

    if miles != 0:
        calc = float(miles) * 1.609
        km_text.config(text=f"{calc}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

km_text = Label(text= "0")
km_text.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()