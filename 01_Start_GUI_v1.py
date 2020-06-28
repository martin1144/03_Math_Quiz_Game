from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, partner):

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.math_quiz_label = Label(self.start_frame, text="Math Quiz",
                                       font="Arial 24 bold", bg="yellow")
        self.math_quiz_label.grid(row=0, column=0, pady=10, padx=10)

        self.math_quiz_instruction = Label(self.start_frame, font="Arial 10 italic",
                                           text="Enter amount of questions you want between 1 to 10",
                                           wrap=180, justify=LEFT, padx=10, pady=10)
        self.math_quiz_instruction.grid(row=1)

        self.entry_error_frame = Frame(self.start_frame, width=200)
        self.entry_error_frame.grid(row=1, column=1)

        self.start_quiz_entry = Entry(self.entry_error_frame,
                                      font="Arial 19 bold", width=10)
        self.start_quiz_entry.grid(row=0, column=1)

        self.math_quiz_instruction = Label(self.start_frame, font="Arial 10 italic",
                                           text="Please choose a level below",
                                           wrap=180, justify=LEFT, padx=10, pady=1)
        self.math_quiz_instruction.grid(row=3, column=0)

        self.easy_button = Button(self.start_frame, text="Easy",
                                  pady=10, padx=10, width=10,
                                  bg="light blue",
                                  command=lambda: self.to_quiz)
        self.easy_button.grid(row=4, pady=5, column=0)

        self.medium_button = Button(self.start_frame, text="Medium",
                                    pady=10, padx=10,
                                    command=lambda: self.to_quiz)
        self.medium_button.grid(row=4, column=1)

        self.hard_button = Button(self.start_frame, text="Hard",
                                  pady=10, padx=10, width=10,
                                  bg="blue",
                                  command=lambda: self.to_quiz)
        self.hard_button.grid(row=4, column=2, pady=10)


    def to_quiz(self):
        get_quiz = Quiz(self)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()