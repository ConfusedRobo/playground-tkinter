import tkinter

screen = tkinter.Tk()
screen.title("Standard Calculator")
buttons = {
    "operations": {
        "add": tkinter.Button(screen, padx=10, pady=10),
        "subtract": tkinter.Button(screen, padx=10, pady=10),
        "divide": tkinter.Button(screen, padx=10, pady=10),
        "product": tkinter.Button(screen, padx=10, pady=10),
    },
    "digits": {
        "one": tkinter.Button(screen, padx=10, pady=10),
        "two": tkinter.Button(screen, padx=10, pady=10),
        "three": tkinter.Button(screen, padx=10, pady=10),
        "four": tkinter.Button(screen, padx=10, pady=10),
        "five": tkinter.Button(screen, padx=10, pady=10),
        "six": tkinter.Button(screen, padx=10, pady=10),
        "seven": tkinter.Button(screen, padx=10, pady=10),
        "eight": tkinter.Button(screen, padx=10, pady=10),
        "nine": tkinter.Button(screen, padx=10, pady=10),
        "zero": tkinter.Button(screen, padx=10, pady=10)
    }
}

entry = tkinter.Entry(screen, width=50, borderwidth=5)
entry.grid(row=0, column=0)
screen.mainloop()
