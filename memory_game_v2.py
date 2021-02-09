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
import random
class MemoryGame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #rand_list = ["apple.png","banana.png","grape.png", "orange.png", "peach.png","strawberry.png","watermelon.png", "apple.png","banana.png","grape.png", "orange.png", "peach.png","strawberry.png","watermelon.png"]
        #rand_choose = random.randint(0,15)
        
        #btn = []
        i=0
        #for nums in range (1,17):
        for row_num in range(0, 4, 1):
            for column_num in range(0, 4, 1):
                    #btn.append(Button(width = 3, height=1,)
                #pict = tk.PhotoImage(file = "fruit-pictures/" + rand_list[rand_choose])
                result = tk.Button(self, text='?', bg = 'Red', width = 3, command = self.bttn_click
                 
                ).grid(row=row_num, column=column_num, columnspan = 1, sticky = tk.W)
                    #tk.btn[i].grid(row = row_num, column = column_num)
                    #i +=1

        #btn.mainloop()
    
    
    def bttn_click(self):
        rand_list = ["apple.png","banana.png","grape.png", "orange.png", "peach.png","pear.png","strawberry.png","watermelon.png", "apple.png","banana.png","grape.png", "orange.png", "pear.png","peach.png","strawberry.png","watermelon.png"]
        rand_choose = random.randint(0,15)
        photo = tk.PhotoImage(file = "fruit-pictures/" + rand_list[rand_choose])
        #return photo
        #photo_button 
        result = tk.Label(root, image = photo)
        #photo_button.img=photo
        #photo_button.pack()

# for creating card/button
# for nums in range(0,17)

#     Button(app, text = "")	
#     .grid()

root = tk.Tk() 
root.title("Memory Game")
#root.geometery('200x100')
app = MemoryGame(root) 
root.mainloop()
