from tkinter import *
class MemoryGame(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        #btn = []
        i=0
        #for nums in range (1,17):
        for row_num in range(0, 4, 1):
            for column_num in range(0, 4, 1):
                    #btn.append(Button(width = 3, height=1,)
                Button(self, text='?', bg = 'Red', width = 20, height = 10
                 
                ).grid(row=row_num, column=column_num, columnspan = 1, sticky = W)
                    #tk.btn[i].grid(row = row_num, column = column_num)
                    #i +=1

        #btn.mainloop()

        # card_list=[apple.png, banana.png, grape.png, orange.png, peach.png, pear.png, strawberry.png]*2
        
        # random.shuffle(card_list)

        # for c in card_list:
        #     Button["text"]=card_list[c]


# for creating card/button
# for nums in range(0,17)

#     Button(app, text = "")	
#     .grid()

root = Tk() 
root.title("Memory Game")
#root.geometery('200x100')
app = MemoryGame(root) 
root.mainloop()