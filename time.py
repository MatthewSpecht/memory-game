import tkinter as tk
from random import randrange

root = tk.Tk()

x = 0
def timer():
    global x
    if x < 30:
        new_time = time.get() + 1
        time.set(new_time)
        root.after(1000, timer) # call this function again in 1,000 milliseconds
        x += 1

def moveButton():
    b.place(x=randrange(10,470),y=randrange(10,470))

frame = tk.Frame(root, width=500, height=500)
frame.pack()

time = tk.IntVar()
time.set(0)

timer_display = tk.Label(root, textvar= time)
timer_display.place(x= 250, y= 5, anchor = tk.CENTER)

b = tk.Button(root, width=3, height=1, bg= "red", command=moveButton)
b.place(x=randrange(10,470), y= randrange(10,470))

timer() # start the timer

tk.mainloop()