import tkinter

screen = tkinter.Tk()
entry = tkinter.Entry(screen, width=50, bg="aquamarine", borderwidth=5)
entry.insert(0, "Enter your name")
entry.pack()

button = tkinter.Button(text="Submit", command=lambda: tkinter.Label(text=entry.get()).pack())
button.pack()
screen.mainloop()
