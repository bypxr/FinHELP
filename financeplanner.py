#finance planner
import sys
import pyttsx3
from tkinter import *
engine = pyttsx3.init()
text = "Welcome to the financial help and education application. Our aim with this application was to provide users with the help and resources required to gain financial stability, step by step. Our application is simple and easy to navigate. Have a good time with the program!"
engine.say(text)
engine.runAndWait()

def Glossary():
    glosslisturl = "https://www.investopedia.com/financial-term-dictionary-4769738"
    print(glosslisturl)
    return glosslisturl
root=Tk()
def send():
    send="You =>" + e.get()
    txt.insert(END,"\n"+send)
    e.delete(0,END)
def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)
root.geometry("900x600")

l = Label(root, text = "DISCLAIMER")
l.config(font =("Courier", 14))
T = Text(root, height = 100, width = 100)

#Disclaimer
openingtext = """Welcome to the FinHelp/FinEdu program!
Please do remember that this advice is not all accurate and true,as
personal finance is very situational and it is hard to implicate that understanding into a program.
This advice can be taken into account after careful consideration.
This program is therefore legally irresponsible of any financial misfortunes."""
l.pack()
T.pack()
txt=Text(root)
T.insert(END, openingtext)

mainloop()
#MAIN






age = int(input("What is your age?"))

if age >= 18:
    print("Thank you for confirming that you are over 18.")
else:
    ans = input("This application is mostly for users over 18, but if you like, you can still go through the program. Would you like to do so?")
    if ans == "Yes".lower():
        print("Great!")
    else:
        sys.exit()


#FINAL DROPDOWN
        from tkinter import *
#module

#regional average functions

def NorthAmerica():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 40000
    avgexp = 20000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def LatinAmerica():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 6000
    avgexp = 2000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def SouthAmerica():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 10000
    avgexp = 4000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def Scandinavia():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 65000
    avgexp = 25000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def CentralEurope():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 50000
    avgexp = 25000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def EasternEurope():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 20000
    avgexp = 8000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def MiddleEast():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 40000
    avgexp = 20000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def NorthAfrica():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 10000
    avgexp = 4000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)
    
def CentralAfrica():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 6000
    avgexp = 2000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def SouthAfrica():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 12000
    avgexp = 5000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def IndianSubcontinent():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 6000
    avgexp = 2000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def CentralAsia():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 15000
    avgexp = 5000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def EastAsia():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 50000
    avgexp = 20000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

def Oceania():
    userinc = int(input("Input your income per year in USD ($)"))
    userexp = int(input("Input your expenses per year in USD ($)"))
    avginc = 50000
    avgexp = 25000
    incdeviation = userinc - avginc
    expdeviation = userexp - avgexp
    print("Ideal is the income deviation to be positive and expense to be negative")
    print("income deviation is",incdeviation,"expense deviation is",expdeviation)

root = Tk()

root.geometry( "500x500" )
regions = ["NorthAmerica",
           "LatinAmerica",
           "SouthAmerica",
           "Scandinavia",
           "CentralEurope",
           "EasternEurope",
           "MiddleEast",
           "NorthAfrica",
           "CentralAfrica",
           "SouthAfrica",
           "IndianSubcontinent",
           "CentralAsia",
           "EastAsia",
           "Oceania"]

def sayNA():
     mylabel=Label(root,text='NorthAmerica').pack()
     NorthAmerica()
def sayLA():
     mylabel=Label(root,text='LatinAmerica').pack()
     LatinAmerica()
def saySA():
     mylabel=Label(root,text='SouthAmerica').pack()
     SouthAmerica()
def saySC():
     mylabel=Label(root,text='Scandinavia').pack()
     Scandinavia()
def sayCE():
     mylabel=Label(root,text='CentralEurope').pack()
     CentralEurope()
def sayEE():
     mylabel=Label(root,text='EasternEurope').pack()
     EasternEurope()
def sayME():
     mylabel=Label(root,text='MiddleEast').pack()
     MiddleEast()
def sayNAF():
     mylabel=Label(root,text='NorthAfrica').pack()
     NorthAfrica()
def sayCEF():
     mylabel=Label(root,text='CentralAfrica').pack()
     CentralAfrica()
def saySAF():
     mylabel=Label(root,text='SouthAfrica').pack()
     SouthAfrica()
def sayCA():
     mylabel=Label(root,text='CentralAsia').pack()
     CentralAsia()
def sayEA():
     mylabel=Label(root,text='EastAsia').pack()
     EastAsia()
def sayIS():
     mylabel=Label(root,text='IndianSubcontinent').pack()
     IndianSubcontinent()
def sayOC():
     mylabel=Label(root,text='Oceania').pack()
     Oceania()
# Change the label text
def show():
        #mylabel=Label(root,text=clicked.get()).pack()
        if clicked.get()=='NorthAmerica':
             mybtn=Button(root,text='NorthAmerica',command=sayNA).pack()
             
        if clicked.get()=='LatinAmerica':
             mybtn=Button(root,text='Selection',command=sayLA).pack()
             
        if clicked.get()=='SouthAmerica':
             mybtn=Button(root,text='Selection',command=saySA).pack()
             
        if clicked.get()=='Scandinavia':
             mybtn=Button(root,text='Selection',command=saySC).pack()
             
        if clicked.get()=='CentralEurope':
             mybtn=Button(root,text='Selection',command=sayCE).pack()
             
        if clicked.get()=='EasternEurope':
             mybtn=Button(root,text='Selection',command=sayEE).pack()
             
        if clicked.get()=='MiddleEast':
             mybtn=Button(root,text='Selection',command=sayME).pack()
             
        if clicked.get()=='NorthAfrica':
             mybtn=Button(root,text='Selection',command=sayNAF).pack()
             
        if clicked.get()=='CentralAfrica':
             mybtn=Button(root,text='Selection',command=sayCEF).pack()
             
        if clicked.get()=='SouthAfrica':
             mybtn=Button(root,text='Selection',command=saySAF).pack()
             
        if clicked.get()=='CentralAsia':
             mybtn=Button(root,text='Selection',command=sayCA).pack()
             
        if clicked.get()=='EastAsia':
             mybtn=Button(root,text='Selection',command=sayEA).pack()
             
        if clicked.get()=='IndianSubcontinent':
             mybtn=Button(root,text='Selection',command=sayIS).pack()
             
        if clicked.get()=='Oceania':
             mybtn=Button(root,text='Selection',command=sayOC).pack()
             

# datatype of menu text
clicked = StringVar()

button = Button( root , text = "click Me" , command = show).pack()

# Create Dropdown menu
drop = OptionMenu( root , clicked , *regions)
drop.pack()


# Create Label
label = Label( root , text = " " )
label.pack()

# Execute tkinter
root.mainloop()

#AI CHATBOT
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
        txt.insert(END, "\n" + "Bot -> Fine! And you?")
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
#rest
print("If you do not have any of the means of income listed in the next part of this program, please type in 0.")
salary = int(input("What is your monthly salary, in case you have a job?"))
assetlist = 'Real estate','Intellectual properties', 'Royalties', 'Stocks', 'Bonds'
print("Please input 0 if any value is inapplicable to you.")
print(assetlist)
userasset1 = input("Which asset from this list do you have? Please select one. If there are none, then ignore.")
if userasset1 == 'real estate'.lower() or 'intellectual properties'.lower() or 'royalties'.lower() or 'stocks'.lower() or 'bonds'.lower():
    userasset1inc = int(input("How much is the expected monthly income from this asset?"))
else:
    userasset1inc = 0

print(assetlist)
userasset2 = input("Which asset from this list do you have? Please select another. If there are none, then ignore.")
if userasset2 == 'real estate'.lower() or 'intellectual properties'.lower() or 'royalties'.lower() or 'stocks'.lower() or 'bonds'.lower():
    userasset2inc = int(input("How much is the expected monthly income from this asset?"))
else:
    userasset2inc = 0

print(assetlist)
userasset3 = input("Which asset from this list do you have? Please select another. If there are none, then ignore.")
if userasset3 == 'real estate'.lower() or 'intellectual properties'.lower() or 'royalties'.lower() or 'stocks'.lower() or 'bonds'.lower():
    userasset3inc = int(input("How much is the expected monthly income from this asset?"))
else:
    userasset3inc = 0

print(assetlist)
userasset4 = input("Which asset from this list do you have? Please select another. If there are none, then ignore.")
if userasset4 == 'real estate'.lower() or 'intellectual properties'.lower() or 'royalties'.lower() or 'stocks'.lower() or 'bonds'.lower():
    userasset4inc = int(input("How much is the expected monthly income from this asset?"))
else:
    userasset4inc = 0

print(assetlist)
userasset5 = input("Which asset from this list do you have? Please select another. If there are none, then ignore.")
if userasset5 =='real estate'.lower() or 'intellectual properties'.lower() or 'royalties'.lower() or 'stocks'.lower() or 'bonds'.lower():
    userasset5inc = int(input("How much is the expected monthly income from this asset?"))
else:
    userasset5inc = 0

interestloanfrom = int(input("Have you lent any money to people with an interest rate? If so, how much money will this bring you in a month?"))

allowance = int(input("If you are given an allowance by a person or organization, roughly how much is it monthly?"))

totalmonthlyinc = salary + userasset1inc + userasset2inc + userasset3inc + userasset4inc + userasset5inc + interestloanfrom + allowance

print("Therefore, your total monthly income (not including other unincluded forms of income), is", totalmonthlyinc)



if totalmonthlyinc <= 0:
    print("Monthly income has to be above 0.")

if totalmonthlyinc > 0 and totalmonthlyinc < 2000:
    print("")
    
monthlyexp1 = int(input("How much is your monthly expense?"))

disposableinc1 = totalmonthlyinc - monthlyexp1
if disposableinc1 < 0:
        print("It is highly advised that you spend less than you earn.")
else:
    print("Great! Lets get started.")
if totalmonthlyinc > 2000:
    monthlyexp2 = int(input("How much is your monthly expense?"))
    disposableinc2 = totalmonthlyinc - monthlyexp2
    if disposableinc2 < 0:
        print("It is highly advised that you spend less than you earn.")
    else:
        print("Great! Lets get started.")

    

interestloanfor = int(input("Have you taken any loans, with or without interest, that you need to pay back? How much should be paid for this month?"))
if interestloanfor/monthlyexp1 >= 0.5:
    print("You need to save as much possible on other items and pay off the loan so that it does not take up too much of your earnings.")


print("Your income to expense ratio is", totalmonthlyinc/monthlyexp1 or totalmonthlyinc/monthlyexp2)
if totalmonthlyinc/monthlyexp1 <=1 or totalmonthlyinc/monthlyexp2 <=1:
    print("You spend as much as you earn or more! It is suggested that you spend less to keep your income to expense ratio low.")
else:
    print()
groceries = int(input("How much of the monthly income is groceries/food/water?"))
if groceries/monthlyexp1 >= 0.4 or groceries/monthlyexp2 >= 0.4:
    print("You need to spend less on groceries as it is taking up too much of your monthly income. May we suggest finding cheaper alternatives to products? Or having home cooked meals more often than going to restauraunts.")
if groceries/monthlyexp1 < 0.4 or groceries/monthlyexp2 <0.4:
    print("The groceries to monthly expense ratio is optimal.")
else:
    print("This value is invalid, and we cannot provide an output for you.")

rent = int(input("How much of the monthly expense is rent? If the house you are living in is owned by you, ignore this question by replying with a 0."))
if rent/monthlyexp1 >= 0.8 or rent/monthlyexp2 >= 0.8:
    print("The house you are living in is too costly as it takes up too much of your monthly expenses. It could be beneficial to live in a place with a lesser cost than your current housing.")
if rent/monthlyexp1 < 0.8 or rent/monthlyexp2 < 0.8:
    print("Your monthly expense on rent is efficient.")
else:
    print("This value is invalid, and we cannot provide an output for you.")


transport = int(input("How much of this monthly expense is regarding transport? This can include cost of maintaining your car or bike etc."))
if transport/monthlyexp1 >= 0.4 or transport/monthlyexp2 >= 0.4:
    print("The cost of transport is exceeding suitable limits when compared to your monthly expense. Therefore it is concluded that this cost should be reduced.")
if transport/monthlyexp1 < 0.4 or transport/monthlyexp2 < 0.4:
    print("The cost of transport is optimal.")
else:
    print("This value is invalid, and we cannot provide an output for you.")

leisureortech = int(input("How much of the monthly expenses go towards leisure and technology? For example, a monthly netflix subscription, or a weekly trip to the mall, or your Wi-fi connectio1n."))

if leisureortech/monthlyexp1 >= 0.4 or leisureortech/monthlyexp2 >= 0.4:
    print("Leisure is a very important part of life, however it must not take up too much of our monthly expenses in order to be financially stable. It is recommended that you decrease this amount.")
if leisureortech/monthlyexp1 < 0.4 or leisureortech/monthlyexp2 < 0.4:
    print("The leisure to expense ratio is optimal.")
else:
    print("This value is invalid, and we cannot provide an output for you.")


print("The amount of disposable income that you have is", disposableinc1 or disposableinc2)
print("This is not financial advice but simply a few ideas of what you could do with your disposable income.")
riskans = str(input("Do you think you can take a higher amount of risk while investing than average with your extra money?"))
if riskans == 'yes'.lower():
    if disposableinc1 > 0 and disposableinc1 < 1000:
        print("You can have minor investments in simple stocks or online currencies.")
    if disposableinc1 > 1000 and disposableinc1 <10000:
        print("You can have medium sized investments in stocks, bonds or online currencies.")
    if disposableinc1 > 10000:
        print("You can have major investments in real estate, or participate in online trading i.e stocks and cryptocurrencies.")

if riskans == 'no'.lower():
    if disposableinc1 > 0 and disposableinc1 < 1000:
        print("You can have small/gradual investments in steady/long term stocks, or save your money.")
    if disposableinc1 > 1000 and disposableinc1 <10000:
        print("You can have medium sized investments in things like mutual funds, save money, or invest in long term/steady stocks.")
    if disposableinc1 > 10000:
        print("You can have medium to major steady investments in real estate, stocks, stable/long term cryptocurrencies etc.")


glossaryrequest = input("Would you like to see the glossary of financial terms?")
if glossaryrequest == "Yes".lower():
    Glossary()
else:
    print("Seeing as you have not input 'yes', we will terminate the program")
















