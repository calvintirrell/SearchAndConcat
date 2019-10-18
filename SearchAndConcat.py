import os
import pandas as pd
import csv
from tkinter import *
from tkinter import messagebox

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("Search and Append")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # label describing the Run button
        runLabel = Label(self, text="Click me to Run the script")
        runLabel.pack()
        runLabel.place(x=100, y=125)

        # the Run button and it's attributes
        runButton = Button(self, text="Run", command=self.search_concat)
        runButton.place(x=50, y=125)

        # label describing the Run button
        quitLabel = Label(self, text="Click me to Quit the program")
        quitLabel.pack()
        quitLabel.place(x=100, y=150)

        # the Quit button and it's attributes
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=50, y=150)

    # function to find and join specific CSV files into 1 master file
    def search_concat(self):

        # indicates current working directory (where this script is located)
        dir = '.'

        # counts the number of found CSV files to be joined
        file_counter = 0

        # save the files into a list for use later
        all_file_names = []

        # search through the file path
        for subdir, dirs, files in os.walk(dir):

            # for each file found
            for file in files:

                # each file needs to start with 'simulated' and ends with '.csv'
                if file.startswith('Pokemon') and file.endswith('.csv'):

                    # displays file location and name
                    print(os.path.join(subdir, file))

                    # for each correct file found add 1 to file_counter
                    file_counter += 1

                    # print file name and the specific file count number
                    print(file + ' ' + str(file_counter))

                    # append files found to all_files_names list
                    all_file_names.append(os.path.join(subdir, file))

        # combine all the CSV files from the all_file_names list
        combined_csv = pd.concat([pd.read_csv(f) for f in all_file_names])

        # from the master list of CSV file data, make this a single CSV file called 'consolidated'
        combined_csv.to_csv('consolidated.csv', index=False, encoding='utf-8-sig')

        # once everything is done a pop up box displays the message below
        messagebox.showinfo("Good News", "All good to go. Feel free to exit now.")

    # close the program function
    def client_exit(self):
        exit()

root = Tk()

# size of the window
root.geometry("300x300")

app = Window(root)
root.mainloop()
