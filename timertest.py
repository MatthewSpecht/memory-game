from tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.pack()
time = 60
def tick():
    canvas.delete(ALL)
    global time
    time -= 1
    canvas.create_text(10, 10, text=time)
    if time == 0:
        time == 60
        # add resetting, perhaps a loss screen here when time == 0
    else:
        canvas.after(1000, tick)
canvas.after(1, tick)
root.mainloop()