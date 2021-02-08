import tkinter as tk
import random

class MemoryGame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.card_list=["apple.png","banana.png","grape.png","orange.png","peach.png","pear.png","strawberry.png"]*2


    def create_widgets(self):

        #btn = []
        #for nums in range (1,17):
        for row_num in range(0, 4, 1):
            for column_num in range(0, 4, 1):
                    #btn.append(Button(width = 3, height=1,)
                tk.Button(self, text='?', bg = 'Red', width = 20, height = 10
                 
                ).grid(row=row_num, column=column_num, columnspan = 1, sticky = tk.W)
                    #tk.btn[i].grid(row = row_num, column = column_num)
                    #i +=1

        #btn.mainloop()        
        random.shuffle(self.card_list)

        for fruit in self.card_list:
            for r in row_num:
                for c in column_num:
        # images = tk.Button(file="images/" + x.small_image);
                    w=tk.Label (self,image = fruit)
                    w.photo = fruit
                    w.grid(row=r,column=c)

        


# for creating card/button
# for nums in range(0,17)

#     Button(app, text = "")	
#     .grid()

root = tk.Tk() 
root.title("Memory Game")
#root.geometery('200x100')
app = MemoryGame(root) 
root.mainloop()