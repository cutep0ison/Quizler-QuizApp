from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: 0", font=("Arial", 15), bg=THEME_COLOR, foreground="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.qus_text = self.canvas.create_text(150, 125, width=280, text="I Am Tonmay Poddar",
                                                font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=self.right, highlightthickness=0, bg=THEME_COLOR, command=self.right_ans)
        self.true_btn.grid(row=2, column=0)

        self.wrong = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=self.wrong, highlightthickness=0, bg=THEME_COLOR, command=self.wrong_ans)
        self.false_btn.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.qus_text, text=q_txt)
        else:
            self.canvas.itemconfig(self.qus_text, text=f"No Question Left\nFinal Score:{self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def right_ans(self):
        if self.quiz.check_answer(user_answer="True"):
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.window.after(1000, lambda: self.canvas.config(bg="white"))
        self.window.after(1000, func=self.get_next_question)
        self.score.config(text=f"Score: {self.quiz.score}")

    def wrong_ans(self):
        if self.quiz.check_answer(user_answer="False"):
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.window.after(1000, lambda: self.canvas.config(bg="white"))
        self.window.after(1000, func=self.get_next_question)
        self.score.config(text=f"Score: {self.quiz.score}")
