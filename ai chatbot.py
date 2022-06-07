#AI CHATBOT
from tkinter import *

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    user = e.get().lower()

    if (user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")
    elif (user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")
    elif (user == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! and you")
    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")
    elif (user == "Thanks" or user == "Thank you"):
        txt.insert(END, "\n" + "Bot -> My pleasure !")
    elif (user == "Goodbye" or user == "See you later" or user == "see yaa"):
        txt.insert(END, "\n" + "Bot -> Thank you, Have a nice day!")
    elif (user=="let me check up on my financial knowledge" or user=="help me increase financial knowledge" or user=="let me know more about finances"):
        f=open("textbegin.txt",'r')
        a=f.read()
        txt.insert(END, "\n" + "Here are some resources:", a)
        f.close()
        fr=open("textintmed.txt",'r')
        b=fr.read()
        txt.insert(END, "\n" + "Here are some resources:", b)
        fr.close()
    elif (user=="nothing" or user=="stop"):
        txt.insert(END, "\n" + "Bot -> Okay!")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I did not understand that.")
    e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()
