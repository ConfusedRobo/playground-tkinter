import tkinter

screen = tkinter.Tk("buttons")
button1 = tkinter.Button(text="Click Me!", padx=50, pady=50, command=lambda: tkinter.Label(text="HI!").pack())
button2 = tkinter.Button(text="Click Me?", command=lambda: tkinter.Label(text="HI?").pack(), fg="blue", bg="#ccc")

button1.pack()
button2.pack()
screen.mainloop()
