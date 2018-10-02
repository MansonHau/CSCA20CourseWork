from tkinter import *

class Window(Frame):
    

    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
        self.init_window()
        self.fluff_count = 0
        self.state = False
    
    def init_window(self):
        self.master.title('The Fluff Counter')
        
        self.pack(fill = BOTH, expand = 1)
        
        countButton = Button(self, text = 'Uh... ', 
                             command = self.count_the_fluff)
        
        countButton.place(x = 175, y = 60)
        
        displayButton = Button(self, text = 'Display Results', 
                             command = self.display_results)
        
        displayButton.place(x = 150, y = 90)
        
        clearButton = Button(self, text = 'Reset', 
                             command = self.clear)
        
        clearButton.place(x = 175, y = 120)        

   
    def count_the_fluff(self):
            
        self.fluff_count = self.fluff_count + 1


    def display_results(self):

        self.text = Label(self, text = str(self.fluff_count) + ' fluff words said.')
        self.text.pack()
        
    def clear(self):
        self.text.destroy()
        self.fluff_count = 0
                    
root = Tk()

root.geometry('400x400')

app = Window(root)

root.mainloop()
