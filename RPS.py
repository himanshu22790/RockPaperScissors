from tkinter import *
from tkinter.ttk import Style
import random
from tkinter import messagebox

window = Tk()

choices = ['Rock','Paper','Scissors']
def rps():
    comp_choice=random.choice(choices)
    player_choice = entry1.get()
    pc_lower = player_choice.lower()
    cc_lower = comp_choice.lower()
    pc_caps = player_choice.capitalize()
    if entry1.get() == cc_lower:
        messagebox.showinfo("Result", "Your choice : " + pc_caps + "\nComputer chooses: " + comp_choice + "\n\nIts a tie!")
    elif((pc_lower == 'rock' and cc_lower == 'scissors') or (pc_lower == 'paper' and cc_lower == 'rock') or (pc_lower == 'scissors' and cc_lower == 'paper')):
        messagebox.showinfo("Result", "Your choice : " + pc_caps + "\n Computer chooses: " +
                            comp_choice + "\n \nYou Win!")
    elif((pc_lower == 'scissors' and cc_lower == 'rock') or (pc_lower == 'rock' and cc_lower == 'paper') or (pc_lower == 'paper' and cc_lower == 'scissors')):
        messagebox.showinfo("Result", "Your choice : " + pc_caps + "\nComputer chooses: " +
                            comp_choice + "\n\nComputer Wins!")
    else:
        messagebox.showinfo("Result", "Invalid Entry, please try again!")


window.title("RockPaperScissors")
window.geometry("430x150")
window.configure(bg='black')

label1 = Label(window, text = "Enter Rock/Paper/Scissors: ", bg='black', fg = 'yellow')
label1.grid(row=0,column=0)

label2 = Label(
    window, text="Rules: \nRock beats Scissors \n Scissors cut Paper \n Paper wraps Rock", bg='black', fg='yellow')
label2.grid(row=1, column=1)

label3 = Label(
    window, text="----------Created by Himanshu----------", bg='black', fg='yellow')
label3.grid(row=4, column=1)

mytext=StringVar()
entry1 = Entry(window,text=mytext,width=30,fg='yellow', bg='green')
entry1.grid(row=0,column=1)

button1= Button(window, text='Play', bg='black', fg='yellow', command=rps)
button1.grid(row=0,column=2)

window.mainloop()
