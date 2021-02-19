import tkinter as tk
from tkinter import messagebox
import random
from tkinter import PhotoImage 

root = tk.Tk() 
root.title("Memory Game")
# root.geometery("550x550")

images = [PhotoImage(file = "fruit-pictures/orange.png"),PhotoImage(file = "fruit-pictures/banana.png"),PhotoImage(file = "fruit-pictures/grape.png"), PhotoImage(file = "fruit-pictures/peach.png"),PhotoImage(file = "fruit-pictures/pear.png"),PhotoImage(file = "fruit-pictures/watermelon.png"),PhotoImage(file = "fruit-pictures/strawberry.png"),PhotoImage(file = "fruit-pictures/banana.gif")]
# images = [PhotoImage(file = "fruit-pictures/small_orange.gif")]*8
matches = [0,1,2,3,4,5,6,7]*2


random.shuffle(matches)

my_frame = tk.Frame(root)
my_frame.pack(pady=10)

count = 0
answer_list = []
answer_dict ={} 

def button_click(b, i):
    global count, answer_list, answer_dict
    if b["text"] == '?' and count < 2:
        b.configure(image = images[matches[i]])
        b.photo = images[matches[i]] #keep a refrence to it 

        # add num to answer list
        answer_list.append(i)
        # add button & num to answer dict
        answer_dict[b] = matches[i]
        #turn +1
        count+=1
        #print answer_list ##keeps track of tile
        #print answer_dict ##keeps track of num on tile

    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]: #direct comparison nums are fine objs not so much
            my_label.config(text="MATCH!")
            for key in answer_dict:
                key["state"] = "disabled"

            count = 0
            answer_list = []
            answer_dict = {}
        else:
            my_label.config(text="NO!")
            count = 0
            answer_list = []
            messagebox.showinfo("Incorrect!","Incorrect")
            

            for key in answer_dict:
                key.configure(text='?', image='')
                

            answer_dict = {}

def reset():
    global matches, winner

    matches = [1,2,3,4,5,6,7,8]*2
    random.shuffle(matches)
    my_label.config(text="") 

    # buttonlist = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]
    for button in grid_buttons:
        button.config(text='?', state="normal")


restart= tk.Button(my_frame, text='Restart', width= 6, height = 2, command = reset).grid(row=4, column=0, columnspan = 3, sticky = tk.W) 

# x = PhotoImage(file = "fruit-pictures/banana.png")

grid_buttons = []
index = 0
for r in range(4):
  for c in range(4):
    # created the button
    b = tk.Button(my_frame, text = '?',  font=("Helvetica", 10), bg = 'Red')

    # adding button to a list
    grid_buttons.append(b)

    # add button command
    grid_buttons[index].config(command = lambda b=grid_buttons[index], i=index: button_click(b, i)) # pass values for b and i into lambda function

    # button on grid
    grid_buttons[index].grid(row=r, column=c, columnspan = 1, sticky = tk.W)

    # increase index
    index+=1
            
my_label = tk.Label(root, text = ' ')
my_label.pack(pady = 20)




root.mainloop()