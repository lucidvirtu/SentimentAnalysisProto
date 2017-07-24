from tkinter import *
import main as mn

title_label = "Aplikasi Analisis Sentiment Twitter"
keyword_lbl = "Taip kata kunci carian ke dalam kotak carian"

def clex():
    exit()

root = Tk()
root.geometry("400x400")
root.title("TSA BM")

label1 = Label(root, text=title_label, fg="green")
label1.pack()
label2 = Label(root, text=keyword_lbl)
label2.pack()

logo = PhotoImage(file="twitter-logo.png")
label4 = Label(root, image=logo)
label4.pack()

label3 = Label(root, text="Kata Kunci:")
label3.pack()
keyword = Entry(root, bd=3)
keyword.pack()

def startop():
    a = keyword.get()
    mn.exec(a)



searchbtn = Button(root, text="Cari", command=startop)
searchbtn.pack()


root.mainloop()