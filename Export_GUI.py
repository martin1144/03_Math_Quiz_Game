from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Export:
    def __init__(self, partner, low_amount, high_amount, questions_played, how_many_right, history_questions):
        print(low_amount, high_amount, questions_played, how_many_right)
        print(history_questions)

        background_color = "#8589FF"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Set up child window (ie: export box)
        self.export_box = Toplevel()

        # If user press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background_color)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                 text="Export", fg="black",
                                 font="arial 20 bold", bg=background_color)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                                         "in the box below "
                                                         "below to save your "
                                                         "game history ",

                                 font="arial 13 italic",
                                 justify=LEFT, width=50, bg=background_color, wrap=200)
        self.export_text.grid(row=1)

        # Help text (label, row 1)
        self.history_label = Label(self.export_frame, text="The low number had: {}""\n"
                                                           "The high number had: {}""\n"
                                                           "you have played {} around""\n"
                                                           "you got {} correct out of {}  ""\n"
                                   .format(low_amount, high_amount, questions_played, how_many_right, questions_played),
                                   font="arial 13 italic",
                                   justify=LEFT, width=50, bg=background_color, wrap=200)
        self.history_label.grid(row=2)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                                         "you enter below "
                                                         "already exists, "
                                                         "its contents will "
                                                         "be replaced with "
                                                         "your game "
                                                         "history",
                                 justify=LEFT, bg="#8589FF", fg="black",
                                 font="arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=3, pady=10)

        # filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="arial 14 bold")
        self.filename_entry.grid(row=4, pady=10)

        # error massage labels (initially blank, row 4 )
        self.save_error_label = Label(self.export_frame, text=" ", fg="black",
                                      bg="#8589FF")
        self.save_error_label.grid(row=5)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=6, pady=10)

        # Save and Cancel buttons 9row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="arial 10 bold", fg="black",
                                  bg="maroon", padx=10, pady=10,
                                  command=partial(lambda: self.save_history(partner, low_amount, high_amount,
                                                                            questions_played, how_many_right,
                                                                            history_questions)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="arial 10 bold", fg="black",
                                    bg="white", padx=10, pady=10,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)


    def save_history(self, partner, low_amount, high_amount, questions_played, how_many_right, history_questions):
        # Regular expression to check filename is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            f.write("the low number was: {}""\n".format(low_amount))
            f.write("the high number was: {}""\n".format(high_amount))
            f.write("played {} throughout""\n".format(questions_played))
            f.write("you got {} correct out of {}  ""\n".format(how_many_right, questions_played))
            f.write("{} ""\n".format(history_questions))

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)


    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Quiz")
    something = Start(root)
    root.mainloop()