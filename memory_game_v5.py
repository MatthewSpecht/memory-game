import tkinter as tk
import random
class MemoryGame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        for row_num in range(0, 4, 1):
            for column_num in range(0, 4, 1):
                 tk.Button(self, text='?', bg = 'Red', width = 3, command = self.bttn_click
                          ).grid(row=row_num, column=column_num, columnspan = 1, sticky = tk.W)
    
    def bttn_click(self):
        rand_list = ["apple.png","banana.png","grape.png", "orange.png", "peach.png","pear.png","strawberry.png","watermelon.png", "apple.png","banana.png","grape.png", "orange.png", "pear.png","peach.png","strawberry.png","watermelon.png"]
        rand_choose = random.randint(0,15)
        photo = tk.PhotoImage(file = "fruit-pictures/" + rand_list[rand_choose])
        tk.Label(self, image = photo)



root = tk.Tk() 
root.title("Memory Game")
#root.geometery('200x100')
app = MemoryGame(root) 
root.mainloop()
