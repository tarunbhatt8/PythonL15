'''
Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
'''
from tkinter import *

def display():
	hwL2.configure(text='you entered '+inputE.get()+' ', bg='blue',\
              font='Times 20 italic underline')


root = Tk()
root.title('My App')
root.configure(background='blue')

inputL = Label(root, text='Enter an Input: ')
inputL.grid(row=0, column=0)



inputE = Entry(root)
inputE.grid(row=0, column=1)

hwL1 = Label(root,text='Your output will be displayed here!', bg='blue')
hwL1.grid(row=1, column=0)


hwL2 = Label(root)
hwL2.grid(row=1, column=1)



              
submitB = Button(root, text='Submit Input', bg='green',\
                 activebackground='yellow', \
                 activeforeground='white',\
		 command=display)
submitB.grid(row=2, column=0)

exitB = Button(root, text='exit', width=25, \
               command=root.destroy)
exitB.grid(row=2, column=1)


root.mainloop()
