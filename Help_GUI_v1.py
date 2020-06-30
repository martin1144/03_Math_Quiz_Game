from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Start:
    def __init__(self, partner):

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Math Quiz Game Heading (row 0)
        self.math_quiz_label = Label(self.start_frame, text="Math Quiz Game",
                                     font="Arial 19 bold")
        self.math_quiz_label.grid(row=1)

        # Help button (row 2)
        self.help_button = Button(self.start_frame, text="Help/Rules",
                                  command=self.to_quiz)
        self.help_button.grid(row=2, pady=10)

    def to_quiz(self):
        get_help = Help(self)

class Help:
    def __init__(self, partner):

        # Disable help button
        partner.help_button.config(state=DISABLED)

        # Help Quiz
        self.help_quiz =Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_quiz.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Gui Frame
        self.help_frame = Frame(self.help_quiz, width=300)
        self.help_frame.grid()

        # Help Heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Rules",
                                 font="Arial 14 bold")
        self.how_heading.grid(row=0)

        help_text="Choose an amount of questions 1 to 10 then. " \
                  "choose a level that will be suitable for you. \n\n " \
                  "The levels are Easy, Medium, Hard. Easy will contain plus and " \
                  "minus, Medium will contain only multiplications and lastly Hard " \
                  "will contain Division and higher numbers that will make it. " \
                  "complicated for some users. " \

        # Help text (row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, font="Arial 15 bold", bg="maroon",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        partner.help_button.config(state=NORMAL)
        self.help_quiz.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()