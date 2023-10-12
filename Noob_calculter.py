import tkinter as tk

def on_button_click(event):
    # type_input
    user_input = entry.get()

    try:
        # part_calculate
        result = eval(user_input)
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Someting wrong: " + str(e))

# window menu
window = tk.Tk()
window.title("Calculater")
window.geometry("300x275")

# input_filed
entry = tk.Entry(window)
entry.pack()

# Enter button
calculate_button = tk.Button(window, text="Enter")
calculate_button.pack()
calculate_button.bind("<Button-1>", on_button_click)

# show rs
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
