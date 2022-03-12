from tkinter import *
import random
root=Tk()
root.geometry("500x500")
root.title("sus")
scoreS=0
colorarray=["red","yellow","green","blue"]

score=Label(root,text="0")
score.place(relx=0.1,rely=0.1,anchor=CENTER)

answerl=Label(root)
answerl.place(relx=0.5,rely=0.35,anchor=CENTER)

enter=Entry(root)
enter.place(relx=0.5,rely=0.5,anchor=CENTER)

def start():
    answerl["fg"]= random.choice(colorarray)
    answerl["text"]= random.choice(colorarray)
def check():
    global scoreS
    if enter.get()==answerl["fg"]:
        scoreS=scoreS+1
        score["text"]=scoreS
        start()
    else:
        start()
Btn1=Button(root,text="CHECK",bg="red",command=check)
Btn1.place(relx=0.35,rely=0.6,anchor=CENTER)
Btn2=Button(root,text="START",bg="green",command=start)
Btn2.place(relx=0.65,rely=0.6,anchor=CENTER)
root.mainloop()