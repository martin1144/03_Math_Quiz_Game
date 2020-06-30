from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, partner):

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()

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
                                      font="Arial 19 bold", width=10)
        self.start_quiz_entry.grid(row=0, column=0)

        self.math_quiz_instruction = Label(self.start_frame, font="Arial 10 italic",
                                           text="Please choose a level below",
                                           wrap=180, justify=LEFT, padx=10, pady=10)
        self.math_quiz_instruction.grid(row=2, column=0)

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

    def to_quiz(self):
        get_quiz = Quiz(self)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()