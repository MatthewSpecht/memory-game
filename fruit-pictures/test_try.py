from tkinter import *
import random

# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        #self.rand_list = ["apple.png","banana.png","grape.png", "orange.png", "peach.png","pear.png","strawberry.png","watermelon.png", "apple.png","banana.png","grape.png", "orange.png", "pear.png","peach.png","strawberry.png","watermelon.png"]
        #self.rand_choose = random.randint(0,15)
        self.remember = []
        self.guess = 0
        for self.row_num in range(0, 4, 1):
            for self.column_num in range(0, 4, 1):
                 sample = Button(self, text='?', width = 3, command = self.pict
                          ).grid(row=self.row_num, column=self.column_num, columnspan = 1, sticky = W)
        #sample = Image.open("pear.png")
        #pear = ImageTk.PhotoImage(sample)
        #sample = Button(self,text = "?", command = self.pict).grid(row=0,column = 0)
        #sample.image = pear
        #sample.place(x=1, y=0)
        #Button(self, text = "?" , image = sample.image)
    def pict(self):
        rand_list = ["apple.png","banana.png","grape.png", "orange.png", "peach.png","pear.png","strawberry.png","watermelon.png", "apple.png","banana.png","grape.png", "orange.png", "pear.png","peach.png","strawberry.png","watermelon.png"]
        rand_choose = random.randint(0,15)
        remember1 = rand_list[rand_choose]
        self.remember.append(remember1)
        sample = Image.open(remember1)
        pear = ImageTk.PhotoImage(sample)

        sample = Button(self,text = "?",image = pear)
        sample.image = pear
        #sample.grid(row=self.row_num, column=self.column_num, columnspan = 1, sticky = W)
        sample.grid(row=5, column=5, columnspan = 1, sticky = W)
        self.guess += 1
        if self.guess == 2:
            if self.remember[0] == self.remember[1]:
                Label(self,text = "You found a match!").grid(row=6,column=5)
            else:
                Label(self,text = "You did not find a match! Keep trying!!!").grid(row=6,column=5)
                
            self.guess = 0
                
        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("200x120")
root.mainloop()