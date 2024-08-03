import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root,width=100,height=100)
canvas.pack()
circle = canvas.create_oval(50,50,80,80,outline="white",fill="blue")

def redraw():
    canvas.after(50,redraw)
    canvas.move(circle,155,155)
    print(canvas.coords(circle))
root.mainloop()