from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Setting up the window
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("My Own TP Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Question canvas
        self.q_canvas = Canvas(width=300, height=250)
        # self.q_canvas.config(bg="white")

        self.question = self.q_canvas.create_text(
            150, 125, text="This will show a question", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.q_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(
            image=true_img, highlightthickness=0, border=0, command=self.pressed_true_btn)
        self.false_btn = Button(
            image=false_img, highlightthickness=0, border=0, command=self.pressed_false_btn)

        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.q_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.q_canvas.itemconfig(self.question, text=question)
        else:
            self.q_canvas.itemconfig(self.question, text="Game over")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def pressed_true_btn(self):
        self.give_user_feedback(self.quiz.check_answer("True"))

    def pressed_false_btn(self):
        self.give_user_feedback(self.quiz.check_answer("False"))

    def give_user_feedback(self, is_right):
        if is_right:
            self.q_canvas.config(bg="green")
        else:
            self.q_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
