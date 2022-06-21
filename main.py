import tkinter as tk
# create the window
window = tk.Tk()
window.geometry("600x600")
window.title("Employee TimeClock")
# create a title on screen
title = tk.Label(text="Employee TimeClock")
title.pack()
# create a text input for their employee ID
employee_id_input = tk.Entry(width=50)
employee_id_input.pack()


def process_clock(event):
    # when the card is read it automatically presses enter after, we hijack that here to run the rest of our code
    print(employee_id_input.get())
    # clear the input for the next person
    employee_id_input.delete(0, tk.END)


# hook into the "return" key to run the above function
window.bind('<Return>', process_clock)


# display the window and loop until closed
window.mainloop()
