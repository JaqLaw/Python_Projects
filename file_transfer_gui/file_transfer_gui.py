
import tkinter
# import all widgets
from tkinter import *
from tkinter import filedialog
import shutil
import os


# create a child class (a window) inheriting the Tkinter built in class 'Frame'; 'master' refers to the Frame class
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(650, 275))
        self.master.title('File transfer app')
        self.master.config(bg='lightgrey')

        # use built in string variable class
        self.varDir1 = StringVar()
        self.varDir2 = StringVar()

        # configure the grid
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=1)


        # browse button 1
        self.btnBrowse = Button(self.master, text='Browse...', width=10, height=2, command=self.browse)
        self.btnBrowse.grid(row=0, column=0, padx=(0,0), pady=(60,0))

        # browse button 2
        self.btnBrowse2 = Button(self.master, text='Browse...', width=10, height=2, command=self.browse2)
        self.btnBrowse2.grid(row=1, column=0, padx=(0,0), pady=(20,0))

        # add a submit(check for files) button
        self.btnSubmit = Button(self.master, text='Check for files...', width=10, height=3, command=self.submit)
        self.btnSubmit.grid(row=2, column=0, padx=(0,0), pady=(20,0))



        # instantiate a text box using Entry widget, place it in self.master, set text,font and color
        self.txtFile1 = Entry(self.master, text=self.varDir1, font=("Helvetica", 16), fg='black')
        # paint the object above onto the window with a geometry manager(pack, grid, etc)
        self.txtFile1.grid(row=0, column=1, columnspan=3, padx=(10,30), pady=(60,0), sticky=EW)

        # instantiate a text box using Entry widget, place it in self.master, set text,font and color
        self.txtFile2 = Entry(self.master, text=self.varDir2, font=("Helvetica", 16), fg='black')
        # paint the object above onto the window with a geometry manager(pack, grid, etc)
        self.txtFile2.grid(row=1, column=1, columnspan=3, padx=(10,30), pady=(30,0), sticky=EW)


        # add a close button
        self.btnClose = Button(self.master, text='Close Program', width=10, height=3, command=self.close)
        self.btnClose.grid(row=2, column=3, padx=(0,30), pady=(20,0), sticky=NE)



    def submit(self):
        # check a folder for any new files or recently edited files and copy to another folder

        # get the user input source folder
        source = self.varDir1.get()+"/"

        # get the user input destination folder
        destination = self.varDir2.get()+"/"


        files_source = os.listdir(source)
        files_destination = os.listdir(destination)


        for i in files_source:
            # copy files that are new over
            if i not in files_destination:
                shutil.copy(source+i, destination)
            # check for updated files and if updated, replace older file
            if i in files_destination:
                modify_time_source = os.path.getmtime(source+i)
                modify_time_destination = os.path.getmtime(destination+i)
                if (modify_time_source > modify_time_destination):
                    shutil.copy(source+i, destination)
        

    def close(self):
        # destroy closes the window
        self.master.destroy()

    def browse(self):
        # browse for files
        dir1 = tkinter.filedialog.askdirectory()
        # just for checking: print(dir1)
        self.varDir1.set(dir1)

    def browse2(self):
        # browse for files
        dir2 = tkinter.filedialog.askdirectory()
        self.varDir2.set(dir2)


if __name__ == "__main__":
    # instantiate tkinter
    root = Tk()
    # pass it to our class
    App = ParentWindow(root)
    # without the following, it will immediately close, keep it alive with mainloop
    root.mainloop()
