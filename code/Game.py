
from tkinter import * 
from PIL import ImageTk, Image
import  random

window = Tk()
 
window.title('Rock Paper Scissor Game')
 
window.geometry('900x680+300+10')

canvas = Canvas(window, width=900, height=680,bg = "light sea green",highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=6, rowspan=6)

#main labels
lbl1 = Label(window, text='Player', font=('Rosewood Std Fill', 24), bg='spring green')
lbl2 = Label(window, text='Vs', font=('Helvetica', 35),bg='light sea green',fg='dark violet')
lbl3 = Label(window, text='Computer', font=('Rosewood Std Fill', 24), bg='spring green')
lbl_msg= Label(window,text = 'Press a button', font=('Helvetica', 32), bg='spring green',fg='white')
#labels grid
lbl_msg.grid(row = 3, column=2, columnspan=2,rowspan=3,  padx=10, pady=10)
lbl1.grid(row=0, column=0, columnspan=2,padx=10, pady=10, sticky='ew')
lbl2.grid(row=0, column=2, columnspan=2,padx=10, pady=10, sticky='ew')
lbl3.grid(row=0, column=4, columnspan=2, padx=10, pady=10, sticky='ew')


#buttons
rock_btn= Button(window,text='Rock', width=12, height=3, bg='yellow',command=lambda:update_choice("rock"), activebackground='light sea green',font=('Times', 20, 'bold'))
paper_btn= Button(window,text='Paper', width=12, height=3, bg='cyan', command=lambda:update_choice("paper"), activebackground='light sea green',font=('Times', 20, 'bold'))
scissor_btn= Button(window,text='Scissor', width=12, height=3, bg='pink', command=lambda:update_choice("scissor"),  activebackground='light sea green',font=('Times', 20, 'bold'))

rock_btn.grid(row = 4, column=0, columnspan=2, rowspan=3, padx=10, pady=10)
paper_btn.grid(row = 4, column=2, columnspan=2,rowspan=3, padx=10, pady=10)
scissor_btn.grid(row = 4, column=4, columnspan=2,rowspan=3,  padx=10, pady=10)

# set of images to put on canvas
rock_img= Image.open('images/rock.png')
rock_img = rock_img.resize((300, 300))
paper_img = Image.open('images/paper.png')
paper_img = paper_img.resize((300, 300))
scissor_img = Image.open('images/scissor.png')
scissor_img = scissor_img.resize((300, 300))
question_img = Image.open("images/question.png")
question_img = question_img .resize((280, 280))

rock_s = ImageTk.PhotoImage(rock_img)
paper_s = ImageTk.PhotoImage(paper_img)
scissor_s = ImageTk.PhotoImage(scissor_img)

# Flipping image from left to right
img_c = question_img.transpose(Image.FLIP_LEFT_RIGHT)
 
# Loading images to put on canvas
img_p = ImageTk.PhotoImage(question_img)
img_c = ImageTk.PhotoImage(img_c)

#canvas for question mark image
canvas.create_image(0, 100, anchor=NW, image=img_p)
canvas.create_image(600, 100, anchor=NW, image=img_c)

#updates message      
def update_message(choice,computer_choice):
    if ((choice == "paper" and computer_choice == "rock") or
    (choice == "rock" and computer_choice == "scissor") or
    (choice == "scissor" and computer_choice =="paper")):
        lbl_msg["text"] = "You win"
    elif((choice == "rock" and computer_choice == "paper") or
    (choice == "scissor" and computer_choice == "rock") or
    (choice == "paper" and computer_choice =="scissor")):
        lbl_msg["text"] = "You loose"
    else:
        lbl_msg["text"] = "You tie"

def update_choice(choice):
    choices=['rock','paper','scissor']
    computer_choice = random.choice(choices)
 
    #deletes previous images to avoid overloading
    canvas.delete("item")
    
     #Creates canva images for user
    if(choice == "rock"):
        canvas.create_image(0, 100, anchor=NW, image=rock_s, tags="item")
        lbl1.configure(bg='yellow')
    elif(choice == "paper"):
        canvas.create_image(0, 100, anchor=NW, image=paper_s, tags="item")
        lbl1.configure(bg='cyan')
    else:
        canvas.create_image(0, 100, anchor=NW, image=scissor_s, tags="item")
        lbl1.configure(bg='pink')
     #Creates canva images for computer
    if(computer_choice == "rock"):
        canvas.create_image(600, 100, anchor=NW, image=rock_s, tags="item")
        lbl3.configure(bg='yellow')
    elif(computer_choice == "paper"):
        canvas.create_image(600, 100, anchor=NW, image=paper_s, tags="item")
        lbl3.configure(bg='cyan')
    else:
        canvas.create_image(600, 100, anchor=NW, image=scissor_s, tags="item")
        lbl3.configure(bg='pink') 
    update_message(choice,computer_choice)
 
window.resizable(False,False)
window.configure(bg='light sea green')
window.mainloop()


















    
    
