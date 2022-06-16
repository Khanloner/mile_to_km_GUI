from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=300)
window.config(pady=80, padx=80)

def mile_to_km():
    mile_value = int(entry1.get())
    km_value = mile_value * 1.6
    result_label.config(text=km_value.__round__(2))

# Entry inputs
entry1 = Entry(width=10)
entry1.grid(row=0, column=1)



# Labels
mile_label = Label(text="Miles", font=("Arial", 11, "bold"))
mile_label.grid(row=0, column=2)

equal_label = Label(text="is equal to", font=("Arial", 11, "bold"))

equal_label.grid(row=1, column=0)

result_label = Label(text="0", font=("Arial", 11, "bold"))
result_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 11, "bold"))
km_label.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=mile_to_km)
button.grid(row=2, column=1)

window.mainloop()