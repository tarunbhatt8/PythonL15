'''
Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.
'''

from tkinter import *

def display():
	hwL1.configure(text='Wollla!!! This Text Got Changed!!', bg='blue',\
              font='Times 20 italic underline')
	

root = Tk()
root.title('My App')
root.configure(background='blue')

hwL1 = Label(root)

hwL1.configure(text='This is some text!!', bg='blue',\
              font='Times 20 italic underline')

changetB = Button(root, text='Chnage Text', bg='green',\
                 activebackground='yellow', \
                 activeforeground='white',\
		 command=display)
exitB = Button(root, text='exit', width=25, \
               command=root.destroy)

hwL1.pack()
changetB.pack()
exitB.pack()
root.mainloop()
