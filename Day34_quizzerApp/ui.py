from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, ques_brain: QuizBrain):
        self.quiz = ques_brain
        self.window = Tk()
        self.window.title("QuizGame")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.correct_img = PhotoImage(file='images/true.png')
        self.true_button = Button(highlightthickness=0, image=self.correct_img)
        self.true_button.grid(column=0, row=2)

        self.wrong_img = PhotoImage(file='images/false.png')
        self.false_button = Button(highlightthickness=0, image=self.wrong_img)
        self.false_button.grid(column=1, row=2)

        self.get_nxt_question()

        self.window.mainloop()

    def get_nxt_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
