#Anagram Game:-
from tkinter import*
from tkinter import messagebox 
from tkinter import*
from PIL import Image,ImageTk
import random

roundd = 2
win = 0
count = 3

#Main work in between this function to get a word from external file:-
#make a jumbled to send a word to submit Function:-

def Give():
    global orignal_word,jumble
    with open("words.txt","r") as f: #Select a word only from the 'words.txt' file.
        words = f.readline().split() 

    word = random.choice(words)
    jumble = "".join(random.sample(word,len(word))) #jumble word here
    e1.delete(0,END)
    e1.insert(0,jumble)
    
    
    orignal_word = word #correct word stored
    print(orignal_word)
    
    
    
    
#it's button to catch a command and checking a user given word match or not 
def submit():
    global count,win,roundd
    user = e2.get().lower()
    try:
            
        if user == orignal_word:
            e1.insert(0,jumble)
            e1.delete(0,END)
            e2.delete(0,END)
            if roundd == 0:
                print()
            else:
                messagebox.showinfo("Good",f"Keep Going You want only need to\nwin {str(roundd)} rounds to succeed.")
            roundd-=1
            win+=1

        else:
            
            e1.delete(0,END)
            e1.insert(0,jumble)
            e2.delete(0,END)
            count-=1
            if count!=0:
                print()
                messagebox.showerror("Wrong","Wrong Guess,\nYou Loose chance "+str(count))
            else:
                print()
                messagebox.showwarning("Wrong","Your Chances is Exceed.Bye....")
                rt.destroy()

        l11.config(text=f"Score: {win}/5")
        if win == 3:
            messagebox.showinfo("Good","Congrulation,You\nWin Anagram Game!!!")
            rt.destroy()
        else:
            print()
        
        
    except Exception as e:
        messagebox.showwarning("Error","Enter Something!!!")


#-------------------------------------------------------------------|


#it's Second gui work.... 
# it's only for rules and use a Simple labels.

rt = Tk()
rt.title("Anagram-Game")
rt.geometry("400x400")

frame = Frame(rt)
frame.pack()

image = Image.open("anagramm.png")
photo = ImageTk.PhotoImage(image)
label = Label(frame, image=photo)
label.place(x=0,y=0,relwidth=1,relheight=1)

def ruls():
    global rg
    rg = Tk()
    rg.title("RULES")
    rg.geometry("400x300")
    
    second_frame = Frame(rg,bg="gray")
    second_frame.pack()
    
    
    rules = Label(second_frame,text="*_____________Rules_____________*",font=("Arial",12))
    rules.grid(row=4,column=0,columnspan=2,pady=10)

    rule_1 = Label(second_frame,text="1.Press the (Give) button a jumbled\n word will appear in the (Word) entry box..",font=("Arial",10,"bold"),bg="gray",fg="white")
    rule_1.grid(row=5,column=0,columnspan=2,pady=10)

    rule_2 = Label(second_frame,text="2.Click button to check if guess is right.",font=("Arial",10,"bold"),bg="gray",fg="white")
    rule_2.grid(row=6,column=0,columnspan=2,pady=10)

    rule_3 = Label(second_frame,text="Note:-Press 'Give', guess word, submit, win or loose.\nAnagram Game.Good luck....",font=("Arial",10,"bold"),bg="gray",fg="white")
    rule_3.grid(row=7,column=0,columnspan=2,pady=20)
    rg.after(15000,window)
    
    
    
def window():
    rg.destroy()

    
    
    

#it's First gui work 
# i take three label & two Entry and two button for play a decent game.


l = Label(frame,text="Anagram-Game",font=("Courier New",21,"bold"),fg="gray")
l.grid(row=0,column=0,columnspan=2,pady=10)

l1 = Label(frame,text="Word:=",font=("Arial",15,"bold"),anchor="w",fg="white",bg="#6F4E37")
l1.grid(row=1,column=0,padx=20,pady=(20,10),sticky="w")

e1 = Entry(frame,justify="center",font="bold")
e1.grid(row=1,column=1,padx=20,pady=(20,10),sticky="w")


#User choice catch from a answer label & give entry box---------|

l2 = Label(frame,text="Ans:=",font=("Arial",15,"bold"),anchor="w",fg="white",bg="#6F4E37")
l2.grid(row=2,column=0,padx=20,pady=20,sticky="w")

e2 = Entry(frame,justify="center",font="bold")
e2.grid(row=2,column=1,padx=20,pady=10,sticky="w")


#button--------------------------------------------------|

button1 = Button(frame,text="Give",font=("Courier New",15,"bold"),command=Give,bg="#8B4513",fg="white")
button1.grid(row=3,column=0,pady=10,columnspan=1)
 
button = Button(frame,text="click",font=("Courier New",15,"bold"),command=submit,bg="#8B4513",fg="white")
button.grid(row=3,column=1,columnspan=1,pady=10)

#Score Label--------------------------------------------------|

l11 = Label(frame,text=f"Score:- {str(win)}/5",font=("Arial",15,"bold"),fg="white",bg="#6F4E37")
l11.grid(row=4,column=0,columnspan=1,pady=70)

rules = Button(frame,text="Rules",font=("Courier New",15,"bold"),command=ruls,bg="#8B4513",fg="white")
rules.grid(row=4,column=1,pady=10)

#-----------------------------------------------------|
rt.mainloop() 

