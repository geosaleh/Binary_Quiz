
# Follow Us On Twitter @PY4ALL

# Import required libraries
from tkinter import *
import tkinter as tk
import random


# Main Class
class gui(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent.title('Binary Quiz')
        parent.resizable(False, False)
        parent.configure(background = 'white')
        self.canvas =  tk.Canvas(parent, width=800, height=500, bg='white')
        self.canvas.pack(fill="both", expand=True)
        self.int = random.randint(0,255)
        self.txt_int_in = self.canvas.create_text(400,100,font='Times 40 bold',text=str(self.int), fill='blue', anchor=CENTER)
        self.txt_int = self.canvas.create_text(400,450,font='Times 40 bold',text=str(0), fill='blue', anchor=CENTER)
        self.txt_bin = self.canvas.create_text(400,400,font='Times 40 bold',text='00000000', fill='blue', anchor=CENTER)
        self.score = 0
        self.score_txt = f"Score : {self.score}"
        self.txt_score_txt = self.canvas.create_text(750,30,font='Times 12 bold',text=self.score_txt, fill='blue', anchor=CENTER)
        

        # load and resize bulb image
        self.bulb_on = PhotoImage(file="images/Bulb_on.png")
        self.bulb_off = PhotoImage(file="images/Bulb_off.png")
        self.bulb_on = self.bulb_on.subsample(8)
        self.bulb_off = self.bulb_off.subsample(8)
        self.bulb_on_all = []
        self.bulb_off_all = []

        # Create 8 images to represent 8 bits
        for i in range(8):
            self.bulb_on_all.append( self.canvas.create_image(50+((7-i)*100),250, anchor=CENTER, image=self.bulb_on) )
            self.bulb_off_all.append( self.canvas.create_image(50+((7-i)*100),250, anchor=CENTER, image=self.bulb_off) )
            self.hideitem(self.bulb_on_all[i])
            self.canvas.create_text(50+((7-i)*100),350,font='Times 12 bold',text=f'{2**i}', fill='blue', anchor=CENTER)

        self.binary = [0,0,0,0,0,0,0,0]
        # connect each bulb image with switch method
        self.canvas.tag_bind(self.bulb_on_all[0], "<Button-1>", lambda x: self.switch(self.bulb_on_all[0], self.bulb_off_all[0],0,0))
        self.canvas.tag_bind(self.bulb_off_all[0], "<Button-1>", lambda x: self.switch(self.bulb_off_all[0], self.bulb_on_all[0],0,1))
        self.canvas.tag_bind(self.bulb_on_all[1], "<Button-1>", lambda x: self.switch(self.bulb_on_all[1], self.bulb_off_all[1],1,0))
        self.canvas.tag_bind(self.bulb_off_all[1], "<Button-1>", lambda x: self.switch(self.bulb_off_all[1], self.bulb_on_all[1],1,1))
        self.canvas.tag_bind(self.bulb_on_all[2], "<Button-1>", lambda x: self.switch(self.bulb_on_all[2], self.bulb_off_all[2],2,0))
        self.canvas.tag_bind(self.bulb_off_all[2], "<Button-1>", lambda x: self.switch(self.bulb_off_all[2], self.bulb_on_all[2],2,1))
        self.canvas.tag_bind(self.bulb_on_all[3], "<Button-1>", lambda x: self.switch(self.bulb_on_all[3], self.bulb_off_all[3],3,0))
        self.canvas.tag_bind(self.bulb_off_all[3], "<Button-1>", lambda x: self.switch(self.bulb_off_all[3], self.bulb_on_all[3],3,1))
        self.canvas.tag_bind(self.bulb_on_all[4], "<Button-1>", lambda x: self.switch(self.bulb_on_all[4], self.bulb_off_all[4],4,0))
        self.canvas.tag_bind(self.bulb_off_all[4], "<Button-1>", lambda x: self.switch(self.bulb_off_all[4], self.bulb_on_all[4],4,1))
        self.canvas.tag_bind(self.bulb_on_all[5], "<Button-1>", lambda x: self.switch(self.bulb_on_all[5], self.bulb_off_all[5],5,0))
        self.canvas.tag_bind(self.bulb_off_all[5], "<Button-1>", lambda x: self.switch(self.bulb_off_all[5], self.bulb_on_all[5],5,1))
        self.canvas.tag_bind(self.bulb_on_all[6], "<Button-1>", lambda x: self.switch(self.bulb_on_all[6], self.bulb_off_all[6],6,0))
        self.canvas.tag_bind(self.bulb_off_all[6], "<Button-1>", lambda x: self.switch(self.bulb_off_all[6], self.bulb_on_all[6],6,1))
        self.canvas.tag_bind(self.bulb_on_all[7], "<Button-1>", lambda x: self.switch(self.bulb_on_all[7], self.bulb_off_all[7],7,0))
        self.canvas.tag_bind(self.bulb_off_all[7], "<Button-1>", lambda x: self.switch(self.bulb_off_all[7], self.bulb_on_all[7],7,1))
        
    # hide selected item
    def hideitem(self, item):
        self.canvas.itemconfigure(item, state='hidden')

    # show selected item
    def showitem(self, item):
        self.canvas.itemconfigure(item, state='normal')

    
    def switch(self, item1, item2, loc, val):
        self.hideitem(item1)
        self.showitem(item2)

        # Update binary value
        self.binary[7-loc] = val
        self.bin = ''.join(map(str, self.binary))

        # check if user get the correct number
        if int(self.bin,2) == self.int:
            self.canvas.itemconfig(self.txt_bin, text=self.bin,fill='green')
            self.canvas.itemconfig(self.txt_int, text=str(int(self.bin,2)),fill='green')
            self.int = random.randint(0,255)
            self.canvas.itemconfig(self.txt_int_in, text=self.int)
            self.score += 1
            self.score_txt = f"Score : {self.score}"
            self.canvas.itemconfig(self.txt_score_txt, text=self.score_txt)
        else:
            self.canvas.itemconfig(self.txt_bin, text=self.bin,fill='red')
            self.canvas.itemconfig(self.txt_int, text=str(int(self.bin,2)),fill='red')

         
    
if __name__ == "__main__":
    root = tk.Tk()
    gui(root)
    root.mainloop()
