from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.scoreboard = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.scoreboard.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280,text="Some question",fill=THEME_COLOR,font=("arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.right = PhotoImage(file="python/Quiz App/images/true.png")
        self.button_right = Button(image=self.right,highlightthickness=0,command=self.correct_button)
        self.button_right.grid(row=2,column=0)

        self.wrong = PhotoImage(file="python/Quiz App/images/false.png")
        self.button_wrong = Button(image=self.wrong,highlightthickness=0,command=self.wrong_button)
        self.button_wrong.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text= q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the limit")
            self.button_wrong.config(state="disabled")
            self.button_right.config(state="disabled")

    def correct_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def wrong_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")

        self.window.after(1000,self.get_next_question)