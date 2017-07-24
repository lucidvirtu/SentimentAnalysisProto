from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("B.Melayu TSA Visualizer")

        self.pack(fill=BOTH, expand=1)

        testbtn = Button(self, text="TestBtn", command=self.client_exit)

        testbtn.place(x=100, y=100)

    def client_exit(self):
        exit()

root = Tk() #root window
root.geometry("200x200")
app = Window(root)
root.mainloop()
