
from tkinter import * 
from PIL import ImageTk, Image
import  random

class Game:
    def __init__(self, window):
        self.window = window
        self.window.title('Rock Paper Scissors Game')
        self.window.geometry('900x680+300+10')
        self.window.configure(bg='light sea green')
        self.window.resizable(False,False)
        
        #canvas  for displaying images and background
        self.canvas = Canvas(self.window, width=900, height=680, bg="light sea green", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=6, rowspan=6, sticky='ew')
        
        #labels
        self.lbl1 = Label(window, text='Player', font=('Rosewood Std Fill', 24), bg='spring green')
        self.lbl2 = Label(window, text='Vs', font=('Helvetica', 35),bg='light sea green',fg='dark violet')
        self.lbl3 = Label(window, text='Computer', font=('Rosewood Std Fill', 24), bg='spring green')
        self.lbl_msg= Label(window,text = 'Press a button', font=('Helvetica', 32), bg='dark turquoise',fg='white')
        self.lbl_userScore= Label(window,text = 0, font=('Helvetica', 30), fg='white',bg = "light sea green")
        self.lbl_botScore=  Label(window,text = 0, font=('Helvetica', 30),fg='white',bg = "light sea green")
        #grid layout
        self.lbl_msg.grid(row = 3, column=2, columnspan=2,rowspan=3,  padx=10, pady=10)
        self.lbl1.grid(row=0, column=0, columnspan=2, sticky='ew')
        self.lbl2.grid(row=0, column=2, columnspan=2,padx=10, pady=10, sticky='ew')
        self.lbl3.grid(row=0, column=4, columnspan=2, padx=10, pady=10, sticky='ew')
        self.lbl_userScore.grid(row = 2, column=1, columnspan=3,rowspan=3,  padx=20, pady=20)
        self.lbl_botScore.grid(row = 2, column=2, columnspan=3,rowspan=3,  padx=20, pady=20)
        
        #set of buttons
        self.rock_btn= Button(window,text='Rock', width=12, height=3, bg='yellow',command=lambda:self.update_choice("rock"), activebackground='light sea green',font=('Times', 22, 'bold'))
        self.paper_btn= Button(window,text='Paper', width=12, height=3, bg='cyan', command=lambda:self.update_choice("paper"), activebackground='light sea green',font=('Times', 22, 'bold'))
        self.scissor_btn= Button(window,text='Scissor', width=12, height=3, bg='pink', command=lambda:self.update_choice("scissor"),  activebackground='light sea green',font=('Times', 22, 'bold'))
        #grid layout
        self.rock_btn.grid(row = 4, column=0, columnspan=2, rowspan=3, padx=10, pady=10)
        self.paper_btn.grid(row = 4, column=2, columnspan=2,rowspan=3, padx=10, pady=10)
        self.scissor_btn.grid(row = 4, column=4, columnspan=2,rowspan=3,  padx=10, pady=10)

        # Loading images to put on canvas
        self.load_images()
        
   
    def load_images(self):  
        """
        Loads images for the game.
        """
        # images directories
        rock_img = Image.open('images/rock.png').resize((300, 300))
        paper_img = Image.open('images/paper.png').resize((300, 300))
        scissor_img = Image.open('images/scissor.png').resize((300, 300))
        question_img = Image.open("images/question.png").resize((280, 280))

        self.rock_s = ImageTk.PhotoImage(rock_img)
        self.paper_s = ImageTk.PhotoImage(paper_img)
        self.scissor_s = ImageTk.PhotoImage(scissor_img)
        self.img_p = ImageTk.PhotoImage(question_img)
        self.img_c = ImageTk.PhotoImage(question_img.transpose(Image.FLIP_LEFT_RIGHT))
        
        #canvas for question mark image
        self.canvas.create_image(0, 100, anchor=NW, image=self.img_p)
        self.canvas.create_image(600, 100, anchor=NW, image=self.img_c)
    
    
    def update_user_score(self):
        """
        Updates the user's score and ends the game when it reaches 5 points.
        """
        score = int(self.lbl_userScore["text"])
        score += 1
        self.lbl_userScore["text"] = str(score)
        if score == 5:
            self.display_result("Player won!     ")
            self.change_buttons_state(DISABLED)
            #set all the buttons to DISABLED state
            
    def update_bot_score(self):
        """
        Updates the computer's score and checks for game end.
        """
        score = int(self.lbl_botScore["text"])
        score += 1
        self.lbl_botScore["text"] = str(score)
        if score == 5:
            self.display_result("Computer won!")
            self.change_buttons_state(DISABLED)
            #set all the buttons to DISABLED state
    
    
    def display_result(self, message):
        """
        Displays the game result in a pop-up window.
        """
        sub_window = Toplevel(self.window)
        sub_window.geometry("340x250+600+200")
        sub_window.title("Game over")

        lbl_message = Label(sub_window, text=message, font=('Helvetica', 21), bg='dark sea green', fg='white')
        lbl_message.grid(row=0, column=4, pady=20, sticky='ew')

        restart_btn = Button(sub_window, text='Restart', width=8, height=2, bg='orange', command=lambda: self.restart(sub_window), activebackground='light sea green', font=('Times', 10, 'bold'), fg='white')
        restart_btn.grid(row=5, column=3, padx=3, pady=5)

        quit_btn = Button(sub_window, text='Quit', width=8, height=2, bg='red', command=lambda: self.window.destroy(), activebackground='light sea green', font=('Times', 10, 'bold'), fg='white')
        quit_btn.grid(row=5, column=5, padx=3, pady=5)

        lbl_results = Label(sub_window, text='Results:', font=('Modern', 19), fg='dark orange', bg='sea green')
        lbl_results.grid(row=2, column=4, sticky="nsew")

        lbl_botScore_res = Label(sub_window, text='Computer: ' + self.lbl_botScore["text"], font=('Helvetica', 14), bg='light grey')
        lbl_botScore_res.grid(row=3, column=4, pady=5, sticky="nsew")

        lbl_userScore_res = Label(sub_window, text='Player: ' + self.lbl_userScore["text"], font=('Helvetica', 14), bg='ghost white')
        lbl_userScore_res.grid(row=4, column=4, pady=5, sticky="nsew")

        sub_window.resizable(False, False)
        sub_window.configure(bg='sea green')
        sub_window.protocol("WM_DELETE_WINDOW", lambda: self.window.destroy())

     
    def change_buttons_state(self, state):
        """
        Changes the state of buttons.
        """
        self.rock_btn.configure(state=state)
        self.paper_btn.configure(state=state)
        self.scissor_btn.configure(state=state)
        
    
    def update_message(self, choice, computer_choice):
        """
        Updates the game message label based on the user's and computer's choices.
        """
        if (choice == "paper" and computer_choice == "rock") or (choice == "rock" and computer_choice == "scissor") or (choice == "scissor" and computer_choice == "paper"):
            self.lbl_msg["text"] = "You win"
            self.update_user_score()
        elif (choice == "rock" and computer_choice == "paper") or (choice == "scissor" and computer_choice == "rock") or (choice == "paper" and computer_choice == "scissor"):
            self.lbl_msg["text"] = "You lose"
            self.update_bot_score()
        else:
            self.lbl_msg["text"] = "You tie"
    
    def update_choice(self, choice):
        """
        Updates the game based on the user's choice.
        """
        choices = ['rock', 'paper', 'scissor']
        computer_choice = random.choice(choices)
        
        #deletes previous images to avoid overloading 
        self.canvas.delete("item")
        
        # Loads user and computer images based on choices
        user_image = None
        computer_image = None

        if choice == "rock":
            user_image = self.rock_s
            self.lbl1.configure(bg='yellow')
        elif choice == "paper":
            user_image = self.paper_s
            self.lbl1.configure(bg='cyan')
        else:
            user_image = self.scissor_s
            self.lbl1.configure(bg='pink')

        if computer_choice == "rock":
            computer_image = self.rock_s
            self.lbl3.configure(bg='yellow')
        elif computer_choice == "paper":
            computer_image = self.paper_s
            self.lbl3.configure(bg='cyan')
        else:
            computer_image = self.scissor_s
            self.lbl3.configure(bg='pink')
        # display images on canvas for both
        self.canvas.create_image(0, 100, anchor=NW, image=user_image, tags="item")
        self.canvas.create_image(600, 100, anchor=NW, image=computer_image, tags="item")
        
        #updating game message
        self.update_message(choice, computer_choice)
        
       
    def restart(self, window):
        """
        Restarts the game by resetting scores and UI elements state.
        """
        self.change_buttons_state(NORMAL)
        self.lbl_botScore["text"] = str(0)
        self.lbl_userScore["text"] = str(0)
        self.lbl_msg["text"] = 'Press a button'
        window.destroy()
        
     
    def run(self):
        #runs the window
        self.window.mainloop()
#Main
if __name__ == '__main__':
    window = Tk()
    game = Game(window)
    game.run()


















    
    
