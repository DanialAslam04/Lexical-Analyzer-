from tkinter import *
import LA as la

root = Tk()
root.title('Lexical Analyzer')
root.geometry('2000x2000')
root.config(bg='#fff8d6')

frame1 = Frame(root, padx=10)
frame1.pack(side=LEFT, anchor="w")

frame2 = Frame(root, padx=10)
frame2.pack(side=RIGHT, anchor="e")

frame3 = Frame(root, padx=10)
frame3.pack(side=BOTTOM, anchor="s")

mainlb=Label(root, text="............    Lexical Analyzer    ............", font=(74),borderwidth=14,background='#fff8d6', relief="ridge")
mainlb.place(x = 510, y = 10) 
   
inputlb=Label(frame1, text="... I N P U T ...", font=(74),borderwidth=8,background='#ffffff', relief="ridge")
inputlb.pack(padx=2, pady=2)

outputlb=Label(frame2, text="... O U T P U T ...", font=(74),borderwidth=8,background='#ffffff', relief="ridge")
outputlb.pack(padx=2, pady=2)

tb1 = Text(frame1, height=25, width=70)#, yscrollcommand=v1.set)
tb1.pack(side=LEFT, padx=20, pady=15)

tb2 = Text(frame2, height=25, width=70)#, yscrollcommand=v2.set)
tb2.pack(side=RIGHT, padx=30, pady=15, expand=1, fill=BOTH)
#text_box2.insert(INSERT, m.tokens[i])
def openfile():
    la.file()
    tb1.insert(INSERT, la.obj)

def clearTextWidget():  # Clear Both Text Widgets
    tb1.delete("1.0", "end")
    tb2.delete("1.0", "end")



file_button = Button(frame1,text="Open file", font="Helvetica 10 bold italic", command=openfile)
file_button.pack(side=LEFT, padx=20, pady=15)

Clear_button = Button(frame1,text="Clear", font="Helvetica 10 bold italic", command=clearTextWidget)
Clear_button.pack(side=LEFT, padx=20, pady=15)

Close_button = Button(frame1,text="Close", font="Helvetica 10 bold italic", command=root.destroy)
Close_button.pack(side=LEFT, padx=20, pady=15)


root.mainloop()
