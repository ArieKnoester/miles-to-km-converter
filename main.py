from tkinter import *


def convert_miles_to_km():
    miles = float(user_input.get())
    km = miles * 1.609344
    km_value_label.config(text=km)


window = Tk()
window.minsize(width=200, height=100)
window.title("Miles to Kilometer Converter")
window.config(padx=10, pady=10)

user_input = Entry(width=10)
user_input.grid(row=0, column=1)

miles_label = Label(text="Miles", padx=5, pady=5)
miles_label.grid(row=0, column=2)

equals_label = Label(text="is equal to", padx=5, pady=5)
equals_label.grid(row=1, column=-0)

km_value_label = Label(text=0)
km_value_label.grid(row=1, column=1)

km_label = Label(text="Km", padx=5, pady=5)
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
