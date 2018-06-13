'''
Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
'''
from tkinter import *

def display():
	hwL2.configure(text='Submitted!!', bg='blue',\
              font='Times 20 italic underline')
	

root = Tk()
root.title('My App')
root.configure(background='blue')

hwL1 = Label(root)
hwL2 = Label(root)

hwL1.configure(text='Hello World!!', bg='blue',\
              font='Times 25 bold underline')

submitB = Button(root, text='Submit', bg='green',\
                 activebackground='yellow', \
                 activeforeground='white',\
		 command=display)
exitB = Button(root, text='exit', width=25, \
               command=root.destroy)

hwL1.pack()
hwL2.pack()
submitB.pack()
exitB.pack()
root.mainloop()
