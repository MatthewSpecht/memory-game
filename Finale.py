import tkinter as tk
from tkinter import messagebox
import random
from tkinter import PhotoImage 

root = tk.Tk() 
root.title("Memory Game")
# root.geometery("550x550")


images = [PhotoImage(file = "small_fruits/small_orange.gif"),PhotoImage(file = "small_fruits/small_grape.gif"), 
PhotoImage(file = "small_fruits/small_peach.gif"),PhotoImage(file = "small_fruits/smol_pear.gif"),
PhotoImage(file = "small_fruits/small_watermelon.gif"),PhotoImage(file = "small_fruits/small_strawberry.gif"),PhotoImage(file = "small_fruits/small_banana.gif"), PhotoImage(file = "small_fruits/small_apple.gif")]
# images = [PhotoImage(file = "small_fruits/small_orange.gif")]*8
matches = [0,1,2,3,4,5,6,7]*2


random.shuffle(matches)

my_frame = tk.Frame(root)
my_frame.pack(pady=10)

count = 0
answer_list = []
answer_dict ={} 

def button_click(b, i):
    global count, answer_list, answer_dict

    # check if button was already pressed, if yes, just return (do nothing)
    if i in answer_list:
      return

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
        my_label.config(text=" ")
        if matches[answer_list[0]] == matches[answer_list[1]]: #direct comparison nums are fine objs not so much
            my_label.config(text="MATCH!")
            for key in answer_dict:
                key["state"] = "disabled"

            count = 0
            answer_list = []
            answer_dict = {}
        else:
            count = 0
            answer_list = []
            messagebox.showinfo("Incorrect!","Incorrect")
            

            for key in answer_dict:
                key.configure(text='?', image='')
                

            answer_dict = {}

def reset():
    global matches, winner, time, minute

    matches = [1,2,3,4,5,6,7,8]*2
    random.shuffle(matches)
    my_label.config(text="") 

    # buttonlist = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]
    for button in grid_buttons:
        button.config(text='?', state="normal", image ='')

    canvas.delete(tk.ALL)
    minute = 0
    time = 0
    # timer = canvas.create_text(100,100, text= "Minutes: 0 Seconds: 0")

        


restart= tk.Button(my_frame, text='Restart', width= 6, height = 2, command = reset).grid(row=4, column=0, columnspan = 3, sticky = tk.W) 

# x = PhotoImage(file = "small_fruits/banana.gif")

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
# canvas = tk.Canvas(root)
# canvas.pack()
# time = 0
# minute = 0

# def tick():
#     canvas.delete(tk.ALL)
#     global minute
#     global time
#     time += 1
#     timer = canvas.create_text(100,100, text= "Minutes: " + str(minute) + " Seconds:" + str(time))
#     #canvas.move(0,0,0)

#     if time == 60:
#         time = 0
#         minute+=1
#         canvas.after(1000, tick)
#         # add resetting, perhaps a loss screen here when time == 0
#     else:
#         canvas.after(1000, tick)
# canvas.after(1, tick)

# my_menu = Menu(root)
# root.config(menu=my_menu)

# option_menu = Menu(my_menu, tearoff=False)
# my_menu.add_cascade(Label = "Options", menu=option_menu) 
# option_menu.add_command(Label = "Fruits", command=fruit_deck)


root.mainloop()