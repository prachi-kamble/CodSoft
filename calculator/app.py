import tkinter as tk


def press_key(key):
    if key == "=" or key == "Return":  
        try:
            result = eval(entry.get())  
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif key == "C" or key == "Escape": 
        entry.delete(0, tk.END)
    elif key in "0123456789+-*/().":  
        entry.insert(tk.END, key)
    elif key == "BackSpace":  
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])


def center_window(window, width=340, height=450):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")


def on_key(event):
    press_key(event.keysym)


root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
center_window(root) 


BACKGROUND_COLOR = "#121212"  
BUTTON_COLOR = "#1e1e1e"     
BUTTON_ACTIVE = "#333333"     
OPERATOR_COLOR = "#00acc1"   
CLEAR_COLOR = "#ff5252"       
EQUALS_COLOR = "#ff9800"     
TEXT_COLOR = "#ffffff"        
INPUT_BG = "#000000"          
INPUT_FG = "#dcdcdc"          


PADDING = 10


root.configure(bg=BACKGROUND_COLOR)


entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid",
                 justify="right", bg=INPUT_BG, fg=INPUT_FG, insertbackground=TEXT_COLOR)
entry.grid(row=0, column=0, columnspan=4, padx=PADDING, pady=PADDING, ipadx=5, ipady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]


for text, row, col in buttons:
    color = BUTTON_COLOR
    fg_color = TEXT_COLOR  

    if text in "+-*/":
        color = OPERATOR_COLOR  
    elif text == "C":
        color = CLEAR_COLOR  
    elif text == "=":
        color = EQUALS_COLOR  

    button = tk.Button(
        root, text=text, font=("Arial", 18), bg=color, fg=fg_color,
        activebackground=BUTTON_ACTIVE, activeforeground=TEXT_COLOR,
        command=lambda t=text: press_key(t), relief="raised", borderwidth=2
    )
    button.grid(row=row, column=col, ipadx=10, ipady=10, padx=PADDING, pady=PADDING)


root.bind("<Key>", on_key)


root.mainloop()
