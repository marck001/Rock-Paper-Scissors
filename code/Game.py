
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
lbl_userScore= Label(window,text = 0, font=('Helvetica', 30), fg='white',bg = "light sea green")
lbl_botScore=  Label(window,text = 0, font=('Helvetica', 30),fg='white',bg = "light sea green")
#labels grid
lbl_msg.grid(row = 3, column=2, columnspan=2,rowspan=3,  padx=10, pady=10)
lbl1.grid(row=0, column=0, columnspan=2,padx=10, pady=10, sticky='ew')
lbl2.grid(row=0, column=2, columnspan=2,padx=10, pady=10, sticky='ew')
lbl3.grid(row=0, column=4, columnspan=2, padx=10, pady=10, sticky='ew')
lbl_userScore.grid(row = 2, column=1, columnspan=3,rowspan=3,  padx=20, pady=20)
lbl_botScore.grid(row = 2, column=2, columnspan=3,rowspan=3,  padx=20, pady=20)

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


#updates score for user
def update_user_score():
    score = int(lbl_userScore["text"])
    score+=1
    lbl_userScore["text"] = str(score)
        
    if(score==5):
        display_result("Player won!     ")
        change_buttons_state(DISABLED)
            
#updates score for computer                         
def update_bot_score():
    score = int(lbl_botScore["text"])
    score +=1
    lbl_botScore["text"] = str(score)
        
    if(score==5):
        display_result("Computer won!")
        change_buttons_state(DISABLED)
#creates an inner window        
def display_result(message):
        sub_window = Toplevel(window)
        sub_window.geometry("340x250+600+200")
        sub_window.title("Game over")

        lbl_message = Label(sub_window, text=message, font=('Helvetica', 21), bg='dark sea green', fg='white')
        lbl_message.grid(row=0, column=4, pady=20, sticky='ew')

        restart_btn = Button(sub_window, text='Restart', width=8, height=2, bg='orange', command=lambda: restart(sub_window), activebackground='light sea green', font=('Times', 10, 'bold'), fg='white')
        restart_btn.grid(row=5, column=3, padx=3, pady=5)

        quit_btn = Button(sub_window, text='Quit', width=8, height=2, bg='red', command=lambda: window.destroy(), activebackground='light sea green', font=('Times', 10, 'bold'), fg='white')
        quit_btn.grid(row=5, column=5, padx=3, pady=5)

        lbl_results = Label(sub_window, text='Results:', font=('Modern', 19), fg='dark orange', bg='sea green')
        lbl_results.grid(row=2, column=4, sticky="nsew")

        lbl_botScore_res = Label(sub_window, text='Computer: ' + lbl_botScore["text"], font=('Helvetica', 14), bg='light grey')
        lbl_botScore_res.grid(row=3, column=4, pady=5, sticky="nsew")

        lbl_userScore_res = Label(sub_window, text='Player: ' + lbl_userScore["text"], font=('Helvetica', 14), bg='ghost white')
        lbl_userScore_res.grid(row=4, column=4, pady=5, sticky="nsew")

        sub_window.resizable(False, False)
        sub_window.configure(bg='sea green')
        sub_window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())
    
 #Changes the state of buttons  
def change_buttons_state(sta):
    rock_btn.configure(state=sta)
    paper_btn.configure(state=sta)
    scissor_btn.configure(state=sta)            

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
    
    user_image = None
    computer_image = None
    #canva images for user
    if(choice == "rock"):
        user_image = rock_s
        lbl1.configure(bg='yellow')
    elif(choice == "paper"):
        user_image = paper_s
        lbl1.configure(bg='cyan')
    else:
        user_image = scissor_s
        lbl1.configure(bg='pink')
    # canva images for computer 
    if(computer_choice == "rock"):
        computer_image = rock_s
        lbl3.configure(bg='yellow')
    elif(computer_choice == "paper"):
        computer_image = paper_s
        lbl3.configure(bg='cyan')
    else:
        computer_image = scissor_s
        lbl3.configure(bg='pink')
     
    #draw canvas for both   
    canvas.create_image(0, 100, anchor=NW, image=user_image, tags="item")
    canvas.create_image(600, 100, anchor=NW, image=computer_image, tags="item")
 
    update_message(choice,computer_choice)

 def restart(window):
    change_buttons_state(NORMAL)
    lbl_botScore["text"] = str(0)
    lbl_userScore["text"] = str(0)
    lbl_msg["text"] = 'Play again'
    window.destroy()
 
window.resizable(False,False)
window.configure(bg='light sea green')
window.mainloop()


















    
    
