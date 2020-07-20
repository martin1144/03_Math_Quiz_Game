from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, partner):

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

        # Set questions to zero
        self.starting_questions = IntVar()
        self.starting_questions.set(1)

        # Quiz Heading (row 0)
        self.math_quiz_label = Label(self.start_frame, text="Math Quiz",
                                       font="Arial 30 bold", bg="yellow")
        self.math_quiz_label.grid(row=0, column=0, pady=10, padx=10)

        # Quiz Instruction (row 1)
        self.math_quiz_instruction = Label(self.start_frame, font="Arial 10 italic",
                                           text="Enter amount of questions you want between 1 to 10",
                                           wrap=180, justify=LEFT, padx=10, pady=10)
        self.math_quiz_instruction.grid(row=1)

        self.entry_error_frame = Frame(self.start_frame)
        self.entry_error_frame.grid(row=1, column=1)

        self.start_quiz_entry = Entry(self.entry_error_frame,
                                      font="Arial 19 bold", width=5)
        self.start_quiz_entry.grid(row=0, column=0)

        self.math_quiz_instruction = Label(self.start_frame, font="Arial 10 italic",
                                           text="Please choose a level below",
                                           wrap=180, justify=LEFT, padx=10, pady=10)
        self.math_quiz_instruction.grid(row=2, column=0)

        self.amount_error_label = Label(self.entry_error_frame, fg="maroon",
                                        text="", font="Arial 10 bold", wrap=275,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # Button Frame
        self.quiz_frame = Frame(self.start_frame)
        self.quiz_frame.grid(row=3)

        # light blue easy mode button
        self.easy_button = Button(self.quiz_frame, text="Easy",
                                  pady=10, padx=10, width=10,
                                  bg="light blue", fg="white",
                                  command=lambda: self.to_quiz)
        self.easy_button.grid(row=0, column=0, padx=5)

        # blue medium mode button
        self.medium_button = Button(self.quiz_frame, text="Medium",
                                    pady=10, padx=10, width=10,
                                    bg="blue", fg="white",
                                    command=lambda: self.to_quiz)
        self.medium_button.grid(row=0, column=1, padx=5)

        # dark blue hard mode button
        self.hard_button = Button(self.quiz_frame, text="Hard",
                                  pady=10, padx=10, width=10,
                                  bg="dark blue", fg="white",
                                  command=lambda: self.to_quiz)
        self.hard_button.grid(row=0, column=2, padx=5)

        # Help / Rules Button (row 4)
        self.help_button = Button(self.quiz_frame, text="Help / Rules",
                                  width=10, bg="light grey", font="arial 16 bold",
                                  command=self.to_help)
        self.help_button.grid(row=4, column=1, pady=20)

    def to_help(self):
        get_help = Help(self)

    def to_quiz(self, levels):
        get_quiz = Quiz(self, levels)

        try:
            number_of_questions = int(number_of_questions)

            if number_of_questions < 1:
                has_errors = "yes"
                error_feedback = "Sorry but you can't go below 1" \

            elif number_of_questions > 10:
                has_errors = "yes"
                error_feedback = "You can go higher than 10!" \

        except ValueError:
            has_errors = "yes"
            error_feedback = "Enter a number 1 to 10 (no decimals / text)"

        if has_errors == "yes":
            self.start_quiz_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            # Set number of questions to amount entered by user
            self.starting_questions.set(number_of_questions)

        def to_Quiz(self, levels):

            # Retrieve number of questions
            number_of_questions = self.starting_questions.get()

            Game(self, levels, number_of_questions)

            # hide start up window
            root.withdraw()



class Quiz:
    def __init__(self, number_of_questions, levels):
        print(number_of_questions)
        print(levels)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()