import tkinter as tk

import random

root = tk.Tk() 
root.title("Memory Game")
# root.geometery("550x550")

matches = ["1","2","3","4","5","6","7","8"]*2
random.shuffle(matches)

my_frame = tk.Frame(root)
my_frame.pack(pady=10)
count = 0
answer_list = []
answer_dict ={} 
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def button_click(b, i):
    global count, answer_list, answer_dict
    if b["text"] == '' and count < 2:
        b["text"] = matches[i]

# b0= tk.Button(my_frame, text='?',  font=("Helvetica", 20), bg = 'Red', width = 20, height = 10, command = lambda: button_click(b0, 0)
#              ).grid(row=r, column=c, columnspan = 1, sticky = tk.W)    
        

for i in range(16):
    for r in range(4):
        for c in range(4):
                "b" + str(i) = tk.Button(my_frame, text='?',  font=("Helvetica", 20), bg = 'Red', width = 20, height = 10, command = lambda: button_click(b + str(i), i)
                ).grid(row=r, column=c, columnspan = 1, sticky = tk.W)   

                     



root.mainloop()