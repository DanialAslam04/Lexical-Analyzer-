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
mainlb.place(x = 450, y = 10) 
   
inputlb=Label(frame1, text="... I N P U T ...", font=(74),borderwidth=8,background='#ffffff', relief="ridge")
inputlb.pack(padx=2, pady=2)

outputlb=Label(frame2, text="... O U T P U T ...", font=(74),borderwidth=8,background='#ffffff', relief="ridge")
outputlb.pack(padx=2, pady=2)

tb1 = Text(frame1, height=25, width=70)
tb1.pack(side=LEFT, padx=20, pady=15)

tb2 = Text(frame2, height=25, width=70)
tb2.pack(side=RIGHT, padx=30, pady=15, expand=1, fill=BOTH)

def openfile():
    tb1.insert(INSERT, la.obj+'\n')
    
def clearTextWidget():  # Clear Both Text Widgets
    tb1.delete("1.0", "end")
    tb2.delete("1.0", "end")

def run():
    #la.obj=tb1.get(0.0, "end-1c")
    la.start()
    tb2.insert(INSERT, "Space_Removed  "+str(la.space_remo)+'\n')
    tb2.insert(INSERT, 'Comments_Removed  '+str(la.comment_remo)+'\n')
    tb2.insert(INSERT,'Keyword  '+ str(la.keyword)+'\n')

    tb2.insert(INSERT, 'Idenifier  '+str(la.identifier)+'\n')

    tb2.insert(INSERT, 'constant  '+str(la.constant)+'\n')
    tb2.insert(INSERT, 'operators  '+str(la.operator)+'\n')
    tb2.insert(INSERT, 'symbols  '+str(la.symbol)+'\n')


file_button = Button(root,text=".. Open file ..", font="Helvetica 10 bold italic", command=openfile)
file_button.place(x=450, y=600)

run_button = Button(root,text=".. Run ..", font="Helvetica 10 bold italic", command=run)
run_button.place(x=600, y=600)

Clear_button = Button(root,text=".. Clear ..", font="Helvetica 10 bold italic", command=clearTextWidget)
Clear_button.place(x=700, y=600)

Close_button = Button(root,text=".. Close ..", font="Helvetica 10 bold italic", command=root.destroy)
Close_button.place(x=800, y=600)

root.mainloop()
