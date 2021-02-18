import tkinter as tk
from tkinter import messagebox
import random
from tkinter import PhotoImage 

class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.img = PhotoImage(file="fruit-pictures/banana.png")

        self.grid()
        self.create_widgets()

    def create_widgets(self):

        label = tk.Label(self, image = self.img)
        label.img = self.img

        label.grid()

        tk.Label(self,text="hi").grid()


root = tk.Tk() 
root.title("Memory Game")
Application(root)
root.mainloop()