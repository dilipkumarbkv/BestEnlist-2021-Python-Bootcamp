from tkinter import *
from tkinter import ttk

window = Tk()

#Window title

window.title("Registration Screen")


#Initialising Window size

window.geometry('720x580')

#Backgroung Color
window.configure(background = "purple")

label1= Label(window, text="Registration form",width=20,font = ("bold",16))
label1.grid(row =0, column = 4)

#Creating Labels

Firstname = Label(window, text="First Name").grid(row=4, column=0)

LastName = Label(window, text="Last Name").grid(row= 6, column=0)

Age = Label(window, text="Age").grid(row=8, column=0)

Email = Label(window, text="Email Id").grid(row=10, column=0)

Mobile1 = Label(window, text="Contact Number ").grid(row=12, column=0)

Mobile2 = Label(window, text="Alternate Number").grid(row=14, column=0)

Pan = Label(window, text="Pan Number").grid(row=16, column=0)

Aadhaar = Label(window, text="Aadhaar Number").grid(row=18, column=0)

tel = Label(window, text="telephone Number").grid(row=20, column=0)

col = Label(window, text="college name").grid(row=22, column=0)

roll = Label(window, text="roll number").grid(row=24, column=0)

sch = Label(window, text="school name").grid(row=26, column=0)

insta = Label(window, text=" instagram id").grid(row=28, column=0)

pn = Label(window, text="Parent Number").grid(row=30, column=0)

Gender = Label(window, text="Gender").grid(row=32, column=0)



Firstname1 = Entry(window).grid(row=4, column=1)

Lastname1 = Entry(window).grid(row=6, column=1)

Age1 = Entry(window).grid(row=8, column=1)

Email1 = Entry(window).grid(row=10, column=1)

Mobile11 = Entry(window).grid(row=12, column=1)

Mobile21 = Entry(window).grid(row=14, column=1)

pan1 = Entry(window).grid(row=16, column=1)

adhaar1 = Entry(window).grid(row=18, column=1)

tele1 = Entry(window).grid(row=20, column=1)

col1 = Entry(window).grid(row=22, column=1)

roll1 = Entry(window).grid(row=24, column=1)

sch1 = Entry(window).grid(row=26, column=1)

insta1 = Entry(window).grid(row=28, column=1)

pnr1 = Entry(window).grid(row=30, column=1)

# Radio Buttons

var = IntVar()
radio = Radiobutton(window, text="male", variable=var, value=1).grid(row=32, column=1)
radio = Radiobutton(window, text="female", variable=var, value=2).grid(row=33, column=1)


var1=IntVar()
Checkbutton(window,text= "I Accept, terms and conditions", variable=var1).place(x=70, y=430)

#function declaration

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)


btn = ttk.Button(window, text="Submit").place(x=70, y=480)
window.mainloop()
