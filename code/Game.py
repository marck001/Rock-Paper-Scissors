
from tkinter import * 
from PIL import ImageTk, Image
import  random

window = Tk()
 
window.title('Rock Paper Scissor Game')
 
window.geometry('800x680+300+10')

canvas = Canvas(window, width=800, height=680,bg = "light sea green",highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=6, rowspan=6)

lbl1 = Label(window, text='Player', font=('Algerian', 25))

lbl2 = Label(window, text='Vs', font=('Algerian', 30))
lbl3 = Label(window, text='Computer', font=('Algerian', 25))
lbl_msg= Label(window,text = 'Text', font=('Algerian', 30))
lbl1.grid(row=0, column=0, columnspan=2,padx=10, pady=10, sticky='ew')
lbl2.grid(row=0, column=2, columnspan=2,padx=10, pady=10, sticky='ew')
lbl3.grid(row=0, column=4, columnspan=2, padx=10, pady=10, sticky='ew')
lbl_msg.grid(row = 3, column=2, columnspan=2,rowspan=3,  padx=10, pady=10)
rock_btn= Button(window,text='Rock', width=12, height=3, bg='orange',command=lambda:update_choice("rock"), activebackground='light sea green',font=('Times', 20, 'bold')).grid(row = 4, column=0, columnspan=2, rowspan=3, padx=10, pady=10)
paper_btn= Button(window,text='Paper', width=12, height=3, bg='green', command=lambda:update_choice("paper"), activebackground='light sea green',font=('Times', 20, 'bold')).grid(row = 4, column=2, columnspan=2,rowspan=3, padx=10, pady=10)
scissor_btn= Button(window,text='Scissor', width=12, height=3, bg='pink', command=lambda:update_choice("scissor"),  activebackground='light sea green',font=('Times', 20, 'bold')).grid(row = 4, column=4, columnspan=2,rowspan=3,  padx=10, pady=10)

rock_img= Image.open('images/rock.png')
rock_img = rock_img.resize((300, 300))

paper_img = Image.open('images/paper.png')
paper_img = paper_img.resize((300, 300))
# Loading images to put on canvas

scissor_img = Image.open('images/scissor.png')
scissor_img = scissor_img.resize((300, 300))

rock_s = ImageTk.PhotoImage(rock_img)
paper_s = ImageTk.PhotoImage(paper_img)
scissor_s = ImageTk.PhotoImage(scissor_img)

img_p = Image.open("images/question.png")
img_p = img_p.resize((300, 300))
 
# Flipping image from left to right
img_c = img_p.transpose(Image.FLIP_LEFT_RIGHT)
 
# Loading images to put on canvas
img_p = ImageTk.PhotoImage(img_p)
img_c = ImageTk.PhotoImage(img_c)

#canvas

#choice_wins

canvas.create_image(0, 100, anchor=NW, image=img_p)
canvas.create_image(500, 100, anchor=NW, image=img_c)

#update message
       
def update_message(choice,computer_choice):
    if ((choice == "paper" and computer_choice == "rock") or
    (choice == "rock" and computer_choice == "scissor") or
    (choice == "scissor" and computer_choice =="paper")):
        lbl_msg["text"] = "You win"
    elif((choice == "rock" and computer_choice == "paper") or
    (choice == "scissor" and computer_choice == "rock") or
    (choice == "paper" and computer_choice =="scissor")):
        lbl_msg["text"] = "You lost"
    else:
        lbl_msg["text"] = "You tie"

def update_choice(choice):
    choices=['rock','paper','scissor']
    computer_choice = random.choice(choices)
    #user
    if(choice == "rock"):
        canvas.create_image(0, 100, anchor=NW, image=rock_s)
    elif(choice == "paper"):
        canvas.create_image(0, 100, anchor=NW, image=paper_s)
    else:
        canvas.create_image(0, 100, anchor=NW, image=scissor_s)
    #computer user
    if(computer_choice == "rock"):
        canvas.create_image(500, 100, anchor=NW, image=rock_s)
    elif(computer_choice == "paper"):
        canvas.create_image(500, 100, anchor=NW, image=paper_s)
    else:
        canvas.create_image(500, 100, anchor=NW, image=scissor_s)   
    update_message(choice,computer_choice)
window.resizable(False,False)
window.mainloop()


















    
    