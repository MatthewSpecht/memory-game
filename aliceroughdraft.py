import tkinter as tk
from tkinter import messagebox
import random
from tkinter import PhotoImage 

root = tk.Tk() 
root.title("Memory Game")
# root.geometery("550x550")

# matches = [PhotoImage(file = "fruit-pictures/apple.png"),PhotoImage(file = "fruit-pictures/orange.png"),PhotoImage(file = "fruit-pictures/banana.png"),PhotoImage(file = "fruit-pictures/grape.png"), PhotoImage(file = "fruit-pictures/peach.png"),PhotoImage(file = "fruit-pictures/pear.png"),PhotoImage(file = "fruit-pictures/watermelon.png"),PhotoImage(file = "fruit-pictures/strawberry.png")]*2
matches = [PhotoImage(file = "fruit-pictures/banana.png")]*16

random.shuffle(matches)

my_frame = tk.Frame(root)
my_frame.pack(pady=10)
count = 0
answer_list = []
answer_dict ={} 

def button_click(b, i):
    global count, answer_list, answer_dict
    if b["text"] == '?' and count < 2:
        b.configure(image = matches[i])
        b.photo = matches[i] #keep a refrence to it 

        # add num to answer list
        answer_list.append(i)
        # add button & num to answer dict
        answer_dict[b] = matches[i]
        #turn +1
        count+=1
        #print answer_list ##keeps track of tile
        #print answer_dict ##keeps track of num on tile

    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
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
                key["text"] = '?'
                key.configure(image='')
                

            answer_dict = {}

def reset():
    global matches, winner

    matches = [1,2,3,4,5,6,7,8]*2
    random.shuffle(matches)
    my_label.config(text="") 

    buttonlist = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]
    for button in buttonlist:
        button.config(text='?', state="normal")


restart= tk.Button(my_frame, text='Restart', width= 6, height = 2, command = reset).grid(row=4, column=0, columnspan = 1, sticky = tk.W) 

x = PhotoImage(file = "fruit-pictures/banana.png")

b0= tk.Button(my_frame, image = x,  font=("Helvetica", 10), bg = 'Red', command = lambda: button_click(b0, 0))
b1= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red',  command = lambda: button_click(b1, 1))
b2= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b2, 2))
b3= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b3, 3))

b4= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b4, 4))
b5= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b5, 5))
b6= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b6, 6))
b7= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b7, 7))

b8= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b8, 8))
b9= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b9, 9))
b10= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b10, 10))
b11= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b11, 11))

b12= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b12, 12))
b13= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b13, 13))
b14= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b14, 14))
b15= tk.Button(my_frame, text='?',  font=("Helvetica", 10), bg = 'Red', width = 10, height = 5, command = lambda: button_click(b15, 15))


b0.grid(row=0, column=0, columnspan = 1, sticky = tk.W)             
b1.grid(row=0, column=1, columnspan = 1, sticky = tk.W)             
b2.grid(row=0, column=2, columnspan = 1, sticky = tk.W)             
b3.grid(row=0, column=3, columnspan = 1, sticky = tk.W)             

b4.grid(row=1, column=0, columnspan = 1, sticky = tk.W)             
b5.grid(row=1, column=1, columnspan = 1, sticky = tk.W)             
b6.grid(row=1, column=2, columnspan = 1, sticky = tk.W)             
b7.grid(row=1, column=3, columnspan = 1, sticky = tk.W)             

b8.grid(row=2, column=0, columnspan = 1, sticky = tk.W)             
b9.grid(row=2, column=1, columnspan = 1, sticky = tk.W)             
b10.grid(row=2, column=2, columnspan = 1, sticky = tk.W)             
b11.grid(row=2, column=3, columnspan = 1, sticky = tk.W)             

b12.grid(row=3, column=0, columnspan = 1, sticky = tk.W)             
b13.grid(row=3, column=1, columnspan = 1, sticky = tk.W)             
b14.grid(row=3, column=2, columnspan = 1, sticky = tk.W)             
b15.grid(row=3, column=3, columnspan = 1, sticky = tk.W)             

                     
my_label = tk.Label(root, text = ' ')
my_label.pack(pady = 20)




root.mainloop()