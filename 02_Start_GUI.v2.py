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
        self.math_quiz_instruction.grid(row=1, column=0)

        self.entry_error_frame = Frame(self.start_frame)
        self.entry_error_frame.grid(row=1, column=1)

        # Quiz Entry Box
        self.start_quiz_entry = Entry(self.entry_error_frame,
                                      font="Arial 19 bold", width=5)
        self.start_quiz_entry.grid(row=0, column=0)

        self.math_quiz_instruction = Label(self.start_frame, font="Arial 10 italic",
                                           text="Please choose a level below",
                                           wrap=180, justify=LEFT, padx=10, pady=10)
        self.math_quiz_instruction.grid(row=2, column=0)

        self.amount_error_label = Label(self.start_frame, fg="maroon",
                                        text="", font="Arial 10 bold",
                                        justify=LEFT)
        self.amount_error_label.grid(row=2, column=1)

        # Button Frame
        self.quiz_frame = Frame(self.start_frame,)
        self.quiz_frame.grid(row=3)

        # light blue easy mode button
        self.easy_button = Button(self.quiz_frame, text="Easy",
                                  pady=10, padx=10, width=10,
                                  bg="light blue", fg="white",
                                  command=lambda: self.to_quiz(1))
        self.easy_button.grid(row=0, column=0, padx=5)

        # blue medium mode button
        self.medium_button = Button(self.quiz_frame, text="Medium",
                                    pady=10, padx=10, width=10,
                                    bg="blue", fg="white",
                                    command=lambda: self.to_quiz(2))
        self.medium_button.grid(row=0, column=1, padx=5)

        # dark blue hard mode button
        self.hard_button = Button(self.quiz_frame, text="Hard",
                                  pady=10, padx=10, width=10,
                                  bg="dark blue", fg="white",
                                  command=lambda: self.to_quiz(3))
        self.hard_button.grid(row=0, column=2, padx=5)

        # Help / Rules Button (row 4)
        self.help_button = Button(self.quiz_frame, text="Help / Rules",
                                  width=10, bg="light grey", font="arial 16 bold",
                                  command=self.to_quiz)
        self.help_button.grid(row=4, column=1, pady=20)

    def check_levels(self):
        number_of_questions = self.start_quiz_entry.get()

        error_back = "#ffafaf"
        has_errors = "no"

        self.start_quiz_entry.config(bg="white")
        self.amount_error_label.config(text="red")

        try:
            number_of_questions = int(number_of_questions)

            if number_of_questions < 1:
                has_errors = "yes"
                error_feedback = "Sorry but you can't go below 1" \

            elif number_of_questions > 10:
                has_errors = "yes"
                error_feedback = "You can't go higher than 10!" \

        except ValueError:
            has_errors = "yes"
            error_feedback = "Enter a number 1 to 10 (no decimals / text)"

        if has_errors == "yes":
            self.start_quiz_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)
            print(error_feedback)

        else:
            # Set number of questions to amount entered by user
            self.starting_questions.set(number_of_questions)
            return "yes"

    def to_quiz(self, levels):

            input_ok = "no"
            # check input...
            input_ok = self.check_levels()

            if input_ok == "yes":

                # Retrieve number of questions
                number_of_questions = self.starting_questions.get()

                Quiz(self, levels, number_of_questions)

                # hide start up window
                root.withdraw()


class Quiz:
    def __init__(self, partner, number_of_questions, levels):
        print(number_of_questions)
        print(levels)


        # initialise variables
        self.numbers = IntVar()
        # Set number of questions to amount entered by user at the start
        self.numbers.set(number_of_questions)

        # GUI setup
        self.quiz_box = Toplevel()
        self.quiz_frame = Frame(self.quiz_box)
        self.quiz_frame.grid()

        # Heading row
        self.heading_label = Label(self.quiz_frame, text="Quiz/Easy Mode",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instruction label
        self.instruction_label = Label(self.quiz_frame, wrap=300, justify=LEFT,
                                       text="Good Luck and Have Fun!",
                                       font="Arial 10", padx=10, pady=10)
        self.instruction_label.grid(row=1)

        self.entry_error_frame = Frame(self.quiz_frame)
        self.entry_error_frame.grid(row=2, column=0)

        self.game_quiz_entry = Entry(self.entry_error_frame,
                                     font="Arial 19 bold", width=5)
        self.game_quiz_entry.grid(row=2, column=0)

        # Next button
        self.next_button = Button(self.quiz_frame,
                                   font="Arial 12 bold",
                                   text="Next")
        self.next_button.grid(row=3, column=0, pady=10)

        # Check button
        self.check_button = Button(self.quiz_frame,
                                   font="Arial 12 bold",
                                   text="Check")
        self.check_button.grid(row=2, column=1)

        # Game Stats Button
        self.game_stats__button = Button(self.quiz_frame,
                                    font="Arial 12 bold",
                                    text="Game Stats")
        self.game_stats__button.grid(row=3, column=1)






















# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()