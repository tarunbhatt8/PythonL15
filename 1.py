'''
Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
'''


from tkinter import *

root = Tk()
root.title('My App')
root.configure(background='blue')

hwL = Label(root)

hwL.configure(text='Hello World!!', bg='blue',\
              font='Times 25 bold underline')

exitB = Button(root, text='exit', width=25, \
               command=root.destroy)
hwL.pack()

exitB.pack()

root.mainloop()
