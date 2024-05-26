from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, ques_brain: QuizBrain):
        self.quiz = ques_brain
        self.window = Tk()
        self.window.title("QuizGame")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

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
        self.true_button = Button(highlightthickness=0, image=self.correct_img, command=self.clicked_true)
        self.true_button.grid(column=0, row=2)

        self.wrong_img = PhotoImage(file='images/false.png')
        self.false_button = Button(highlightthickness=0, image=self.wrong_img, command=self.clicked_false)
        self.false_button.grid(column=1, row=2)

        self.get_nxt_question()

        self.window.mainloop()

    def get_nxt_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score : {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def clicked_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def clicked_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_nxt_question)
