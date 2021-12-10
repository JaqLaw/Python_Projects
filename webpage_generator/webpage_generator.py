import webbrowser
import os

import tkinter
# import all widgets
from tkinter import *


#original code for making and displaying a simple html page
"""
# the text to go in the file
text = '''
<html>
    <body>
        <h1>
    Stay tuned for our amazing summer sale!
        </h1>
    </body>
</html>
'''

# create a new file
f = open("webpage.html", "w")

# write the text to the file
f.write(text)

# close the file
f.close()

# open in webbrowser
webbrowser.open("file://" + os.path.realpath("webpage.html"))
"""




# create a child class (a window) inheriting the Tkinter built in class 'Frame'; 'master' refers to the Frame class
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 500))
        self.master.title('Make your own web page!')
        self.master.config(bg='darkgrey')


        # configure the grid
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=1)
        root.columnconfigure(4, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=1)
        root.rowconfigure(4, weight=1)
        root.rowconfigure(5, weight=1)


        #Define the text box with a scrollbar and grid them
        self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.txtHtml1 = Text(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.txtHtml1.yview)
        self.scrollbar1.grid(row=0,column=5,rowspan=5,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+W+S)
        self.txtHtml1.grid(row=0,column=0,rowspan=5,columnspan=5,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

        # add a submit button
        self.btnSubmit = Button(self.master, text='Submit', width=5, height=2, command=self.submit)
        self.btnSubmit.grid(row=10, column=2, padx=(0,0), pady=(0,30), sticky=NE)

        # add a cancel button
        self.btnCancel = Button(self.master, text='Cancel', width=5, height=2, command=self.cancel)
        self.btnCancel.grid(row=10, column=1, padx=(0,0), pady=(0,30), sticky=NE)

    def submit(self):
        # get the user input from the text box
        html = self.txtHtml1.get("1.0",END)
        # create a new file with user input, if file exists, overwrite
        f = open("webpage.html", "w")
        # write the text to the file
        f.write(html)
        # close the file
        f.close()
        # open in webbrowser
        webbrowser.open("file://" + os.path.realpath("webpage.html"))
        

    def cancel(self):
        # destroy closes the window
        self.master.destroy()




if __name__ == "__main__":
    # instantiate tkinter
    root = Tk()
    # pass it to our class
    App = ParentWindow(root)
    # without the following, it will immediately close, keep it alive with mainloop
    root.mainloop()
