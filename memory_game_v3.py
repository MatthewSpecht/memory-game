#Memory Game 

## goals: GUI allows player to matches up the 8 different buttons 
# with the other by selecting the buttons/image 
# computer deletes counts correct and wrong and delete cards after selecting a correct pair

#A simple memory game that employs GUI with 
#layout of 16 cards(revealing themselves after you press the button) 
#total with 8 different kind of card where the player trys to match up 
#the cards by selecting a pair of buttons based on memory


# create 16 buttons 
# give attributes of: each holds image, buttons
# give behaviors of: matching which partner image, show image when clicked



# pair and remove 
# show card if clicked card is shown and everytime we get a pair the pair is removed
# suceed in fewest amount of attempts 

#-----Tkinter Set up------
import tkinter as tk
class MemoryGame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        for row_num in range(4):
            for column_num in range(4):
                tk.Button(self, text='?', bg = 'Red', width = 10
                 
                ).grid(row=row_num, column=column_num, columnspan = 1, sticky = tk.W)

root = tk.Tk() 
root.title("Memory Game")
app = MemoryGame(root) 
root.mainloop()