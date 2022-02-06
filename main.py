from email.mime import image
from tkinter import *
import random

rnum = random.randint(0,3)
aichoos = rnum  
def prock():
    if aichoos == 1:
        print("its a Draw!")
        quit()
    elif aichoos == 2:
        print("You lost, Ai choosed Paper!")
        quit()
    else:
        print("You won, Ai choosed sissor!")
        quit()
    
def ppaper():
    if aichoos == 1:
        print("You won, Ai choosed rock!")
        quit()
    elif aichoos == 2:
        print("Its a draw!")
        quit()
    else:
        print("You lost, Ai choosed sissor")
        quit()
    
def psissor():
    if aichoos == 1:
        print("You lost , Ai choosed Rock!")
        quit()
    elif aichoos == 2:
        print("You won, Ai choosed Paper!")
        quit()
    else:
        print("Its a draw!")
        quit()
  
    
window = Tk()
rock = Button(window, text='Rock!')
rock.pack()
rock.config(command=prock)
paper = Button(window, text='paper!')
paper.pack()
paper.config(command=ppaper)
sissor = Button(window, text='Sissor')
sissor.pack()
sissor.config(command=psissor)
window.mainloop()
