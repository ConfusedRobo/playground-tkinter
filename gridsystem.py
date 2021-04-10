import tkinter

root = tkinter.Tk()
label1 = tkinter.Label(root, text="Hello, World!")
label2 = tkinter.Label(root, text="Hi! there")
# label1.pack()
label1.grid(column=0, row=0)  # columnspan, rowspan is also allowed
label2.grid(column=0, row=1)
root.mainloop()
